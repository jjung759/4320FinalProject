from flask import Flask
from flask import render_template
from flask import request
from wtforms import Form, StringField, SelectField
from newsapi import newsapi_client
from news    import News
global apikey
# precisely searching for particular news
apikey = newsapi_client.NewsApiClient(api_key='c6ad02b14a8e4089a9f0bbc6f44c2d6c')

class searchnews(Form):
    select = SelectField('Search...')
    search = StringField('')



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index_page():
    _topic=searchnews(request.form)
    return render_template('index.html')
#    return render_template('index.html',form=_topic)


if __name__ == '__main__':
    app.run()
