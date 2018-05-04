from flask import Flask
from flask import render_template
from flask import request,redirect
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


class search_item(Form):
    keyword=StringField('searchBar')


@app.route('/test', methods=['GET', 'POST'])
def a():


    return redirect('login')

@app.route('/login', methods=['GET', 'POST'])
def test():

    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index_page():
    #form=search_item()
    #t=form.keyword.data
    #print(t,"hellp")
    ABC = News.Hotlines(News,'trump','abc-news','en')
   # ABC = ABC['articles'][0]
    BBC =  News.Hotlines(News,'trump','bbc-news,the-verge','en')
    #BBC=BBC['articles'][0]
    CBS =  News.Hotlines(News,'trump', 'cbs-news', 'en')
    #CBS = CBS['articles'][0]
    CNN= News.Hotlines(News,'trump', 'CNN', 'en')
    #CNN=CNN['articles'][0]
    ESPN = News.Hotlines(News,'trump', 'espn', 'en')
    #ESPN = ESPN['articles'][0]
    FOX =  News.Hotlines(News,'trump', 'fox-news', 'en')
    #FOX=  FOX['articles'][0]
    NBC = News.Hotlines(News,'trump', 'nbc-news', 'en')
    #NBC = NBC['articles'][0]
    NYM = News.Hotlines(News,'trump', 'new-york-magazine', 'en')
    #NYM = NYM['articles'][0]
    WSJ = News.Hotlines(News,'trump', 'the-wall-street-journal','en')
    #WSJ = WSJ['articles'][0]
    TIME= News.Hotlines(News,'trump','Time','en')
    #TIME=TIME['articles'][0]
    return render_template('index.html',ABC=ABC,BBC=BBC,CBS=CBS,CNN=CNN,ESPN=ESPN,FOX=FOX,NBC=NBC,NYM=NYM,WSJ=WSJ,TIME=TIME)

@app.route('/searching',methods=['POST', 'GET'])
def search():
    topic=request.args.get('contain',0,type=str)
    print(topic)
    source='BBC'
    begin=datetime.datetime.now()
    end=datetime.datetime(year=begin.year,month=begin.month,day=begin.day+4)
    begin=datetime.datetime(year=begin.year-1,month=begin.month,day=begin.day)
    if(source=='Time'):
        default_topic='Trump'
        topic=default_topic
        _domains = "http://www.time.com"
        print(begin.date(),end.date(),topic,source,_domains)
        everything = apikey.get_everything(q=topic, sources=source, domains=_domains, from_parameter=begin.date(),
                                       to=end.date(), language='English', sort_by='relevancy', page=3)
    elif (source=='BBC'):
        default_topic = 'Trump'
        topic = default_topic
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
    print(everything)
    return render_template('searching.html',NEWS=everything)
#    return render_template('index.html',form=_topic)


if __name__ == '__main__':
    app.run()
