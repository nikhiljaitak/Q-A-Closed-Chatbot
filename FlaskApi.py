from flask import Flask
app = Flask(__name__)
import json
from flask_cors import CORS
from flask_cors import cross_origin
import sys
sys.path.append('C:/Users/Nikhil/Downloads/Machine_Learning/Chatbot/Greenway_FAQ -Nikhil - _Version1_/Greenway_FAQ -Nikhil - _Version1_')
import Greenway_FAQbot_version_2 as FAQBot
#from flask.ext.cors import CORS, cross_origin
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])


@app.route('/get')  
def hello():
    return "Hello World!"

@app.route('/getResponse')
def get():
    #FAQBot.chat('hi')
    return FAQBot.chat('q')

if __name__ == '__main__':
    app.run()