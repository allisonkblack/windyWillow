import json
from time import sleep
import os
import sys


import requests
import datetime
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import Row, SQLContext

f = open(os.devnull, 'w')
sys.stderr = f


def get_sql_context_instance(spark_context):
    if 'sqlContextSingletonInstance' not in globals():
        globals()['sqlContextSingletonInstance'] = SQLContext(spark_context)
    return globals()['sqlContextSingletonInstance']


# create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def convert_date_string(string_date):
    time_obj = datetime.datetime.strptime(string_date, "%d/%m/%y %H:%M")
    time_obj2 = time_obj + datetime.timedelta(hours=1)
    return [time_obj.strftime('%Y-%m-%dT%H:%M'), time_obj2.strftime('%Y-%m-%dT%H:%M')]


def get_price(date_times):
    resp = requests.get('https://apidatos.ree.es/en/datos/mercados/precios-mercados-tiempo-real?' +
                        'start_date=' + date_times[0] +
                        '&end_date=' + date_times[1] +
                        '&time_trunc=hour')

    data = resp.json()
    price = data["included"][1]["attributes"]["values"][0]["value"]
    return price


def get_action(wind):
    wind_int = int(wind)
    if wind_int < 1800:
        return "Call the insurance"
    elif wind_int < 2500:
        return "Sell/Store"
    else:
        return "Shutdown"


def process_wind(time, rdd):
    if not rdd.isEmpty():
        sql_context = get_sql_context_instance(rdd.context)
        # convert the RDD to Row RDD
        row_rdd = rdd.map(lambda w: Row(timestamp=w[0], wind=w[1], action=get_action(w[1]),price_euros=get_price(convert_date_string(w[0])), potential_revenue=round(float(w[1])*float(get_price(convert_date_string(w[0]))),0)))
        # create a DF from the Row RDD
        values_df = sql_context.createDataFrame(row_rdd)
        values_df.write.csv("output", mode='append', header=True)
        values_df.show()
        


# create spark context with the above configuration
sc = SparkContext('local[*]', appName="WindConsumer")
sc.setLogLevel("ERROR")
# create the Streaming Context from the above spark context with interval size 5 seconds
ssc = StreamingContext(sc, 5)

# setting a checkpoint to allow RDD recovery
#ssc.checkpoint("checkpoint")

# read data from the port
dataStream = ssc.socketTextStream("127.0.0.1", 12345)
lines = dataStream.map(lambda line: line.decode().split(","))

if lines.count() != 0:
    lines.foreachRDD(process_wind)

# start the streaming computation
ssc.start()
# wait for the streaming to finish
ssc.awaitTermination()
#sleep(10)
ssc.stop(stopSparkContext=True, stopGraceFully=True)
