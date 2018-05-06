from flask import Flask
from flask import render_template
from flask import request
from wtforms import Form, StringField, SelectField
from newsapi import newsapi_client
from news    import News
from werkzeug.security import generate_password_hash
import mysql.connector as db
import os
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
app._static_folder = os.path.abspath("static")

@app.route('/loginPage')
def showLogin():
    return(render_template('login.html'))

@app.route('/registerPage')
def showRegister():
    return(render_template('register.html'))

@app.route('/', methods=['GET', 'POST'])
def index_page():
    FOX = apikey.get_top_headlines(q='trump', sources='Fox-news ', language='en')
    FOX=FOX['articles'][0]
    time=apikey.get_top_headlines(q='trump',sources='Time', language='en')
    time=time['articles'][0]
    CNN=apikey.get_top_headlines(q='trump', sources='CNN', language='en')
    CNN=CNN['articles'][0]
    return render_template('index.html', FOX=FOX, Time=time, CNN=CNN)

@app.route('/hotline',methods=['GET'])
def hotlines():
    BBC=apikey.get_top_headlines(q='trump',sources='bbc-news,the-verge',language='en')
    news=BBC['articles'][0]
    news=json.dumps(news)
    return news

@app.route('/search', methods=['POST'])
def search():
    searchData = request.form
    print(searchData)
    # print(searchData)
    if not searchData.get('queryString'): ##Checks to see if a query was entered.
        return(render_template('emptySearch.html'))
    query = request.form['queryString']
    print(query)
    ### The following block indexes source collection
    selectedSources = []
    if searchData.get('WAPO'):
        selectedSources.append("the-washington-post")
    if searchData.get('BBC'):
        selectedSources.append("bbc-news")
    if searchData.get('ABC'):
        selectedSources.append("abc-news")
    if searchData.get('CBS'):
        selectedSources.append("cbs-news")
    if searchData.get('CNN'):
        selectedSources.append("cnn")
    if searchData.get('ESPN'):
        selectedSources.append("espn")
    if searchData.get('FOX'):
        selectedSources.append("fox-news")
    if searchData.get('NBC'):
        selectedSources.append("nbc-news")
    if searchData.get('NYT'):
        selectedSources.append("the-new-york-times")
    if searchData.get('WSJ'):
        selectedSources.append("the-wall-street-journal")
    if len(selectedSources) == 0: ## case where no sources selected
        newsItems = apikey.get_everything(q=str(query), language='en', sort_by='relevancy')
        articleListing = newsItems['articles']
        return(render_template('search.html', results=articleListing))
    else:
        sourcesStr = ""
        if len(selectedSources) > 1:
            x = len(selectedSources)
            finalIndex = x - 1
            for i in range(len(selectedSources)-1):
                sourcesStr = sourcesStr + selectedSources[i] + ","
            sourcesStr = sourcesStr + selectedSources[finalIndex]
            newsItems = apikey.get_everything(q=str(query), sources=str(sourcesStr), language='en', sort_by='relevancy')
            articleListing = newsItems['articles']
            return(render_template('search.html', results=articleListing)) ## Initially just testing to see what gets rendered on form submit atm:
        else:
            newsItems = apikey.get_everything(q=str(query), sources=str(selectedSources[0]), language='en', sort_by='relevancy')
            articleListing = newsItems['articles']
            return(render_template('search.html', results=articleListing))

#    return render_template('index.html',form=_topic)

@app.route('/connectionTest')
def testConnect():
    cnx = db.connect(user='groupmem', password='password', host='localhost', database='finalProj')
    if(cnx):
        print("connected??")
    cnx.close()
    return(render_template('emptySearch.html'))

@app.route('/register', methods=['POST'])
def register():
    print(request.form)
    return(render_template('emptySearch.html'))

@app.route('/login', methods=['POST'])
def handleLogin():
    print(request.form)
    return(render_template('emptySearch.html'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
