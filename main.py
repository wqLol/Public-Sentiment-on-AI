from getVideos import getVideo
import datetime, dateutil, json




startYear = 2012
startMonth = 1
ctime = datetime.datetime(startYear, startMonth, 1)

# for year in range(2012,2014):
#     for month in range(1, 13):
#         cf = open('out.json', 'r')
#         data = json.load(cf)
#         cf.close()
#         ftime = ctime + dateutil.relativedelta.relativedelta(months=1)
#         print(ctime)
#         with open('out.json', 'w') as f:
#             gdata = getVideo('fortnite', ctime.isoformat() + 'Z', ftime.isoformat() + 'Z')
#             data |= gdata
#             f.write(json.dumps(data))
#         ctime = ftime

cf = open('out.json', 'r')
data = json.load(cf)
cf.close()
for year in range(2012,2013):
    for month in range(1, 13):
        ftime = ctime + dateutil.relativedelta.relativedelta(months=1)
        print(ctime)

        gdata = getVideo('', ctime.isoformat() + 'Z', ftime.isoformat() + 'Z')
        data["items"] += gdata["items"]

        ctime = ftime
with open('out.json','w') as f:
    f.write(json.dumps(data))
# print(test)