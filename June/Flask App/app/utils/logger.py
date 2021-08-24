from flask import make_response
from app import app
from flask import request
import logging
from flask import json,jsonify

from collections import namedtuple

logging.basicConfig(filename='logfile.log', format='%(message)s' ,level=logging.DEBUG)

@app.before_request
def before_request():
   # print(request.get_json())
   logging.debug(request.get_json())

@app.after_request
def after_request(response):
    after_request = response.get_json()
    after_request['done_by'] ='Kausic'
    #d1 = json.loads(str(d))
    #print(type(d1))
    #response = namedtuple("Response", after_request.keys())(*after_request.values())
    #print(response)
    logging.debug(after_request)
    #return jsonify(after_request)
    #return response
    headers = {"Content-Type": "application/json"}
    return make_response(jsonify(after_request),response.status,headers)