import plotly.express as px

class plot():
    
    def __init__(self):
        None

    def draw(self,data):


        fig = px.bar(data, y="isoYW", x="distance", color="type", title="Running", orientation='h')
        fig.write_html('figure.html', auto_open=True)


if __name__ == "__main__":
    import datetime

    testdata=[{'date': datetime.date(2021, 1, 4), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 5), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 6), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 11), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 12), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 13), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 18), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 19), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 20), 'distance': 5.0, 'time': 25.5, 'type': '-', 'done': True}, {'date': datetime.date(2021, 1, 30), 'distance': 6, 'time': 25, 'type': 'Long', 'done': False}, {'date': datetime.date(2021, 1, 28), 'distance': 5, 'time': 25, 'type': 'Short', 'done': False}, {'date': datetime.date(2021, 1, 26), 'distance': 7, 'time': 25, 'type': 'Medium', 'done': False}, {'date': datetime.date(2021, 2, 11), 'distance': 8, 'time': 25, 'type': 'Long', 'done': False}, {'date': datetime.date(2021, 2, 9), 'distance': 5, 'time': 25, 'type': 'Short', 'done': False}, {'date': datetime.date(2021, 2, 7), 'distance': 6, 'time': 25, 'type': 'Medium', 'done': False}, {'date': datetime.date(2021, 2, 23), 'distance': 9, 'time': 25, 'type': 'Long', 'done': False}, {'date': datetime.date(2021, 2, 21), 'distance': 6, 'time': 25, 'type': 'Short', 'done': False}, {'date': datetime.date(2021, 2, 19), 'distance': 6, 'time': 25, 'type': 'Medium', 'done': False}, {'date': datetime.date(2021, 3, 7), 'distance': 10, 'time': 25, 'type': 'Long', 'done': False}, {'date': datetime.date(2021, 3, 5), 'distance': 7, 'time': 25, 'type': 'Short', 'done': False}, {'date': datetime.date(2021, 3, 3), 'distance': 6, 'time': 25, 'type': 'Medium', 'done': False}, {'date': datetime.date(2021, 3, 19), 'distance': 11, 'time': 25, 'type': 'Long', 'done': False}, {'date': datetime.date(2021, 3, 17), 'distance': 7, 'time': 25, 'type': 'Short', 'done': False}, {'date': datetime.date(2021, 3, 15), 'distance': 7, 'time': 25, 'type': 'Medium', 'done': False}]

    p=plot()
    p.draw(data=testdata)