from model import Schema
from service import msgService
from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/msgs")
def homepage():
    return "Hello! Welcome to the Message Microservice!"

@app.route("/msgs/send_msg", methods=['POST'])
def send_msg():
    return msgService().send_msg(request.get_json())

@app.route("/msgs/delete_msg", methods=['DELETE'])
def delete_msg():
    return msgService().delete_msg(request.get_json())

@app.route("/msgs/fav_msg", methods=['POST'])
def fav_msg():
    return msgService().fav_msg(request.get_json())

@app.route("/msgs/unfav_msg", methods=['POST'])
def unfav_msg():
    return msgService().unfav_msg(request.get_json())


if __name__ == "__main__":       
    Schema()
    app.run(debug=True) 