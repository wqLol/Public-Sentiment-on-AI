import langdetect, json

f= open('out.json')
data = json.load(f)
f.close()

outdata = { "items": [] }

for video in data["items"]:
    title = video["snippet"]["title"]
    description = video["snippet"]["description"]
    titlelang = langdetect.detect(title)
    descriptionlang = langdetect.detect(title)
    if titlelang == "en" or descriptionlang == "en": 
        outdata["items"].append(video)
    else:
        print(title, titlelang, descriptionlang)
        
with open("filtered.json", "w") as f:   
    json.dump(outdata, f, indent=4)