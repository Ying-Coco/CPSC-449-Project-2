from model import MsgModel
from flask import jsonify

class msgService:
    def __init__(self):
        self.model = MsgModel()

    def send_msg(self, params):
        result = self.model.send_msg(params["user_fr"], params["user_to"], params["msg_desc"], params["msg_flag"])
        return result

    def delete_msg(self, params):
        result = self.model.delete_msg(params["msg_id"])
        return result

    def fav_msg(self,params):
        result = self.model.fav_msg(params["msg_id"])
        return result