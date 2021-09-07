from os import name
from flask import Flask, request,jsonify
import requests
import botchat
import func
from dotenv import load_dotenv
from plugin import sakura
load_dotenv()
app = Flask(__name__)

# FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
# VERIFY_TOKEN = 'lucvu123'# <paste your verify token here>
# PAGE_ACCESS_TOKEN = 'EAACJhdA6p1cBAMpHo3ZCQCZAFI0mZByzITRffltbgQXZA1BWE0QTTyvSbZC7BpMSVeXQ6CifgD8Ug9xK2q7UQLJBBBIObVAQsYd0LMZAtu5pGHvwBs5aBCR5sZA7mRNocC40zZCjBZCoW03IfCxNPSAoihVjZAKjeBDs9QLn98cmHdliZBG5ZB19e0Pt'# paste your page access token here>"

def verify_webhook(req):
    if req.args.get("hub.verify_token") == botchat.VERIFY_TOKEN:
        return req.args.get("hub.challenge")
    else:
        return "incorrect"



# def is_user_message(message):
#     """Check if the message is a message from the user"""
#     return (message.get('message') and
#             message['message'].get('text') or
#             message['message'].get('attachments') and
#             not message['message'].get("is_echo"))
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
@app.route('/hello/')
def hello():
    return 'Hello, World!'
@app.route("/webhook",methods=['GET', 'POST'])

# def listen():
#     """This is the main function flask uses to 
#     listen at the `/webhook` endpoint"""
#     if request.method == 'GET':
#         return verify_webhook(request)

#     if request.method == 'POST':
#         payload = request.json
#         event = payload['entry'][0]['messaging']
#         for x in event:
#             if is_user_message(x):
#                 # text = x['message']['text']
#                 print(x)
#                 sender_id = x['sender']['id']
#                 # func.doCmd(sender_id,text)
#         return "ok"

def listen():
    """This is the main function flask uses to 
    listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        return verify_webhook(request)

    if request.method == 'POST':
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if x.get("message"):
                sender_id = x['sender']['id']
                if x['message'].get("text"):
                    text = x['message']['text']
                    func.doCmd_text(sender_id,text)
                if x['message'].get("attachments"):
                    # print(x)
                    # print(x['message']['attachments'][0]['payload']['url'])
                    image_link = x['message']['attachments'][0]['payload']['url']
                    func.doCmd_attachments(sender_id,image_link)
                    # botchat.upload_image(sender_id,image_link)
        return "ok"