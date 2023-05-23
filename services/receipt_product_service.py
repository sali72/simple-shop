from models.models import  db
from models.models import ReceiptProduct
from services.main_service import exception_handler

# main methods
@exception_handler
def create_receipt_product_logic(receipt_product:ReceiptProduct):
    db.session.add(receipt_product)
    db.session.commit()
    return {"success": "ReceiptProduct created"}, 200


@exception_handler   
def read_all_receipt_product_logic():
    return db.session.query(ReceiptProduct).all()
    
@exception_handler
def read_one_receipt_product_logic(id):
    return db.session.query(ReceiptProduct).get(id)

@exception_handler
def update_receipt_product_logic(id, updated_receipt_product:ReceiptProduct):
    receipt_product = read_one_receipt_product_logic(id)
    receipt_product.count = updated_receipt_product.count
    receipt_product.product = updated_receipt_product.product
    receipt_product.receipt = updated_receipt_product.receipt
    db.session.commit()
    return {"success": "ReceiptProduct updated"}, 200

@exception_handler
def delete_receipt_product_logic(id):
    receipt_product = read_one_receipt_product_logic(id)
    db.session.delete(receipt_product)
    db.session.commit()
    return {"success": "ReceiptProduct deleted"}, 200
    

    


