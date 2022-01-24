import plotly.express as px

class plot():
    
    def __init__(self):
        None

    def draw(self,data):


        fig = px.bar(data, y="phase_number", x="distance", color="phase_status", title="Running", orientation='h')
        fig.write_html('figure.html', auto_open=True)


if __name__ == "__main__":
    None