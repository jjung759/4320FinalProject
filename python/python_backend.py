from flask import Flask
from flask import render_template
from flask import request
from wtforms import Form, StringField, SelectField
from newsapi import newsapi_client
from news    import News
import datetime
import json
global apikey
# precisely searching for particular news
apikey = newsapi_client.NewsApiClient(api_key='c6ad02b14a8e4089a9f0bbc6f44c2d6c')

def _json(stat):
    return json.dumps(stat)

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

@app.route('/searching',methods=['POST', 'GET'])
def search():
    topic=request.args.get('contain',0,type=str)
    source='Time'
    begin=datetime.datetime.now()
    end=datetime.datetime(year=begin.year,month=begin.month,day=begin.day+4)
    if(source=='Time'):
        _domains = "http://www.bbc.co.uk/news"
        everything = apikey.get_everything(q=topic, sources=source, domains=_domains, from_parameter=begin.date(),
                                       to=end.date(), language='English', sort_by='relevancy', page=3)
    elif (source=='BBC'):
        _domains="http://www.bbc.co.uk/news"
        everything = apikey.get_everything(q=topic, sources=source, domains=_domains, from_parameter=begin.date(),
                                           to=end.date(), language='English', sort_by='relevancy', page=3)
    elif (source=='CNN'):
        _domains="http://us.cnn.com"
        everything = apikey.get_everything(q=topic, sources=source, domains=_domains, from_parameter=begin.date(),
                                           to=end.date(), language='English', sort_by='relevancy', page=3)
    else :
        _domains="http://www.foxnews.com"
        everything = apikey.get_everything(q=topic, sources=source, domains=_domains, from_parameter=begin.date(),
                                           to=end.date(), language='English', sort_by='relevancy', page=3)

    return render_template('index1.html.html')


#    return render_template('index.html',form=_topic)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
