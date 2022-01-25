import datetime
import pandas as pd
from activity import Activity
from traininghistory import Traininglog
from chart import plot
import math

INCPCT=1.10     # Hvor meget løbes der ekstra fra uge til uge

class TrainingPhase():
    '''En fase er 14 dage. Fasen indeholder en liste af aktiviteter
    '''
    next_phasenumber=1  # count variabel

    def __init__(self,startdate,status,length=14):
        self.startdate=startdate
        self.enddate=startdate+datetime.timedelta(days=length-1)
        self.status = status #planned, done
        self.activities =[]
        self.incpct=None #procent forøgelse. 
        self.phasenumber =TrainingPhase.next_phasenumber
        TrainingPhase.next_phasenumber=TrainingPhase.next_phasenumber+1

    def insert(self,activity):
        # checker om datoen passer og indsætter hvis ok
        if activity.date >= self.startdate and activity.date <= self.enddate:
            self.activities.append(activity)
            return True
        else: return False  

    def _getsubphase(self,date):
        if (date-self.startdate).days>=7: 
            return 'w2'        
        else: return 'w1'
        


    def get_dataframe(self):
        ''' Samler data fra alle aktiviteter og returnerer en liste
        der tilføjes kolonner med data fra fasen som er ens for alle aktiviteter'''
        df=pd.DataFrame()
        for activity in self.activities:
            df_activity=activity.get_dataframe()
            df_activity['phase_subphase']=self._getsubphase(activity.date)
            df = pd.concat([df,df_activity])
            df['phase_status']=self.status 
            df['phase_startdate']=self.startdate
            df['phase_number']=self.phasenumber
            df['phase_incpct']=self.incpct
        return df

    def get_summery(self):
        '''Returnerer nogle summerede værdier fra phasens aktiviteter
        '''
        number_of_activities = 0        
        distance_sum = 0
        distance_max = 0
        
        for activity in self.activities:
            number_of_activities+=1
            distance_sum+=activity.distance 
            distance_max = max(distance_max,activity.distance)
        return number_of_activities, distance_sum, distance_max

    def __str__(self):
        number_of_activities, distance_sum, distance_max = self.get_summery()
        return f"Phase: #{self.phasenumber} {self.startdate}-{self.enddate}  {self.status} {number_of_activities, distance_sum, distance_max} + "


