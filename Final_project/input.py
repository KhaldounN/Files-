import datetime
class dates():
    def __init__(self):
        self.day = ""

    def validate(self,date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y%m%d')
            return True
        except ValueError:
            return False


    def daysBefore(self):

        print("Write the day. YYYY/MM/DD, Ex:2020101 ")
        self.day = input()
        if self.validate(self.day):
            return self.day
        else:
            self.daysBefore(self.day)
