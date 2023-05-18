import json
from flask import request
from flask_restful import Resource
from flask_login import login_required, login_user, logout_user, current_user
from security import admin_only, load_user
from models.models import db
from services.user_service import *
import werkzeug


class Login(Resource):
    def post(self):
        claimed_user =  json_to_user()
        user = read_user_by_email_logic(claimed_user.email)
        if werkzeug.security.check_password_hash(user.password, claimed_user.password):
            login_user(user)
            print(f'{user.name} logged in')
            return {"success": f'{user.name} logged in'}, 200
        else:
            return {"error": "Email or Password is wrong"}, 400
        
class Register(Resource):
    def post(self):
        new_user =  json_to_user()
        user = read_user_by_email_logic(new_user.email)
        if not user:
            create_user_logic(new_user)
            print(f'{new_user.name} registered')
            return {"success": f'{new_user.name} registered'}, 200
        else:
            return {"error": "Email already exists"}, 400

class Logout(Resource):
    @login_required
    def post(self):
        user_name = current_user.name
        print(f'{user_name} logged out')
        logout_user()
        return {"success": f'{user_name} logged out'}, 200

class UsersList(Resource):
    # Create a user
    @admin_only
    def post(self):
        return create_user_logic(json_to_user())
    # Read all users
    @admin_only
    def get(self):
        users = read_all_user_logic()
        json_users = []
        for user in users:
            json_users.append(user.to_dict())
        return json_users, 200

class Users(Resource):
    @admin_only
    def get(self, id):
        return read_one_user_logic(id).to_dict(), 200

    @admin_only
    def put(self, id):
        return update_user_logic(id, json_to_user())

    @admin_only
    def delete(self, id):
        return delete_user_logic(id)

def json_to_user():
    json_user = request.get_json()
    new_user = User()
    if 'name' in json_user:
        new_user.name = json_user['name']
    new_user.email = json_user['email']
    new_user.password = json_user['password']
    return new_user

