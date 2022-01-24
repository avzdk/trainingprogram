import datetime
import pandas as pd
from activity import Activity
from traininghistory import Traininglog
from chart import plot

class TrainingPhase():
    next_phasenumber=1

    def __init__(self,startdate,status,length=14):
        self.startdate=startdate
        self.enddate=startdate+datetime.timedelta(days=length-1)
        self.status = status #planned, done
        self.activities =[]
        self.phasenumber =TrainingPhase.next_phasenumber
        TrainingPhase.next_phasenumber=TrainingPhase.next_phasenumber+1

    def insert(self,activity):
        # checker om datoen passer og indsætter hvis ok
        if activity.date >= self.startdate and activity.date <= self.enddate:
            self.activities.append(activity)
            return True
        else: return False  

    def __str__(self):
        return f"Phase: {self.startdate}-{self.enddate}  {self.status} {len(self.activities)}"

    def get_dataframe(self):
        ''' Samler data fra alle aktiviteter og returnerer en liste
        der tilføjes kolonner med data fra fasen som er ens for alle aktiviteter'''
        df=pd.DataFrame()
        for activity in self.activities:
            df = pd.concat([df,activity.get_dataframe()])
            df['phase_status']=self.status 
            df['phase_startdate']=self.startdate
            df['phase_number']=self.phasenumber
        return df

class TrainingPlan():

    def __init__(self,history):
        self.history=history    # Traininglog
        self.phases=[]
        

    def plan2weeks():
        None

    def create_calender(self,extraweeks=0):
        ''' Danner en "kalender" med de faser der skal til, inkl. historiske fraser markeret med "done"
        Der fyldes ikke data i på nuværende tidspunkt. det er selvstændig funktion.
        '''
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
        '''Forsøger at indsætte en aktivitet i alle phaser. Den checker om lovlit. Hvis det lykkes så stoppes loopet
        '''
        for phase in self.phases:
            if phase.insert(activity) == True: break
    
    def load_history(self):
        '''Indsætter hele historikken i den oprettede kalender
        '''
        for activity in self.history.activities: self.insert_activity(activity)
        return self.phases

    def get_dataframe(self):
        df=pd.DataFrame()
        for phase in self.phases:
            df = pd.concat([df,phase.get_dataframe()])
        return df





if __name__ == "__main__":
    FILENAME="./testdata/5kmx3.csv"
    history=Traininglog()
    history.readcsvfile(FILENAME)
    #for i in history.activities: print(i)
    plan=TrainingPlan(history)
    a=plan.create_calender(10)
    #for p in a: print(p)
    phases=plan.load_history()
    print(plan.get_dataframe())
    plotter=plot()
    plotter.draw(plan.get_dataframe())
    
