import datetime
class dates():
    def __init__(self,protect1,protect2):
        self.day = ""
        self.protect1 = protect1 +7
        self.protect2 = protect2 +1

    def validate(self,date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y%m%d')
            return True
        except ValueError:
            return False


    def daysBefore(self):

        print("Write the day. YYYY/MM/DD, Ex:20200101, From 20150108 to Tomorrow(20200926)")
        self.day = input()
        if self.validate(self.day):


            # if the final data is the end day of month. Then it should be the first day of month
            if self.validate(str(self.protect2)) == False:
                self.protect2 -= 1
                new = datetime.datetime.strptime(str(self.protect2), '%Y%m%d')
                next_day = new + datetime.timedelta(days=1)

                if int(next_day.month) < 10 :
                    self.protect2 = str(next_day.year) + str(0) + str(next_day.month) + str(0) + str(next_day.day)
                    #print(self.protect2)
                else:
                    self.protect2 = str(next_day.year) + str(next_day.month) + str(0) + str(next_day.day)
                    #print(self.protect2)

            if int(self.day) >= self.protect1 and int(self.day) <= int(self.protect2):
                return self.day
            else:
                print("Outside of data")
                self.daysBefore()

        else:
            self.daysBefore()
