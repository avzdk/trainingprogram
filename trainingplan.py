import datetime
from activity import Activity
from traininghistory import Traininglog

class TrainingPhase():

    def __init__(self,startdate,status,length=14):
        self.startdate=startdate
        self.enddate=startdate+datetime.timedelta(days=length-1)
        self.status = status #planned, done
        self.activities =[]

    def insert(self,activity):
        if activity.date >= self.startdate and activity.date <= self.enddate:
            self.activities.append(activity)
            return True
        else: return False  

    def __str__(self):
        return f"Phase: {self.startdate}-{self.enddate}  {self.status} {len(self.activities)}"


class TrainingPlan():

    def __init__(self,history):
        self.history=history    # Traininglog
        self.phases=[]
        

    def plan2weeks():
        None

    def create_calender(self,extraweeks=0):
        print(f"CHECK {self.history.lastdate-self.history.firstdate}")
        startdate=self.history.firstdate
        # startdate er mandagen i første uge med træning.
        startdate=startdate+datetime.timedelta(days=-self.history.firstdate.weekday()) # mandag er 0
        
        # korriger hvis der så bliver en phase med en uge uden træning
        span=(self.history.lastdate-self.history.firstdate).days
        if span%14 < 7: startdate=startdate-+datetime.timedelta(days=7)

        while startdate<self.history.lastdate:
            phase=TrainingPhase(startdate,"done")
            self.phases.append(phase)
            startdate=startdate+datetime.timedelta(days=14)
        for i in range(0,extraweeks):
            startdate=startdate+datetime.timedelta(days=14)
            phase=TrainingPhase(startdate,"planned")
            self.phases.append(phase)
        return self.phases

    def insert_activity(self,activity):
        for phase in self.phases:
            if phase.insert(activity) == True: break
    
    def load_history(self):
        for activity in self.history.activities: self.insert_activity(activity)
        return self.phases
        

        # dan kalender med phaser inkl. historik
        



if __name__ == "__main__":
    FILENAME="./testdata/5kmx3.csv"
    history=Traininglog()
    history.readcsvfile(FILENAME)
    #for i in history.activities: print(i)
    plan=TrainingPlan(history)
    a=plan.create_calender(10)
    #for p in a: print(p)
    phases=plan.load_history()
    for i in phases: print(i)
