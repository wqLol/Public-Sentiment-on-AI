from getVideos import getVideo
import datetime, json



json.loads('{}')

for year in range(2015,2016):
    for month in range(1, 3):
        cf = open('out.json', 'r')
        data = json.load(cf)
        cf.close()
        with open('out.json', 'w') as f:

            startDate = datetime.datetime(year, month, 1).isoformat() + 'Z'
            endDate = datetime.datetime(year, month, 1).isoformat() + 'Z'

            gdata = getVideo('fortnite', startDate, endDate)
            data |= gdata
            f.write(json.dumps(data))
# print(test)