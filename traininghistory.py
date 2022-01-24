import csv
import datetime
from activity import Activity


class Traininglog():

    def __init__(self):
        self.activities=[]

    def _sortlist(self):
        self.activities.sort(key=lambda x: x.date)

    @property
    def firstdate(self):
        return self.activities[0].date

    @property
    def lastdate(self):
        return self.activities[-1].date

    
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

if __name__ == "__main__":
    FILENAME="./testdata/5kmx3.csv"
    traininglog=Traininglog()
    traininglog.readcsvfile(FILENAME)
    for i in traininglog.activities:
        print(i)
    print(traininglog.firstdate)
    print(traininglog.lastdate)
