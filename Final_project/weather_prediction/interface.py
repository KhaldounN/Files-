class interface():

    def __init__(self, predic_dato):
        self.design_sun = ["   \  /   ", " - (  ) - ", "   /  \   "]
        self.design_rain = [" ~~~~~~~~ "," ~||~||~ ~","   ||  || "]
        self.design_shower = [" ~~~~~~~~ "," ~~ ~~~ ~ ","   ||  || "]
        self.design_cloud = ["~~ ~~~~~ ~","~~~ ~~ ~~~","~  ~~ ~ ~~"]
        self.data_sun = 0
        self.data_rain = int(predic_dato[1][0][0])
        self.data_cloud = int(predic_dato[2][0][0])
        self.temp = int(predic_dato[0][0][0])
        self.say =""

    def print_interface(self):
        if self.data_rain == 0:

            if self.data_cloud > 35:
                ## cloudy
                self.say = "Cloudy"
                self.make_interface(self.design_cloud)

            else:
                #Sun
                self.say = "Sunny Day"
                self.make_interface(self.design_sun)

        else:
            ## Raining
            if self.data_rain == 1:
                self.say = "Shower" +"  " + str(self.data_rain)+"mm"
                self.make_interface(self.design_shower)

            else:
                self.say = "Raining" +"  " + str(self.data_rain)+"mm"
                self.make_interface(self.design_rain)


    def make_interface(self, design):
        print("")
        print("==============")

        for i in design:
            print("||",end="")
            print(i, end="")
            print("||")
        print("==============")
        print(self.say)
        print(f"Average temp: {self.temp}°C, {(self.temp * 9 / 5) + 32}°F")
        print("==============")
