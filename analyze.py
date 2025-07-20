from transformers import pipeline
import json, torch
 
print(torch.cuda.is_available())

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device = 0)

f = open('comments.json')
data = json.load(f)
f.close()
total = 0

comments = []
for vid in data["data"]:
    for commentResource in vid["items"]:
        comment = commentResource["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
        if comment: 
            comments.append(comment)
        

results = classifier(comments, truncation=True)


for val in results:
    total += val["score"] if val["label"] == "POSITIVE" else -1 * val["score"]

print("\n" + str(total/len(results)))