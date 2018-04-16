from flask import Flask
from flask import render_template
from flask import request
from wtforms import Form, StringField, SelectField
from newsapi import newsapi_client
from news    import News
import json
global apikey
# precisely searching for particular news
apikey = newsapi_client.NewsApiClient(api_key='c6ad02b14a8e4089a9f0bbc6f44c2d6c')

def _json(stat):
    return json.dumps(stat)


class searchnews(Form):
    select = SelectField('Search...')
    search = StringField('')



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index_page():
    BBC = apikey.get_top_headlines(q='trump', sources='bbc-news,the-verge', language='en')
    BBC=BBC['articles'][0]
    FOX = apikey.get_top_headlines(q='trump', sources='Fox-news ', language='en')
    FOX=FOX['articles'][0]
    time=apikey.get_top_headlines(q='trump',sources='Time', language='en')
    time=time['articles'][0]
    CNN=apikey.get_top_headlines(q='trump', sources='CNN', language='en')
    CNN=CNN['articles'][0]
    return render_template('index.html',BBC=BBC,FOX=FOX,Time=time,CNN=CNN)

@app.route('/hotline',methods=['GET'])
def hotlines():
    BBC=apikey.get_top_headlines(q='trump',sources='bbc-news,the-verge',language='en')
    news=BBC['articles'][0]
    news=json.dumps(news)
    return news


#    return render_template('index.html',form=_topic)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
