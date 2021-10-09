from flask import Flask, render_template, redirect, request
import requests
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse


app = Flask(__name__)
app.secret_key = 'dev'

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
