import json
from flask import request
from flask_restful import Resource
from flask_login import login_required
from security import admin_only, load_user
from models.models import db
from services.receipt_service import *


class ReceiptsList(Resource):
    # Create a receipt
    @admin_only
    def post(self):
        return create_receipt_logic(json_to_receipt())
    # Read all receipts
    def get(self):
        return read_all_receipt_logic()

class Receipts(Resource):
    def get(self, id):
        return read_one_receipt_logic(id)
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
    return new_receipt
