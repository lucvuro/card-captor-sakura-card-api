from os import name
from flask import Flask, request,jsonify
from plugin import sakura
app = Flask(__name__)
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