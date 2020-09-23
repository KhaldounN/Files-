class interface():

    def __init__(self, predic_dato):
        self.design_sun = ["   \  /   ", " - (  ) - ", "   /  \   "]
        self.design_rain = [" ~~~~~~~~ ","  || ||   ","   ||  || "]
        self.design_cloud = ["~~ ~~~~~ ~","~~~ ~~ ~~~","~  ~~ ~ ~~"]
        self.data_sun = 0
        self.data_rain = int(predic_dato[1][0][0])
        self.data_cloud = int(predic_dato[2][0][0])
        self.temp = int(predic_dato[0][0][0])
        self.say =""

    def print_interface(self):
        if self.data_rain > 0:

            if self.data_cloud > 35:
                ## cloudy
                self.say = "Cloudy"
                self.make_interface(self.data_cloud,self.design_cloud,self.say)

            else:
                #Sun
                self.say = "Sunny Day"
                self.make_interface(self.data_sun, self.design_sun,self.say)

        else:
            ## Raining
            self.say = "Raining"
            self.make_interface(self.data_rain, self.design_rain,self.say)

    def make_interface(self, data, design,say):
        print("")
        print("==============")

        for i in design:
            print("||",end="")
            print(i, end="")
            print("||")
        print("==============")
        print(self.say)
        print("Temp : {}".format(self.temp))
        print("==============")
