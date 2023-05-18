import json
from flask import jsonify
from models.models import  db
from models.models import Receipt
from services.main_service import exception_handler
from services.product_service import defined_read_one_product_logic

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
def read_receipts_by_userId_logic(id):
    return db.session.execute(db.select(Receipt).filter_by(user=id)).scalar()
    
@exception_handler
def read_one_receipt_logic(id):
    return db.session.query(Receipt).get(id)

@exception_handler
def update_receipt_logic(id, updated_receipt:Receipt):
    receipt = read_one_receipt_logic(id)
    receipt.date = updated_receipt.date
    print(updated_receipt.products)
    # read_products = []
    # for product in updated_receipt.products:
    #     read_product = read_one_product_logic(product.id)
        # read_products.append(read_product)
    db.session.commit()
    return {"success": "Receipt updated"}, 200

@exception_handler
def update_receipt_for_buy_logic(id, products):
    receipt = read_one_receipt_logic(id)
    print(products)
    read_products = []
    for product in products:
        read_product = defined_read_one_product_logic(product['id'])
        read_products.append(read_product)
    receipt.products = read_products
    db.session.commit()
    return {"success": "Receipt updated"}, 200

@exception_handler
def delete_receipt_logic(id):
    receipt = read_one_receipt_logic(id)
    db.session.delete(receipt)
    db.session.commit()
    return {"success": "Receipt deleted"}, 200
    

    


