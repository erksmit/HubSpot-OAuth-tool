# generates a Oauth authorization url for linking the application and opens it in browser
# this program must be ran through flask with "flask --app oauth_authorize.py run"

import json5
import webbrowser
from flask import Flask, request
import requests

API_URI = 'https://api.hubapi.com'
config = json5.load(open('config.json5'))
client_id = config['client_id']
client_secret = config['client_secret']
redirect_uri = 'http://localhost:5000/oauth_callback'
scopes = config['scopes']
refresh_token = config['refresh_token']
use_oauth = config['use_oauth']
access_token = config['access_token']


flask = Flask(__name__)

@flask.get("/oauth_callback")
def recieve_auth_code():
    code = request.args.get('code')
    return exchange_tokens(auth_code=code)
    
def exchange_tokens(auth_code: str):
    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': auth_code
    }
    response = requests.post(API_URI + '/oauth/v1/token', data=data)
    if response.status_code == 200:
        body = response.json()
        refresh_token = body['refresh_token']
        print('refresh token: ' + refresh_token)
        return f'<p>your refresh token is: {refresh_token}</p>'
    else:
        print(response.text)
        return response.text


scope_string = '%20'.join(scopes)
auth_url = f'https://app.hubspot.com/oauth/authorize?client_id={client_id}&scope={scope_string}&redirect_uri={redirect_uri}'

webbrowser.open(auth_url)
