import json
from flask import request
from flask_restful import Resource
from flask_login import login_required, current_user
from security import admin_only, load_user
from models.models import db, User
from services.receipt_service import *
from controllers.product_controller import *


class Buy(Resource):

    @login_required
    def post(self):
        logged_in_user = current_user._get_current_object()
        # finding if an open receipt exists
        logged_in_receipt = Receipt()
        if not logged_in_user.receipts:
            print('receipts are empty, new receipt is created')
        elif logged_in_user.receipts:
            for receipt in logged_in_user.receipts:
                if not receipt.is_finalized:
                    logged_in_receipt = receipt
                    print('a not finalized receipt exists')
                    break
        else:
            print('receipts are finalized, new receipt is created')
        # adding the products to receipt
        products = request.get_json()
        # for json_product in products:
        #     product = json_to_product(json_product)
        #     logged_in_receipt.products.append(product)
        update_receipt_for_buy_logic(logged_in_receipt.id ,products)


class ReceiptsList(Resource):
    # Create a receipt
    @admin_only
    def post(self):
        return create_receipt_logic(json_to_receipt())
    # Read all receipts
    def get(self):
        receipts = read_all_receipt_logic()
        json_receipts = []
        for receipt in receipts:
            json_receipts.append(receipt.to_dict())
        return json_receipts, 200

class Receipts(Resource):
    def get(self, id):
        return read_one_receipt_logic(id).to_dict(), 200
    @admin_only
    def put(self, id):
        return update_receipt_logic(id, json_to_receipt())
    @admin_only
    def delete(self, id):
        return delete_receipt_logic(id)

def json_to_receipt():
    json_receipt = request.get_json()
    new_receipt = Receipt()
    new_receipt.id = json_receipt['id']
    if 'date' in json_receipt:
        new_receipt.date = json_receipt['date']
    if 'is_finalized' in json_receipt:
        new_receipt.is_finalized = json_receipt['is_finalized']
    return new_receipt
