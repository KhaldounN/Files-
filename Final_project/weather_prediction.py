import pandas as pd


#from other file
import class_predic
import input
import AI
import interface


### import CSV
date = []
data = pd.read_csv('dataexport_20200921T130310.csv')


#data -> Raining & Snow & Basel Temperature [2 m elevation corrected] mean & cloud_cover_low

for i,d in enumerate((data["location"])):
    if d.startswith("2015") or d.startswith("2016") or d.startswith("2017") or d.startswith("2018") or d.startswith("2019"):
        date.append([d[:-5],float(data["Basel.9"][i]),float(data["Basel.10"][i]),float(data["Basel.2"][i]),float(data["Basel.14"][i])]) # to remove T0000 things [:-5]


##### AI file
AI = AI.AI_parsing(date)
AI_done = AI.loop_parsing()
temp_KNN = AI_done[0]
rain_KNN = AI_done[1]
claud_KNN = AI_done[2]



##### input file
day_input = input.dates()
day_output = day_input.daysBefore()
#print(day_output)

### class_predic file
AX = class_predic.Weather_prediction(temp_KNN , rain_KNN , claud_KNN, date)
predic_dato = AX.predict_weather_for(day_output)

## interface
interface = interface.interface(predic_dato)
interface.print_interface()
