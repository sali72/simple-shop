import json
from flask import jsonify
from models.models import  db
from models.models import Product
from services.main_service import exception_handler

# main methods
@exception_handler
def create_product_logic(product:Product):
    db.session.add(product)
    db.session.commit()
    return {"success": "Product created"}, 200


@exception_handler   
def read_all_product_logic():
    products = db.session.query(Product).all()
    json_products = []
    for product in products:
        json_products.append(product.to_dict())
    return json_products, 200
    
@exception_handler
def read_one_product_logic(id):
    product = get_product(id)
    return product.to_dict(), 200

@exception_handler
def update_product_logic(id, updated_product:Product):
    product = get_product(id)
    product.name = updated_product.name
    product.description = updated_product.description
    product.count = updated_product.count
    product.price = updated_product.price
    db.session.commit()
    return {"success": "Product updated"}, 200

@exception_handler
def delete_product_logic(id):
    product = get_product(id)
    db.session.delete(product)
    db.session.commit()
    return {"success": "Product deleted"}, 200
    
# helping methods
def get_product(id):
    return db.session.query(Product).get(id)

    


