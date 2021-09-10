from os import name
from flask import Flask, request,jsonify,render_template
from plugin import sakura
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

@app.route('/sakura/api/card/array',methods=['GET'])
def get_list_card():
    if request.method=='GET':
        list_cards =  sakura.cardSakura.get_list_cards()
        return jsonify(list_cards)

@app.route('/sakura/api/card/all', methods=['GET','POST'])
def get_all_card():
    if request.method == 'GET':
        list_cards =  sakura.cardSakura.create_list_sakura()
        return jsonify(list_cards)
@app.route('/sakura/api/card/<name>',methods=['GET'])
def get_card(name):
    if request.method == 'GET': 
        card = sakura.cardSakura.get_info_cards(name)
        return jsonify(card)
@app.route("/",methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template("sakura.html")
    if request.method == "POST":
        nani = request.form['card']
        return nani