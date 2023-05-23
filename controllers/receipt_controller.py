import json
from flask import request
from flask_restful import Resource
from flask_login import login_required, current_user
from security import admin_only, load_user
from models.models import db, User
from services.receipt_service import *
from services.user_service import *
from controllers.product_controller import *
from services.receipt_product_service import *
from datetime import datetime

class FinishPurchase(Resource):
    @login_required
    def post(self):
        logged_in_user = current_user._get_current_object()
        logged_in_receipt = find_receipt(logged_in_user)
        # if transaction completed & there is something in the cart
        r_ps = logged_in_receipt.receipt_products
        if r_ps != []:
            # reduce the products from db
            for r_p in r_ps:
                product = read_one_product_logic(r_p.product_id)
                if (product.count - r_p.count) > 0:
                    product.count = (product.count - r_p.count)
                else:
                    {"error": f"not enough {product.name}"}
                update_product_logic(product.id, product)
            
            logged_in_receipt.is_finalized = True
            update_receipt_logic(logged_in_receipt.id, logged_in_receipt)
            return {"success": "your purchase is finalized"}
        else:
            return {"error": "maybe your cart is empty"}
        


class AddToCart(Resource):

    @login_required
    def post(self):
        logged_in_user = current_user._get_current_object()
        logged_in_receipt = find_receipt(logged_in_user)
        # adding the products to receipt
        json_products = request.get_json()
        products = []
        # read product objects
        for json_product in json_products:
            read_product = read_one_product_logic(json_product['id'])

            receipt_product = ReceiptProduct()
            # checks if a receipt_product already exists
            for user_receipt_product in logged_in_receipt.receipt_products:
                if user_receipt_product.product_id == json_product['id']:
                   receipt_product = user_receipt_product

            receipt_product.product_id = json_product['id']
            receipt_product.receipt_id = logged_in_receipt.id
            receipt_product.count = json_product['count']
            read_product.receipt_products.append(receipt_product)
            update_product_logic(json_product['id'], read_product)
            products.append(read_product)
        update_receipt_for_buy_logic(logged_in_user, logged_in_receipt, products)

def find_receipt(user):
    # finding if an open receipt exists
    if not user.receipts:
        print('receipts are empty, new receipt will be created')
    elif user.receipts:
        for receipt in user.receipts:
            if not receipt.is_finalized:
                print('a not finalized receipt exists')
                return receipt
    else:
        print('receipts are finalized, new receipt will be created')
    # creating a new receipt
    new_receipt = Receipt()
    new_receipt.is_finalized = False
    now = datetime.now()
    new_receipt.date = now
    # adding the receipt to user
    user.receipts.append(new_receipt)
    update_user_logic(user.id, user)
    return read_receipt_by_date_logic(now)


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
