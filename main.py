import requests as rq
import json
from apikey import key
# get videos first
url = r'https://www.googleapis.com/youtube/v3/search'
params = {
    "part": "snippet",
    "q": "test",
    "type": "video",
    "maxResults": 5,
    "order": "date",
    "key": key
}

req = rq.get(url,params=params)
print(req.url)
with open('test.txt', 'w') as f:
    f.write(str(req.content))
