from model import Schema
from service import UserAccountService
from flask import Flask      
from flask import request     


app = Flask(__name__)             

@app.route("/accounts")
def homepage():
    return "User Account Service"
@app.route("/accounts/create-user", methods=['PUT'])                  
def create_user():                     
    return UserAccountService().create_user(request.get_json())

@app.route('/accounts/update-email', methods=['POST'])
def update_email():
    return UserAccountService().update_email(request.get_json())

@app.route('/accounts/increment-karma', methods=['POST'])
def increment_karma():
    return UserAccountService().increment_karma(request.get_json())

@app.route('/accounts/decrement-karma', methods=['POST'])
def decrement_karma():
    return UserAccountService().decrement_karma(request.get_json())

@app.route('/accounts/deactivate-account', methods=['POST'])
def deactivate_account():
    return UserAccountService().deactivate_account(request.get_json())

if __name__ == "__main__":       
    Schema()
    app.run(debug=True)                    