from datetime import timedelta, datetime

class Timer:
    def __init__(self) -> None:
        self.prev_data = datetime(2000, 1, 1)
        self.now = datetime.now()

    def SetCurrentTime(self):
        self.now = datetime.now()

    def SetPrevData(self):
        self.prev_data = self.now
    
    def GetCurrentData(self):
        return self.now
    
    def GetPrevData(self):
        return self.prev_data
    
    def isGood(self):
        return self.now - self.prev_data >= timedelta(minutes=30)

