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
        return create_product_logic(json_to_product(request.get_json()))
    # Read all products
    def get(self):
        products = read_all_product_logic()
        json_products = []
        for product in products:
            json_products.append(product.to_dict())
        return json_products, 200

class Products(Resource):
    def get(self, id):
        return read_one_product_logic(id).to_dict(), 200

    @admin_only
    def put(self, id):
        return update_product_logic(id, json_to_product(request.get_json()))
    @admin_only
    def delete(self, id):
        return delete_product_logic(id)

def json_to_product(json_product):
    new_product = Product()
    if 'id' in json_product:
        new_product.id = json_product['id']
    if 'name' in json_product:
        new_product.name = json_product['name']
    if 'description' in json_product:
        new_product.description = json_product['description']
    new_product.count = json_product['count']
    if 'price' in json_product:
        new_product.price = json_product['price']
    return new_product
