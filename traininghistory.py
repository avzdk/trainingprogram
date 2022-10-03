import csv
import datetime
from activity import Activity
from strava import Strava

class Traininglog():

    def __init__(self):
        self.activities=[]

    def _sortlist(self):
        self.activities.sort(key=lambda x: x.date)


    def groupbydate(self):
        
        for i in range(1,len(self.activities)):
            if self.activities[i].date == self.activities[i-1].date:
                self.activities[i].combine(self.activities[i-1])
                self.activities[i-1].combined=True   # markeret til sletning.add()
        filtered = filter(lambda x: x.combined==False ,self.activities)    
        self.activities=list(filtered)
            


    @property
    def firstdate(self):
        return self.activities[0].date

    @property
    def lastdate(self):
        return self.activities[-1].date

    def readstrava(self,pagesize=20):
        client=Strava()
        client.getToken()
        activities = client.getActivities(pagesize)
        for a in activities:
            if a['type']=='Run':
                date=datetime.datetime.strptime(a['start_date'][0:10], "%Y-%m-%d").date()
                distance=float(a['distance'])/1000
                time=float(a['moving_time'])/60
                activity=Activity(date,distance,time)        
                self.activities.append(activity)
        self._sortlist()
        return self.activities

    
    def readcsvfile(self,filename):
        reader = csv.reader(open(filename), delimiter=";")
        next(reader, None)  # skip the headers
        for row in reader:
            date=datetime.datetime.strptime(row[0], "%d/%m/%Y").date()            
            distance=float(row[1])
            time=float(row[2][0:2])*60+float(row[2][3:5])+float(row[2][6:8])/60
            activity=Activity(date,distance,time)        
            self.activities.append(activity)
        self._sortlist()
        return self.activities

    def distance_list(self):
        list=[]
        for i in traininglog.activities:
            list.append(i.distance)
        return list



    def summary(self):
        days=abs((traininglog.lastdate - traininglog.firstdate).days)+1
        activitiecount=len(self.activities)
        weeklyruns=(activitiecount/days)*7
        print(f"SUMMARY: Baseret på {days} dage og {activitiecount} ture svarende til {weeklyruns} ture pr. uge.")
        print(f"SUMMARY: Længste {max(self.distance_list())} og korteste {min(self.distance_list())}")
        
        

if __name__ == "__main__":
    FILENAME="./testdata/5kmx3.csv"
    traininglog=Traininglog()
    #traininglog.readcsvfile(FILENAME)pip in
    traininglog.readstrava(20)
    traininglog.groupbydate()
    for i in traininglog.activities:
        print(i)
    print(f"First date  in data {traininglog.firstdate}")
    print(f"First date  in data {traininglog.lastdate}")
    traininglog.summary()
