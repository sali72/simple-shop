import json
from flask import jsonify
from models.models import  db
from models.models import Receipt
from services.main_service import exception_handler

# main methods
@exception_handler
def create_receipt_logic(receipt:Receipt):
    db.session.add(receipt)
    db.session.commit()
    return {"success": "Receipt created"}, 200


@exception_handler   
def read_all_receipt_logic():
    receipts = db.session.query(Receipt).all()
    json_receipts = []
    for receipt in receipts:
        json_receipts.append(receipt.to_dict())
    return json_receipts, 200
    
@exception_handler
def read_one_receipt_logic(id):
    receipt = get_receipt(id)
    return receipt.to_dict(), 200

@exception_handler
def update_receipt_logic(id, updated_receipt:Receipt):
    receipt = get_receipt(id)
    receipt.date = updated_receipt.date
    db.session.commit()
    return {"success": "Receipt updated"}, 200

@exception_handler
def delete_receipt_logic(id):
    receipt = get_receipt(id)
    db.session.delete(receipt)
    db.session.commit()
    return {"success": "Receipt deleted"}, 200
    
# helping methods
def get_receipt(id):
    return db.session.query(Receipt).get(id)

    


