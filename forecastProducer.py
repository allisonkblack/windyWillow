from time import sleep

print("Reading file...")
sleep(60)
with open('price_forecast.tsv') as f:
    for line in f:
        print(line)
        sleep(60)
print('End Of Stream.')
