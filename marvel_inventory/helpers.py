from functools import wraps
from flask import request, jsonify, json
import secrets
import decimal
import requests

from marvel_inventory.models import User

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split()[1]
            print(token)
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401 #status code says 'thing we were looking for was not provided'

        try:
            our_user = User.query.filter_by(token=token).first()
            print(our_user)
            if not our_user or our_user.token != token:
                return jsonify({'message':'Token is invalid'})

        except:
            our_user = User.query.filter_by(token=token).first()
            if token != our_user.token and secrets.compare_digest(token, our_user.token):
                return jsonify({'message':'Token is invalid'})
        
        return  our_flask_function(our_user, *args, **kwargs)
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)
    

# def random_joke_generator():
#     url = "https://dad-jokes.p.rapidapi.com/random/joke"

#     headers = {
#         "X-RapidAPI-Key": "58699bc98cmshd355f1f8b50dd89p1464d6jsn1e68fde8e1d6",
#         "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
#     }

#     response = requests.request("GET", url, headers=headers)

#     data = response.json()

#     return data['body'][0]['setup']+' '+data['body'][0]['punchline']

    