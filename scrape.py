from newscatcherapi import NewsCatcherApiClient
import time
import json


def scrap(query, pages, page_size,api_key):
    newscatcherapi = NewsCatcherApiClient(x_api_key=api_key)
    arr = []
    all_news_name=set()
    try:
        for page in range(1, pages+1):
            time.sleep(0.5)
            all_articles = newscatcherapi.get_latest_headlines(
                topic=query,
                lang='en',
                page=page,
                page_size=page_size,
                )

            for news in all_articles['articles']:
                if news['title'] not in all_news_name: 
                    temp = {'title': news['title'], 'excerpt': news['excerpt'],
                        'summary': news['summary'], 'label': query}
                    arr.append(temp)
                    all_news_name.add(news['title'])
    except:
        print('Insufficent data.')
    finally:
        file_name = 'news_dataset/'+f'{query}' + '.json'
        
        with open(file_name, 'a') as f:
            json.dump(arr, f)
        return len(arr)


query = ['sport','tech', 'world', 'finance', 'politics', 'business', 'economics', 'entertainment', 'beauty', 'travel','food', 'science']
api_key = 'aNWN1kWureFPONyGke7q3dLhK1fVq-GCFDuoh0zeXW4'

for q in query:
    total_val = scrap(query=q, pages=100, page_size=100,api_key=api_key)
    print(q,'is added to the database. Total number of values: ',total_val)
    time.sleep(10)