class TrainingPlan():
    ''''Den samlede træningsplan inkl. faser.
    Historikken optræder to gange. Både som sevlstænding self.history og som del af phaserne.
    '''

    def __init__(self,history):
        self.history=history    # Traininglog
        self.phases=[]

    def create_calender(self):
        ''' Danner en "kalender" med de faser der skal til, inkl. historiske fraser markeret med "done"
        Der fyldes ikke data i på nuværende tidspunkt. det er selvstændig funktion.
        '''
        startdate=self.history.firstdate
        # startdate er mandagen i første uge med træning.
        startdate=startdate+datetime.timedelta(days=-self.history.firstdate.weekday()) # mandag er 0
        
        # korriger hvis der så bliver en phase med en uge uden træning
        span=(self.history.lastdate-self.history.firstdate).days
        if span%14 < 7: startdate=startdate-+datetime.timedelta(days=7)

        # historiske faser
        while startdate<self.history.lastdate:
            phase=TrainingPhase(startdate,"done")
            self.phases.append(phase)
            startdate=startdate+datetime.timedelta(days=14)
        # fremtidige faser


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

    def get_summery(self,phases):
        '''Analyserer en liste af phaser og returnerer nogle nøgletal'''
        distance_max = 0
        distance_sum = 0
        number_of_activities = 0
        number_of_phases = len(phases)
        for phase in phases:
            p_number_of_activities, p_distance_sum, p_distance_max = phase.get_summery()
            number_of_activities+=p_number_of_activities
            distance_sum+=p_distance_sum
            distance_max = max(distance_max,p_distance_max)
        return number_of_activities, distance_sum, distance_max, number_of_phases

    def planweeks(self,inputphases):
        ''' baseret på en liste af phaser dannes næste phase'''

        number_of_activities, distance_sum, distance_max,number_of_phases = plan.get_summery(inputphases)
        print(f"A SUM MAX={number_of_activities, distance_sum, distance_max}")     
        distance_sum_per_phase=distance_sum/number_of_phases

        phase_startdate =inputphases[-1].startdate+datetime.timedelta(days=14)
        newphase=TrainingPhase(phase_startdate,'planned')
        newphase.incpct=1+  (1-(1/(1+math.e**(6-distance_sum_per_phase/10))))/15
        print(f"INCPCT ={newphase.incpct}")
        new_sum = distance_sum_per_phase * newphase.incpct * newphase.incpct # 14 dage
        print(f"lastsum {distance_sum_per_phase}")
        print(f"newsum {new_sum}")

        distances={}

        if new_sum<35:
            # 2 + 3 TURE    
            distances['Lang']=distance_max * newphase.incpct* newphase.incpct*0.98
            sum_mellem=(new_sum-distances['Lang'])*0.7
            sum_kort=new_sum-distances['Lang']-sum_mellem
            distances['Mellem']=sum_mellem/2
            distances['Kort']=sum_kort/2
            template=[(1,'Kort'),(4,'Mellem'),(7,'Mellem'),(10,'Kort'),(13,'Lang')]
        elif new_sum<50:
        # 3 + 3 TURE A
            distances['Lang']=distance_max * newphase.incpct* newphase.incpct*0.98
            sum_mellem=(new_sum-distances['Lang'])*0.7
            sum_kort=new_sum-distances['Lang']-sum_mellem
            distances['Mellem']=sum_mellem/2
            distances['Kort']=sum_kort/3
            template=[(1,'Kort'),(3,'Mellem'),(5,'Kort'),(8,'Mellem'),(10,'Kort'),(13,'Lang')]
        elif new_sum<60:   
        # 3 + 3 TURE B
            distances['Lang']=distance_max * newphase.incpct* newphase.incpct*0.98
            sum_mellem=(new_sum-distances['Lang'])*0.7
            sum_kort=new_sum-distances['Lang']-sum_mellem
            distances['Mellem']=sum_mellem/3
            distances['Kort']=sum_kort/2
            template=[(1,'Kort'),(3,'Mellem'),(5,'Mellem'),(8,'Mellem'),(10,'Kort'),(13,'Lang')]
        elif new_sum<70:
            # 4 + 3 TURE
            distances['Lang']=distance_max * newphase.incpct* newphase.incpct*0.98
            sum_mellem=(new_sum-distances['Lang'])*0.7
            sum_kort=new_sum-distances['Lang']-sum_mellem
            distances['Mellem']=sum_mellem/3
            distances['Kort']=sum_kort/3
            template=[(1,'Kort'),(3,'Mellem'),(5,'Kort'),(6,'Mellem'),(8,'Mellem'),(10,'Kort'),(13,'Lang')]
        else:
            # 4 + 4 TURE
            distances['Lang']=distance_max * newphase.incpct* newphase.incpct*0.98
            sum_mellem=(new_sum-distances['Lang'])*0.7
            sum_kort=new_sum-distances['Lang']-sum_mellem
            distances['Mellem']=sum_mellem/4
            distances['Kort']=sum_kort/3
            template=[(1,'Kort'),(3,'Mellem'),(5,'Mellem'),(6,'Kort'),(7,'Mellem'),(9,'Mellem'),(10,'Kort'),(13,'Lang')]

        

        new_activities=[]
        for t in template:
            new_activity=Activity(phase_startdate+datetime.timedelta(days=t[0]-1), distances[t[1]]  ,trainingtype=t[1])
            newphase.insert(new_activity)
        self.phases.append(newphase)



if __name__ == "__main__":
    FILENAME="./testdata/allan202201.csv"
    history=Traininglog()
    history.readcsvfile(FILENAME)
    #for i in history.activities: print(i)
    plan=TrainingPlan(history)
    
    a=plan.create_calender()
    phases=plan.load_history()
    for p in a: print(p)
    
    #print(plan.get_dataframe())

    number_of_activities, distance_sum, distance_max, number_of_phases = plan.get_summery(plan.phases)
    #print(number_of_activities, distance_sum, distance_max)
    inputphases=plan.phases  # hele historikken
    plan.planweeks(plan.phases)
    for i in range(0,10):
        inputphases=[plan.phases[-2],plan.phases[-1]]
        plan.planweeks(inputphases)
    plotter=plot()
    print("RESULTAT----------------")
    print(plan.get_dataframe().to_string())
    plotter.drawByDate(plan.get_dataframe())
