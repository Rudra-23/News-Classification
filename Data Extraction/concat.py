import pandas as pd
import json
import random

json1 = []
json2 = []

with open('environment.json','r') as f1:
    json1 = json.load(f1)

with open('news_dataset/environment.json','r') as f2:
    json2 = json.load(f2)


s = set()
for val in json1:
    s.add(val['title'])

for val in json2:
    if val['title'] not in s:
        json1.append({'title':val['title'],'excerpt':val['excerpt'],'summary':val['summary'],'label':'environment'})


random.shuffle(json1)

json_object = json.dumps(json1[:9000])
with open('environment.json','w') as f:
    f.write(json_object)

with open('environment.json', 'r') as f:
    data = json.load(f)
    print(len(data))
