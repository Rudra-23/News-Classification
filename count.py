
import json

query = ['sport', 'tech', 'world', 'finance', 'politics', 'business',
         'economics', 'entertainment', 'travel', 'food', 'science','beauty']


for q in query:
    f = open(f'dataset/{q}.json')
    data = json.load(f)
    print(f'{q} :',len(data))
    f.close()
