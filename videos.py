from getData import getVideo
import datetime, dateutil, json
import googleapiclient.discovery
from apikey import key
from sys import quit


startYear = 2018
startMonth = 1
ctime = datetime.datetime(startYear, startMonth, 1)

api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=key)


data = {"data": []}
search = "future of artificial intelligence"


for year in range(2018,2026):
    for month in range(1, 13):
        if ctime > datetime.datetime.now(): 
            break
        ftime = ctime + dateutil.relativedelta.relativedelta(months=1)
        print(ctime)
        try:
            gdata = getVideo(youtube,search, ctime.isoformat() + 'Z', ftime.isoformat() + 'Z')
        except Exception as e:
            print(e)
            with open('out.json','w') as f:
                f.write(json.dumps(data))
                quit()
                
                
        data["items"] += gdata["items"]

        ctime = ftime
with open('out.json','w') as f:
    f.write(json.dumps(data))
# print(test)