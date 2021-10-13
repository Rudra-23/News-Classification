
import json
import glob


json_files = []
for file in glob.glob("news_dataset/*.json"):
    json_files.append(file)
query = json_files

for q in query:
    f = open(f'{q}')
    data = json.load(f)
    file_name = q.split('\\')[1]
    file_name = file_name.split('.')[0]
    print(file_name+' :',len(data))
    f.close()
