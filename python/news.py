import urllib
import datetime
import requests
import json
from flask import Flask
from newsapi import newsapi_client
global apikey
# precisely searching for particular news
class News:
    def Everything(self,_topic,_source,_domains,_from_parameter,_to,_language,_sort_by,_page):
        everything = apikey.get_everything(q=_topic,sources=_source,domains=_domains,from_parameter=_from_parameter,to=_to,language=_language,sort_by=_sort_by,page=_page)
        return everything

    def Hotlines(self,_topic,_source,_language):
        hotlines = apikey.get_top_headlines(q=_topic,sources=_source,language=_language)
        if hotlines['totalResults']!=0:
            return hotlines['articles'][0]
        else:
            return "nothing related is found"

    def Sources(self,_category,_language,_country):
        sources = apikey.get_sources(category=_category,language=_language,country=_country)
        return sources

apikey = newsapi_client.NewsApiClient(api_key='c6ad02b14a8e4089a9f0bbc6f44c2d6c')
request_news=News()
top_headlines = News.Hotlines(News,'trump','espn','en')
everything = apikey.get_everything(q='trump', sources='bbc-news', domains='bbc.co.uk,techcrunch.com', from_parameter='2017-05-04',
                                       to='2018-05-08', language='en', sort_by='relevancy', page=3)
print(top_headlines)
print(everything)
# interact with frontend
#  get the latest news to display (sports, movie,etc)







