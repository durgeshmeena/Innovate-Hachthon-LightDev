from flask import Flask, render_template, redirect, request
import requests
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
import json
from decouple import config
from user_data import get_user


app = Flask(__name__)
app.secret_key = config('APP_SECRET')

@app.route('/')
def index():
    return render_template('home.html')

@app.route( '/bot', methods=['POST']) 
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False



    if 'start' in incoming_msg:
        # msg.body("Loading data")
        data =  get_user(config('USER'), config('PASSWORD'))

        with open("data.json", "w") as database:
            json.dump(data, database)

        # print("data= ", data[1])
        resp.message("Details Found")
        return str(resp)
        # responded = True

    elif 'general' in incoming_msg:
        val = ""
        with open("data.json", "r") as database:
            json_object = json.load(database)
            val = json_object["2"]
        msg.body(val)
        responded = True

    elif 'balance' in incoming_msg:
        val = ""
        with open("data.json", "r") as database:
            json_object = json.load(database)
            val = json_object["2"]
        msg.body(val)
        responded = True

    elif 'user' in incoming_msg:
        val = ""
        with open("data.json", "r") as database:
            json_object = json.load(database)
            val = json_object["3"]
        msg.body(val)
        responded = True

    else:
        msg.body('Type *START* to get your details')     
        responded = True
    if not responded:
        msg.body('an Error occured! again Type *START* to start bot')       

    return str(resp)

if __name__ == "__main__":
    app.run(debug=False)
