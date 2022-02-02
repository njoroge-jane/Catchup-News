from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_article, get_news

@main.route('/')
def index():
    news_sources= get_news()
    print(news_sources)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, news_sources = news_sources )

@main.route('/article/<string:id>')
def article(id):
    news_articles= get_article(id)
    return render_template('article.html', news_articles = news_articles)    