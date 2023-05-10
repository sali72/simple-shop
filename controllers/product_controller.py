import json
from flask import request
from flask_restful import Resource
from models.models import db
from services.product_service import *


class Products(Resource):
    def post(self):
        json_product = request.get_json()
        new_product = Product()
        new_product.name = json_product['name']
        new_product.description = json_product['description']
        new_product.count = json_product['count']
        new_product.price = json_product['price']
        return create_product_logic(new_product)

    def get(self):
        return read_all_product_logic()
    
    # def get(self, id):
    #     pass

    def put(self, id):
        pass

    def delete(self, id):
        pass