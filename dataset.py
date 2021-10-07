import pandas as pd
import json 

query = ['sport', 'tech', 'world', 'finance', 'politics', 'business',
         'economics', 'entertainment', 'travel', 'food', 'science', 'beauty']

df = pd.DataFrame()

for q in query:
    file_name = f'dataset/{q}.json'
    f = open(file_name)
    data = json.load(f)
    temp_df = pd.read_json(file_name)
    df = pd.concat([df,temp_df])
    f.close()

df = df.sample(frac=1)

# print(df.label.value_counts())

df.to_csv('dataset.csv',index=False)