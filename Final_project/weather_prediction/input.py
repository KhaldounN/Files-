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

            if int(self.day) >= self.protect1 and int(self.day) <= self.protect2:
                return self.day
            else:
                print("Outside of data")
                self.daysBefore()
        else:
            self.daysBefore()
