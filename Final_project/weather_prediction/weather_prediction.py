##https://www.meteoblue.com/en/weather/archive/export/basel_switzerland_2661604?daterange=2020-09-15%20to%202020-09-22&min=2020-09-15&max=2020-09-22&domain=NEMSAUTO&params=&params%5B%5D=temp2m&params%5B%5D=relhum2m&params%5B%5D=pressure&params%5B%5D=precip&params%5B%5D=snow&params%5B%5D=totalClouds&params%5B%5D=clouds&params%5B%5D=sunshine&params%5B%5D=swrad&params%5B%5D=directrad&params%5B%5D=diffuserad&params%5B%5D=evapotrans&params%5B%5D=faoreference&params%5B%5D=cape&params%5B%5D=windgust&params%5B%5D=wind%2Bdir10m&params%5B%5D=wind%2Bdir80m&params%5B%5D=wind%2Bdir900mb&params%5B%5D=wind%2Bdir850mb&params%5B%5D=wind%2Bdir700mb&params%5B%5D=wind%2Bdir500mb&params%5B%5D=gpt1000mb&params%5B%5D=gpt850mb&params%5B%5D=gpt700mb&params%5B%5D=gpt500mb&params%5B%5D=temp1000mb&params%5B%5D=temp850mb&params%5B%5D=temp700mb&params%5B%5D=tempsfc&params%5B%5D=soiltemp0to10&params%5B%5D=soilmoist0to10&params%5B%5D=vpd2m&utc_offset=2&timeResolution=hourly&temperatureunit=CELSIUS&velocityunit=KILOMETER_PER_HOUR&energyunit=watts&lengthunit=metric

import pandas as pd


#from other file
import class_predic
import input
import AI
import interface


### import CSV
date = []
data = pd.read_csv('dataexport_20200925T050912.csv')


#data -> Raining & Snow & Basel Temperature [2 m elevation corrected] mean & cloud_cover_low

for i,d in enumerate((data["location"])):
    if i>=9:
        date.append([d[:-5],float(data["Basel.9"][i]),float(data["Basel.2"][i]),float(data["Basel.14"][i])]) # to remove T0000 things [:-5]


##### AI file
AI = AI.AI_parsing(date)
AI_done = AI.loop_parsing()
temp_KNN = AI_done[0]
rain_KNN = AI_done[1]
claud_KNN = AI_done[2]



##### input file
protect1 = int(date[0][0])
protect2 = int(date[-1][0])
day_input = input.dates(protect1, protect2)
day_output = day_input.daysBefore()
#print(day_output)

### class_predic file
AX = class_predic.Weather_prediction(temp_KNN , rain_KNN , claud_KNN, date)
predic_dato = AX.predict_weather_for(day_output)

## interface
interface = interface.interface(predic_dato)
interface.print_interface()


#### Real Data from 20150108 to today(20200925)
for i in range(len(date)):
    if date[i][0].startswith(str(day_output)):
        print(date[i])
