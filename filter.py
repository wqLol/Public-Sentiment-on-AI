import langdetect, json

f= open('out.json')
data = json.load(f)
f.close()

outdata = { "items": [] }

for video in data["items"]:
    try:
        title = video["snippet"]["title"]
        description = video["snippet"]["description"]
        titlelang =  "na" if not title else  langdetect.detect(title) 
        descriptionlang = "na" if not description else langdetect.detect(description) 
        if titlelang == "en" or descriptionlang == "en": 
            outdata["items"].append(video)
        else:
            print(title, titlelang, descriptionlang)
    except langdetect.lang_detect_exception.LangDetectException as e:
        print(e)
        
with open("filtered.json", "w") as f:   
    json.dump(outdata, f, indent=4)