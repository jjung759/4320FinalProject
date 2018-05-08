from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect, url_for
from wtforms import Form, StringField, SelectField
from newsapi import newsapi_client
from news    import News
from datetime import datetime
import re
from werkzeug.security import generate_password_hash,  check_password_hash
import mysql.connector as db
import os
import json
global apikey
import hashlib
# precisely searching for particular news
apikey = newsapi_client.NewsApiClient(api_key='c6ad02b14a8e4089a9f0bbc6f44c2d6c')

def _json(stat):
    return json.dumps(stat)


class searchnews(Form):
    select = SelectField('Search...')
    search = StringField('')



app = Flask(__name__)
app._static_folder = os.path.abspath("static")
app.secret_key = "RZ23UL2KwY69"



class favoriteItem():
    def __init__(self, newsSource, userID, favoriteDate, author, descriptions, url, imageURL, title):
        self.newsSource = newsSource
        self.userID = userID
        self.favoriteDate = favoriteDate
        self.author = author
        self.descriptions = descriptions
        self.url = url
        self.imageURL = imageURL
        self.title = title

@app.route('/favorites', methods=['GET', 'POST'])
def favorite():
    if 'username' in session:
        cnx = db.connect(user='groupmem', password='password', host='localhost', database='finalProj')
        cursor = cnx.cursor()
        # empty array of favorites to populate with the query
        favorites = []
        queryUser = ("SELECT * FROM newsUsers WHERE username="+ "'"+session['username']+"'")
        cursor.execute(queryUser)
        for (userID) in cursor:
            uid =  userID
        print(uid)
        print(uid[0])
        query = ("SELECT * FROM favorites WHERE userID =" + "'"+str(uid[0])+"'")
        cursor.execute(query)
        for (newsSource, userID, favoriteDate, author, descriptions, url, imageURL, title) in cursor:
            favorites.append(favoriteItem(newsSource, userID, favoriteDate, author, descriptions, url, imageURL, title))
        cursor.close()
        cnx.close()
        return render_template('favorites.html', results=favorites)
    else:
        return redirect(url_for('showLogin'))

@app.route('/unfavorite', methods=['GET', 'POST'])
def unfavorite():
    #User login error checking
    if 'username' in session:
        #Database connection
        ##Should modify this so that deletion is based off of title//userID
        url = request.form['url']
        ## Get UserID
        username = session['username']
        queryUserID = ("SELECT id FROM newsUsers WHERE username="+ "'"+username+"'")
        cnx = db.connect(user='groupmem', password='password', host='localhost', database='finalProj')
        cursor = cnx.cursor()
        cursor.execute(queryUserID)
        idT = 0
        for (id) in cursor:
            idT = id
        uid = idT[0] #userID to insert into table
        query = "DELETE FROM favorites WHERE userID=" + str(uid) + " AND url='" + str(url) + "'"
        print(query)
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
        return render_template('favorites.html')

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
    if 'username' in session:
        print(session['username'])
        print("Session appears to be activated")
        return render_template('indexLoggedIn.html', FOX=FOX,Time=time,CNN=CNN)
    else:
        print("Session Inactive")
        return render_template('index.html', FOX=FOX, Time=time, CNN=CNN)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
        return redirect(url_for('index_page'))
    else:
        return redirect(url_for('index_page'))


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
        if 'username' in session:
            return(render_template('searchLoggedIn.html', results=articleListing))
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
            if 'username' in session:
                return(render_template('searchLoggedIn.html', results=articleListing))
            return(render_template('search.html', results=articleListing)) ## Initially just testing to see what gets rendered on form submit atm:
        else:
            newsItems = apikey.get_everything(q=str(query), sources=str(selectedSources[0]), language='en', sort_by='relevancy')
            articleListing = newsItems['articles']
            if 'username' in session:
                return(render_template('searchLoggedIn.html', results=articleListing))
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
    ## essentially, the hashed form of our password is being realll unreliable,
    ## So, I'm gonna go ahead and change the methods for hashing to something dumber.
    print(request.form)
    regData = request.form
    username = regData['username']
    passwordInit = regData['password']
    # passwordHashed = generate_password_hash(passwordInit)
    h = hashlib.md5(passwordInit.encode())
    passwordHashed = h.hexdigest()
    add_user = ("INSERT INTO newsUsers " "(username, passwordHashed) " "VALUES (" + "'" +str(username)+"','" + str(passwordHashed)+"')")
    print(add_user)
    data_user = (str(username), str(passwordHashed))
    cnx = db.connect(user='groupmem', password='password', host='localhost', database='finalProj')
    cursor = cnx.cursor()
    cursor.execute(add_user)
    cnx.commit()
    cursor.close()
    cnx.close()
    return(render_template('login.html'))

@app.route('/login', methods=['POST'])
def handleLogin():
    print("What the fuck");
    print(request.form)
    loginData = request.form
    username = loginData['username']
    passwordInit = loginData['password']
    queryUser = ("SELECT * FROM newsUsers WHERE username="+ "'"+username+"'")
    print(queryUser)
    cnx = db.connect(user='groupmem', password='password', host='localhost', database='finalProj')
    cursor = cnx.cursor()
    cursor.execute(queryUser)
    hashTest = ""
    for (passwordHashed) in cursor:
        hashTest = passwordHashed
    print(hashTest[2])
    h = hashlib.md5(passwordInit.encode())
    hashedPUser = h.hexdigest()
    print(str(hashedPUser))
    print(hashTest)
    print(str(hashTest[2]))
    if (hashedPUser == str(hashTest[2])):
        session['username'] = loginData['username']
        print("fuck")
        return redirect(url_for('index_page'))
    else:
        print("guess it didn't work!")
        return redirect(url_for('showLogin'))
    return(render_template('emptySearch.html'))

@app.route('/addFavorite', methods=['POST'])
def addFavorite():
    ## to do --> Parse post request of article info, get UsersID, make sql query inserting article info & userID
    favoritedInfo = request.form
    print(favoritedInfo)
    title = favoritedInfo['title']
    author = favoritedInfo['author']
    source = favoritedInfo['newsSource']
    descrip = favoritedInfo['description']
    favDate = favoritedInfo['favoriteDate']
    imgUrl = favoritedInfo['imageURL']
    url = favoritedInfo['url']
    username = session['username']
    # descrip = re.escape(descrip)
    queryUserID = ("SELECT id FROM newsUsers WHERE username="+ "'"+username+"'")
    cnx = db.connect(user='groupmem', password='password', host='localhost', database='finalProj')
    cursor = cnx.cursor()
    cursor.execute(queryUserID)
    idT = 0
    for (id) in cursor:
        idT = id
    uid = idT[0] #userID to insert into table
    add_fav = ("INSERT INTO favorites " "(newsSource, userID, favoriteDate, author, descriptions, url, imageURL, title) " "VALUES ("
    + "'" +str(source)+"'," + str(uid) + ",NOW()"+ ",'" + str(author) + "','" + descrip + "','" + url + "','" + imgUrl + "','" + title +"')")
    print(add_fav);
    cursor.execute(add_fav)
    cnx.commit()
    cursor.close()
    cnx.close()
    return str(favoritedInfo)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
