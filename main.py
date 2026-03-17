import news_scraper

if __name__ == '__main__':
    print('List of available sources: ')
    print('Enter the news source: ')
    news_source = input()
    print('Enter the date in yyyy-mm-dd format')
    date = input()

    news_scraper.get_news(news_source, date)
