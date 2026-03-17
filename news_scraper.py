import configparser
import requests

# Load API key from cfg ini
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['newsapi']['api_key']

news_source = ' '
date = '2026-03-15'

def get_news(news_source, date):
    url = ('https://newsapi.org/v2/everything?'
        f'q={news_source}&'
        f'from={date}&'
        'sortBy=popularity&'
        f'apiKey={api_key}')

    response = requests.get(url)
    result = response.json()
    print(result)
