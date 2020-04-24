from model import VoteModel
from flask import jsonify

class voteService:
    def __init__(self):
        self.model = VoteModel()

    def up_vote(self, params):
        result = self.model.up_vote(params["pID"])
        return result

    def down_vote(self, params):
        result = self.model.down_vote(params["pID"])
        return result

    def retrieve_votes(self,params):
        result = self.model.retrieve_votes(params["pID"])
        return result

    def list_top_posts_byvotes(self, params):
        result = self.model.list_top_posts_byvotes(params["n"])
        return result

    def get_list(self, params):
        result = self.model.get_list(params["title"])
        return result