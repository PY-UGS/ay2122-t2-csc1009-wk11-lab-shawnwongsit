class ClockTime:
    
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def setHours(self, hours):
        self.hours = hours

    def setMinutes(self, min):
        self.minutes = min

    def setSeconds(self, sec):
        self.sec = sec

    def setTime(self, time):
        self.time = time

    def showTime(self):
        print(str(self.hours)+":"+str(self.minutes)+":"+str(self.seconds))

ct = ClockTime(16,30,10)
ct.showTime()
