# windyWillow
Windy Willow is a mock-up wind farm that uses data from wind generation and electricity pricing APIs to make better business and maintenance decisions. 

# Project overview



# How to run files 

Open 3 terminals, one for each of the python scripts: windProducer, windConsumer, and forecastProducer.
These scripts run in Python 2.7. 
Run each script, starting with windProducer (red window in the screenshot).
The blue window in the screenshot is the windConsumer; this will show a dataframe every 5 seconds with information from the APIs as well as an action and calculated potential revenue.  
The green window in the screenshot is forecastProducer, which streams Windy Willow's predicted prices 20 seconds.  

The bottom right corner of the screenshot shows a Tabluea dashboard that is reading the streaming data from text files and producing live visuals.  

![image](https://user-images.githubusercontent.com/65284472/103562042-ba374500-4eba-11eb-830a-9e19f405f903.png)


