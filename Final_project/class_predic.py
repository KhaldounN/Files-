class Weather_prediction():
    def __init__(self,ai_temp,ai_rain,ai_claud,date):
        self.ai_temp = ai_temp
        self.ai_rain = ai_rain
        self.ai_claud = ai_claud
        self.date = date
    def get_weather_7days(self,time):
        Local_holder = 0
        seven_days_temp = []
        seven_days_rain = []
        seven_days_claud = []
        for i in range(int(len(self.date))):
            if time == self.date[i][0]:
                Local_holder = i
        for k in reversed(range(1,8)):
            seven_days_temp.append(self.date[Local_holder - k][3])
            seven_days_rain.append(self.date[Local_holder - k][1])
            seven_days_claud.append(self.date[Local_holder - k][4])
        return seven_days_temp , seven_days_rain , seven_days_claud
    def predict_weather_for(self,time):
        temp , rain , claud = self.get_weather_7days(time)
        return [self.ai_temp.predict([temp])],[self.ai_rain.predict([rain])],[self.ai_claud.predict([claud])]
