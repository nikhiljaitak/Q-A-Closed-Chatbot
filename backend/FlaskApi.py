from flask import Flask,request
app = Flask(__name__)
import json
from flask_cors import CORS
from flask_cors import cross_origin
import sys
#sys.path.append('C:/Users/nikhilj/Downloads/FAQChatBot_Ver1/FAQChatBot')
#sys.path.append('C:/Users/Nikhil/Downloads/Machine_Learning/Chatbot/Greenway_FAQ -Nikhil - _Version1_/Greenway_FAQ -Nikhil - _Version1_/version3')
sys.path.append('C:/Users/nikhilj/Downloads/RPA_ML/ML/Emids-Chatbot/ChatBot_Backend/backend')
#C:\Users\Administrator\Downloads\Greenway_FAQ-Nikhil_Version2\Greenway_FAQ -Nikhil - _Version1_\version3
import chat_FAQ as FAQBot
#from flask.ext.cors import CORS, cross_origin
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app)
@cross_origin(origin='localhost:5000',headers=['Content- Type','Authorization'])


@app.route('/get')  
def hello():
    return "Hello World!"

@app.route('/getResponse')
def get():
    data = {}
    #FAQBot.chat(str(request.args.get('query')))
    #json_data = json.dumps(data)
    data['response'] = FAQBot.chat(request.args.get('query'))
    return json.dumps(data)

@app.route('/saveTraining')  
def save():
    medicalDataset = pd.read_csv('file:///C:/Users/Administrator/Downloads/Greenway_FAQ-Nikhil_Version2/FAQChatBot/FAQDataset_Greenway.csv', encoding='ISO-8859–1')
    d = json.loads(j)
    return d['hi']

if __name__ == '__main__':
    app.run()