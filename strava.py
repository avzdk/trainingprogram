import requests
import urllib3
import logging
import configparser
import os
ENVIRONMENT = os.environ.get("ENV", "local")
print(f"env:{ENVIRONMENT}")
conf = configparser.ConfigParser()
if ENVIRONMENT == "local":
    cf = conf.read("config_local.ini")
else:
    cf = conf.read("config.ini")

log = logging.getLogger(__name__)
logging.basicConfig(
    level=conf.get("LOG", "LEVEL", fallback="DEBUG"),
    format="%(levelname)s %(module)s.%(funcName)s %(message)s",
)
log.info(
    f"Starting service loglevel={conf['LOG']['LEVEL']} @ {ENVIRONMENT} environemnt "
)
log.info(f"WorkingDirectory: {os.getcwd()}")
log.info(f"Configurationfiles: {cf}")

CLIENT_ID=conf['STRAVA']['client_id']
CLIENT_SECRET=conf['STRAVA']['client_secret']
REFRESH_TOKEN=conf['STRAVA']['refresh_token']
#https://github.com/franchyze923/Code_From_Tutorials/blob/master/Strava_Api/strava_api.py
#https://towardsdatascience.com/using-the-strava-api-and-pandas-to-explore-your-activity-data-d94901d9bfde


class Strava():
    def __init__(self):
        self.auth_url = "https://www.strava.com/oauth/token"
        self.activites_url = "https://www.strava.com/api/v3/athlete/activities"
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    def getToken(self):
        payload = {
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'refresh_token': REFRESH_TOKEN,
            'grant_type': "refresh_token",
            'f': 'json'
        }
        res = requests.post(self.auth_url, data=payload, verify=False)
        self.access_token = res.json()['access_token']
        

    def getActivities(self,pagesize=200,page=1):
        header = {'Authorization': 'Bearer ' + self.access_token}
        param = {'per_page': pagesize, 'page': page}
        activities = requests.get(self.activites_url, headers=header, params=param).json()
        return activities
        





if __name__ == "__main__":
    client=Strava()
    client.getToken()
    activities = client.getActivities(10)
    for a in activities:
        print(a['name'])












