import urllib.request
import json
from .models import Article, Source

# Getting api key
api_key = None
# Getting the news base url
base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = f'{base_url}sources?apiKey={api_key}'

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None

        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_results(news_sources_list)

    return news_sources


def process_results(source_list):
    '''
    Function  that processes the news sources and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        news_sources: A list of source objects
    '''
    news_sources = []
    for source in source_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        country = source.get('country')
        new_source = Source(id, name, description, url, country)
        news_sources.append(new_source)

    return news_sources


def get_article(id):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url = f'{base_url}everything?q=Apple&from=2022-01-31&sortBy=popularity&apiKey={api_key}'

    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        news_articles = None

        if get_article_response['articles']:
            news_article_list = get_article_response['articles']
            news_articles = process_articles(news_article_list)

    return news_articles


def process_articles(article_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        news_articles: A list of article objects
    '''
    news_articles = []
    for article in article_list:
        id = article.get('source').get('id')
        title = article.get('title')
        image = article.get('urlToImage')
        description = article.get('description')
        url = article.get('url')
        author = article.get('author')
        publishedAt = article.get('publishedAt')
        new_artical = Article(id, title, image, description,
                              url, author, publishedAt)
        news_articles.append(new_artical)
    print(news_articles)
    return news_articles
