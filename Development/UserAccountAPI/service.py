from model import UserModel
from flask import jsonify

class UserAccountService:
    def __init__(self):
        self.model = UserModel()
        
    def create_user(self, params):
        result = self.model.create_user(params["user_name"], params["email"], params["karma"])
        return result

    def update_email(self, params):
        result = self.model.update_email(params["user_name"], params["email"])
        return result

    def increment_karma(self, params):
        result = self.model.increment_karma(params["user_name"])
        return result
    
    def decrement_karma(self, params):
        result = self.model.decrement_karma(params["user_name"])
        return result

    def deactivate_account(self, params):
        result = self.model.deactivate_account(params["user_name"])
        return result