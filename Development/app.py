from model import Schema
from service import voteService
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/votes")
def homepage():
    return "Hello!"


@app.route("/votes/up_vote", methods=['POST'])
def up_vote():
    return voteService().up_vote(request.get_json())

@app.route("/votes/down_vote", methods=['POST'])
def down_vote():
    return voteService().down_vote(request.get_json())


@app.route("/votes/retrieve_votes", methods=['GET'])
def retrieve_votes():
    return voteService().retrieve_votes(request.get_json())


@app.route("/votes/list_top_posts_byvotes", methods=['GET'])
def list_top_posts_byvotes():
    return voteService().list_top_posts_byvotes(request.get_json())


@app.route("/votes/get_list", methods=['GET'])
def get_list():
    return voteService().get_list(request.get_json())


if __name__ == "__main__":       
    Schema()
    app.run(debug=True) 