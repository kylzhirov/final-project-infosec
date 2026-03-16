import configparser
import requests

# Load API key from cfg ini
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['newsapi']['api_key']

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2026-01-25&'
       'sortBy=popularity&'
       f'apiKey={api_key}')


response = requests.get(url)

result = response.json()

print(result)
