import glob
import pandas as pd
import json

json_files = []
for file in glob.glob('./news_dataset/*.json'):
    json_files.append(file)

df = pd.DataFrame()

print(json_files)

for file in json_files:
    f = open(file)
    data = json.load(f)
    temp_df = pd.read_json(file)
    df = pd.concat([df, temp_df])
    f.close()

df = df.sample(frac=1)

df.to_csv('news_dataset.csv',index=False)
