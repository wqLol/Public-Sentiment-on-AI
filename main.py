from getVideos import getVideo
import datetime, dateutil, json




startYear = 2012
startMonth = 1
ctime = datetime.datetime(startYear, startMonth, 1)

for year in range(2012,2014):
    for month in range(1, 13):
        cf = open('out.json', 'r')
        data = json.load(cf)
        cf.close()
        ftime = ctime + dateutil.relativedelta.relativedelta(months=1)
        print(ctime.now())
        with open('out.json', 'w') as f:
            gdata = getVideo('fortnite', ctime.isoformat() + 'Z', ftime.isoformat() + 'Z')
            data |= gdata
            f.write(json.dumps(data))
        ctime = ftime
# print(test)