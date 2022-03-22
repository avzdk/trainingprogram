import plotly.express as px
<<<<<<< HEAD
import datetime
=======
from datetime import datetime
>>>>>>> 6a96c36e32215ef34d4da654bb5f9e5aea1df59d

class plot():
    
    def __init__(self):
        None

    def drawByWeek(self,data):
        data['xlabel']=data["phase_number"].map(str) +data["phase_subphase"]

<<<<<<< HEAD
        fig1 = px.bar(data, y="xlabel", x="distance",  color="trainingtype", title=f"Running ({datetime.date.today()})", orientation='h', text_auto='.2s')
        fig1.write_html('figure.html', auto_open=False)

    def drawByPhase(self,data):
        data['xlabel']=data["phase_number"].map(str)+":"+data["phase_startdate"].map(str)
        fig1 = px.bar(data, y="xlabel", x="distance",  color="trainingtype", title=f"Running ({datetime.date.today()})", orientation='h', text_auto='.2s')
=======
        fig1 = px.bar(data, y="xlabel", x="distance",  color="trainingtype", title="Runnining", orientation='h', text_auto='.2s')
        fig1.write_html('figure.html', auto_open=False)

    def drawByPhase(self,data):
        fig1 = px.bar(data, y="phase_number", x="distance",  color="trainingtype", title="Running", orientation='h', text_auto='.2s')
>>>>>>> 6a96c36e32215ef34d4da654bb5f9e5aea1df59d
        fig1.write_html('figure.html', auto_open=False)

    def drawByDate(self,data):
        data['xlabel']=data["phase_number"].map(str) +data["date"].map(str)
<<<<<<< HEAD
        fig1 = px.bar(data, y="date", x="distance",  color="trainingtype", title=f"Running ({datetime.date.today()})", orientation='h', textposition="outside",text_auto='.2s')
=======
        fig1 = px.bar(data, y="date", x="distance",  color="trainingtype", title="Running"+str(datetime.now()), orientation='h', text_auto='.2s')
>>>>>>> 6a96c36e32215ef34d4da654bb5f9e5aea1df59d
        fig1.write_html('figure.html', auto_open=False)

    def drawSummary(self,data):
        print(data.columns)
        fig1 = px.line(data, y=['distance','maxdist'], x="phase_number",  title=f"Running ({datetime.date.today()})")
        fig1.write_html('figure.html', auto_open=False)

if __name__ == "__main__":
    None