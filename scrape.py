from newscatcherapi import NewsCatcherApiClient
import time
import json
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("api-key")
api_key = token

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
        # file_name = 'news_dataset/'+f'{query}' + '.json'
        file_name = f'{query}' + '.json'
        
        with open(file_name, 'a') as f:
            json.dump(arr, f)
        return len(arr)


def custom(query, pages, page_size):
    newscatcherapi = NewsCatcherApiClient(x_api_key=api_key)
    arr = []
    all_news_name = set()
    try:
        for page in range(1, pages+1):
            time.sleep(0.1)
            all_articles = newscatcherapi.get_search(
                q=query,
                lang='en',
                page=page,
                page_size=page_size,
            )

            for news in all_articles['articles']:
                if news['title'] not in all_news_name:
                    temp = {'title': news['title'], 'excerpt': news['excerpt'],
                            'summary': news['summary'], 'label': 'sport'}
                    arr.append(temp)
                    all_news_name.add(news['title'])
    except Exception as e:
        print('Insufficent data.')
        print(e)
    finally:
        file_name = 'environment' + '.json'

        print(len(arr))
        with open(file_name, 'w') as f:
            json.dump(arr, f)


## standard scraping

query = ['sport','tech', 'world', 'finance', 'politics', 'business', 'economics', 'entertainment', 'beauty', 'travel','food', 'science']


for q in query:
    total_val = scrap(query=q, pages=100, page_size=100,api_key=api_key)
    print(q,'is added to the database. Total number of values: ',total_val)
    time.sleep(10)


### custom scraping

temp_arr = ['agriculture', 'climate', 'global warming', 'pollution', 'weather', 'disaster', 'anthropology', 'green',
            'sustainability', 'climate change', 'environmental science', 'environmental engineering', 'air quality', 'wildlife']

val = ''
for temp in temp_arr:
    val += temp.lower() + ' OR ' + temp.capitalize() + \
        ' OR ' + temp.upper() + ' OR '

val = val[:-4]
# val = 'Sport OR Athlete OR Boxing OR Championship OR Cricket OR Basketball OR Baseball OR Football OR Soccer OR Badminton OR Gymnasium OR Gymnastics OR Goal OR Hockey OR Olympics OR Race OR Rafting OR Racing OR Rugby OR Referee OR Swimming OR Swimmer OR Tennis OR World Series OR Tennis OR Table Tennis OR World Cup'

custom(val, 100, 100)
