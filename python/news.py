import urllib
import datetime
import requests
from flask import Flask
from newsapi import newsapi_client
global apikey
# precisely searching for particular news
class News:
    def Everything(self,_topic,_source,_domains,_from_parameter,_to,_language,_sort_by,_page):
        everything = apikey.get_everything(q=_topic,sources=_source,domains=_domains,from_parameter=_from_parameter,to=_to,language=_language,sort_by=_sort_by,page=_page)
        return everything

    def Hotlines(self,_topic,_source,_category,_language,_country):
        hotlines = apikey.get_top_headlines(q=_topic,sources=_source,category=_category,language=_language,country=_country)
        return hotlines

    def Sources(self,_category,_language,_country):
        sources = apikey.get_sources(category=_category,language=_language,country=_country)
        return sources

    def keyword(self,input):
        key=

        return

apikey = newsapi_client.NewsApiClient(api_key='c6ad02b14a8e4089a9f0bbc6f44c2d6c')
request_news=News()
top_headlines = apikey.get_top_headlines(q='trump',sources='CNN',language='en')

print(top_headlines['articles'][0])
print(type(top_headlines['articles'][0]))
# interact with frontend
#  get the latest news to display (sports, movie,etc)







