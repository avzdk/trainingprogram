import datetime
import pandas as pd

class Activity():
    def __init__(self,date,distance,time=None,trainingtype='Running'):
        self.date=date
        self.distance=distance
        self.time = time
        self.trainingtype=trainingtype
        self.inserted=False

    @property
    def isoYW(self): #isoYear and isoWeek
        return str()+f"{self.date.isocalendar()[0]}-{self.date.isocalendar()[1]:02}"

    @property
    def weekstart(self): #mandag i ugen
        d=self.date
        d+= datetime.timedelta(days=-self.date.weekday()) # mandag er 0
        return d

    def get_dataframe(self):
        ''' danner en df med én række
        '''
        df = pd.DataFrame(columns=['date','distance','trainingtype'])
        df.loc[0] = [self.date,self.distance,self.trainingtype]
        return df

    def __str__(self):
        return f"Activity: {self.date} ({self.isoYW}) {self.distance} km in {self.time} doing {self.trainingtype}"


if __name__ == "__main__":
    my_activity=Activity(datetime.date.today(),42.2,242.5,"Race")
    print(my_activity)
    print(my_activity.get_dataframe())
