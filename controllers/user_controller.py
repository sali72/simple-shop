import json
from flask import request
from flask_restful import Resource
from flask_login import login_required, login_user
from security import admin_only, load_user
from models.models import db
from services.user_service import *
import werkzeug


class Login(Resource):
    # login
    def post(self):
        claimed_user =  json_to_user()
        user = read_user_by_email_logic()
        if werkzeug.security.check_password_hash(user.password, claimed_user.password):
            login_user(user)
            print(f'{user.name} logged in')
        else:
            return {"error": "Email or Password is wrong"}, 400


class UsersList(Resource):
    # Create a user
    def post(self):
        return create_user_logic(json_to_user())
    # Read all users
    def get(self):
        return read_all_user_logic()

class Users(Resource):
    def get(self, id):
        return read_one_user_logic(id)

    def put(self, id):
        return update_user_logic(id, json_to_user())

    def delete(self, id):
        return delete_user_logic(id)

def json_to_user():
    json_user = request.get_json()
    new_user = User()
    new_user.name = json_user['name']
    new_user.email = json_user['email']
    new_user.password = json_user['password']
    return new_user

