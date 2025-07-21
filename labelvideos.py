import json

f= open('comments.json')
data = json.load(f)
f.close()


data = data["data"]
