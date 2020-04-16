from model import PostModel
from flask import jsonify

class PostService:
    def __init__(self):
        self.model = PostModel()
        
    def create_post(self, params):
        result = self.model.create_post(params["title"], params["text"], params["community"], params["URL"], params["username"], params["postDate"])
        return result

    def delete_post(self, params):
        result = self.model.delete_post(params["title"])
        return result

    def retrieve_post(self, params):
        result = self.model.retrieve_post(params['title'])
        return result
    
    def list_particular(self, params):
        result = self.model.list_particular(params['community'], params['n'])
        return result

    def list_recent(self, params):
        result = self.model.list_recent(params['n'])
        return result
