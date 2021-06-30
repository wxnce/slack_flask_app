import requests
from flask import Flask, request, make_response, Response, jsonify
import os
import json
import threading

SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]


# Flask web server for incoming traffic from Slack

app = Flask(__name__)

def send_message(message,response_url):
    requests.post(response_url, json={'text' :'---------- You entered: ' + message + '----------'})

@app.route('/slash', methods=['POST'])
def slash():
   # if request.form['token'] == SLACK_VERIFICATION_TOKEN:
    payload = request.form.get('payload')
    payload = json.loads(payload)
    #message, response_url = payload['message']['text'], payload['response_url']
    #requests.post(response_url, json={'text' :'---------- You entered: ' + message + '----------'})

    t1 = threading.Thread(target=send_message, args = (payload['message']['text'], payload['response_url']))
    t1.start()
    return make_response('',200)


if __name__ == '__main__':
    app.run()

