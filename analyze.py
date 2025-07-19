# from transformers import pipeline
import json, torch

print(torch.cuda.is_available())
# classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device = 0)

# f = open('comments.json')
# data = json.load(f)
# f.close()
# x = 1
# total = 0
# for vid in data["data"]:
#     for commentResource in vid["items"]:
#         comment = commentResource["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
#         if not comment: continue
#         try:
#             val = classifier(comment[:512])[0]
#         except RuntimeError as e:
#             print(e)
#             continue
#         total += val["score"] if val["label"] == "POSITIVE" else -1 * val["score"]
        
#         print(comment[:512] + ' ' + str(val))
#         x += 1
        
        
# print("\n" + total/x)

