import time
import json
from newscatcherapi import NewsCatcherApiClient
import newscatcherapi

api_key = 'aNWN1kWureFPONyGke7q3dLhK1fVq-GCFDuoh0zeXW4'


def scrap(query, pages, page_size):
    newscatcherapi = NewsCatcherApiClient(x_api_key=api_key)
    arr = []
    for page in range(1, pages+1):
        time.sleep(1)
        all_articles = newscatcherapi.get_latest_headlines(
            topic=query,
            lang='en',
            page=page,
            countries=['US', 'IND', 'UK'],
            page_size=page_size)
        for news in all_articles['articles']:
            temp = {'title': news['title'], 'excerpt': news['excerpt'],
                    'summary': news['summary'], 'label': query}
            arr.append(temp)

    file_name = 'dataset/'+f'{query}' + '.json'

    with open(file_name, 'a') as f:
        json.dump(arr, f)


# query = ['sport', 'tech', 'world', 'finance', 'politics', 'business', 'economics', 'entertainment', 'beauty', 'travel','food', 'science']
# for q in query:
#     scrap(query=q, page=40, page_size=100)

scrap('beauty',35,100)
