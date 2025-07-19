import json

import googleapiclient.http
from getData import getComments

import googleapiclient.discovery
from apikey import key

api_service_name = "youtube"
api_version = "v3"

youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=key)

f = open('filtered.json')
data = json.load(f)
f.close()

videos = []

print(data["items"][0])


for vid in data["items"]:
   videos.append(vid["id"]["videoId"])

comments = {"data": []}


x = 1
progressBarMax = len(videos)
for vid in videos:
    try:
        comments["data"].append(getComments(youtube, vid))
    except googleapiclient.http.HttpError as e:
        print(e)
    
    print(f"{x}/{progressBarMax}")
    x += 1
       
       
with open('comments.json', 'w') as f:
    json.dump(comments, f)