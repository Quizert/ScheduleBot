import parse_schedule

class Schedule:
    def __init__(self):
        self.parse_schedule = parse_schedule.Parser()
        self.subjects = self.parse_schedule.start()
        for subject in self.subjects:
            if len(subject) != 0:
                subject[0] = subject[0].replace('корейского', 'кор')
                subject[0] = subject[0].replace("Академическое", "Академ") 
                subject[0] = subject[0].replace("Python", "Петухоне") 

    def GetFirst(self):
        return [self.subjects[subject] for subject in range(2, 33, 6)]

    def GetSecond(self):
        return [self.subjects[subject] for subject in range(3, 34, 6)]

    def GetThird(self):
        return [self.subjects[subject] for subject in range(4, 35, 6)]

    def GetFourth(self):
        return [self.subjects[subject] for subject in range(5, 36, 6)]

    def GetFifth(self):
        return [self.subjects[subject] for subject in range(6, 37, 6)]

    def GetSixth(self):
        return [self.subjects[subject] for subject in range(7, 38, 6)]
    
    def GetSchedule(self):
        schedule = {
            "09:30-10:50" : self.GetFirst(),
            "11:10-12:30" : self.GetSecond(),
            "13:00-14:20" : self.GetThird(),
            "14:40-16:00" : self.GetFourth(),
            "16:20-17:40" : self.GetFifth(),
            "18:10-19:30" : self.GetSixth()
        }
        return schedule
