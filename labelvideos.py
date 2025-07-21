import json

f= open('comments.json')
data = json.load(f)
f.close()


for x in range(len(data["data"])):
    print(data["data"][x][0])
    
    
    
    

f = open('comments.json', 'w')
json.dump(data, f)
f.close()