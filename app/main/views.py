from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news

@main.route('/')
def index():
    news_sources= get_news()
    print(news_sources)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, news_sources = news_sources )