from getVideos import getVideo
import datetime, dateutil, json
import googleapiclient.discovery
from apikey import key


startYear = 2018
startMonth = 1
ctime = datetime.datetime(startYear, startMonth, 1)

api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=key)

cf = open('out.json', 'r')
data = json.load(cf)
cf.close()
for year in range(2018,2026):
    for month in range(1, 13):
        if ctime > datetime.datetime.now(): 
            break
        ftime = ctime + dateutil.relativedelta.relativedelta(months=1)
        print(ctime)
        
        gdata = getVideo(youtube,'AI', ctime.isoformat() + 'Z', ftime.isoformat() + 'Z')
        data["items"] += gdata["items"]

        ctime = ftime
with open('out.json','w') as f:
    f.write(json.dumps(data))
# print(test)