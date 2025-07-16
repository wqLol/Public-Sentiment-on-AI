import json
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

comments = {"items": []}
for vid in videos:
    comments["items"] += getComments(youtube, vid)["items"]
with open('comments.json') as f:
    json.dump(comments, f)
