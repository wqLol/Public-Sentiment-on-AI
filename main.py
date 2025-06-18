from getVideos import getVideo
import datetime

startDate = datetime.datetime(2020, 5, 1)
endDate = datetime.datetime(2020, 6, 1)
test = getVideo('test', startDate, endDate)

print(test)