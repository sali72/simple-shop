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
def read_receipts_by_userId_logic(id):
    return db.session.execute(db.select(Receipt).filter_by(user=id)).scalars()

@exception_handler   
def read_receipt_by_date_logic(date):
    return db.session.execute(db.select(Receipt).filter_by(date=date)).scalar()
    
@exception_handler
def read_one_receipt_logic(id):
    return db.session.query(Receipt).get(id)

@exception_handler
def update_receipt_logic(id, updated_receipt:Receipt):
    receipt = read_one_receipt_logic(id)
    receipt.date = updated_receipt.date
    receipt.receipt_products = updated_receipt.receipt_products
    receipt.is_finalized = updated_receipt.is_finalized
    db.session.commit()
    return {"success": "Receipt updated"}, 200

@exception_handler
def update_receipt_for_buy_logic(user, receipt, products):
    # replaces all the products with new ones
    receipt.receipt_products = products
    for r in user.receipts:
        if r is receipt:
            r.receipt_products = products
    db.session.commit()
    return {"success": "Receipt updated"}, 200

@exception_handler
def delete_receipt_logic(id):
    receipt = read_one_receipt_logic(id)
    db.session.delete(receipt)
    db.session.commit()
    return {"success": "Receipt deleted"}, 200
    

    


