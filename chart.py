import plotly.express as px
from datetime import datetime

class plot():
    
    def __init__(self):
        None

    def drawByWeek(self,data):
        data['xlabel']=data["phase_number"].map(str) +data["phase_subphase"]

        fig1 = px.bar(data, y="xlabel", x="distance",  color="trainingtype", title="Runnining", orientation='h', text_auto='.2s')
        fig1.write_html('figure.html', auto_open=False)

    def drawByPhase(self,data):
        fig1 = px.bar(data, y="phase_number", x="distance",  color="trainingtype", title="Running", orientation='h', text_auto='.2s')
        fig1.write_html('figure.html', auto_open=False)

    def drawByDate(self,data):
        data['xlabel']=data["phase_number"].map(str) +data["date"].map(str)
        fig1 = px.bar(data, y="date", x="distance",  color="trainingtype", title="Running"+str(datetime.now()), orientation='h', text_auto='.2s')
        fig1.write_html('figure.html', auto_open=False)
        
if __name__ == "__main__":
    None