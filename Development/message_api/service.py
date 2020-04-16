from model import MsgModel
from flask import jsonify

class msgService:
    def __init__(self):
        self.model = MsgModel()

    def send_msg(self, params):
        result = self.model.up_vote(params["user_fr"], params["user_to"], params["msg_desc"], params["msg_flag"])
        return result

    def delete_msg(self, params):
        result = self.model.down_vote(params["msg_id"])
        return result

    def fav_msg(self,params):
        result = self.model.retrieve_votes(params["msg_id"])
        return result