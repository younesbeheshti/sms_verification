from flask import Flask, jsonify, request
import requests 
import config
app = Flask(__name__)



@app.route('/v1/process, methods = ['POST', 'GET'])
def process():
    """this is a call back from KeveNeger, will get sender andn message and will check if it si valid,
    then answers back
    """
    data = request.form
    sender = date['from']
    message = data['message']

