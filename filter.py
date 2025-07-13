import langdetect, json

f= open('out.json')
data = json.load(f)
f.close()

outdata = ''

for video in data["items"]:
    print(video)