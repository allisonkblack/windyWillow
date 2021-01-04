# windyWillow
Windy Willow is a mock-up wind farm that uses data from wind generation and electricity pricing APIs to make better business and maintenance decisions. 

# Project overview
### What and why?

Windy Willow obtains near real-time data from a mock-up wind generator API and the REData API from Red Electrica, a Spansih corporation which operates the national electricity grid in Spain. Windy Willow uses this data to make better decisions on when and to whom to sell their wind power, as well as when to maintain their wind turbines. 

## Dependencies 
python 2.7

![image](https://user-images.githubusercontent.com/65284472/103562042-ba374500-4eba-11eb-830a-9e19f405f903.png)

## Executing Program 
* open 3 terminals, one for each of the python scripts
* first terminal window: 
```
python windProducer.py
```
* second terminal window:
```
python windConsumer.py
```
* third terminal window:
```
python forecastProducer.py
```



The red window in the screenshot is the windProducer.

The blue window in the screenshot is the windConsumer; this will show a dataframe every 5 seconds with information from the APIs as well as an action and calculated potential revenue. By setting thresholds on the wind generated in megawatts (MW), an action is produced in the output to guide a business decision. The price_euros column gives the real-time market price of energy from Red Electrica. The potential_revenue column multiplies the wind column and price_euros columns. 

The green window in the screenshot is forecastProducer, which streams Windy Willow's predicted prices 20 seconds.  

The bottom right corner of the screenshot shows a Tableau dashboard that is reading the streaming data from text files and producing live visuals.  



