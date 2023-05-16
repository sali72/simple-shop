import json
from flask import request
from flask_restful import Resource
from flask_login import login_required
from security import admin_only, load_user
from models.models import db
from services.product_service import *


class ProductsList(Resource):
    # Create a product
    @admin_only
    def post(self):
        return create_product_logic(json_to_product())
    # Read all products
    def get(self):
        return read_all_product_logic()

class Products(Resource):
    def get(self, id):
        return read_one_product_logic(id)

    @admin_only
    def put(self, id):
        return update_product_logic(id, json_to_product())
    @admin_only
    def delete(self, id):
        return delete_product_logic(id)

def json_to_product():
    json_product = request.get_json()
    new_product = Product()
    new_product.name = json_product['name']
    new_product.description = json_product['description']
    new_product.count = json_product['count']
    new_product.price = json_product['price']
    return new_product
