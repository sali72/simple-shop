import json
from flask import jsonify
from models.models import  db
from models.models import Product

def create_product_logic():
    try:
        # create  if not exists.
        
        db.session.commit()
        return 'json'

    except Exception as e:
        print(e)
        return 'json error'
    
def read_all_product_logic():
    try:
        products = db.session.query(Product).all()
        json_products = []
        for product in products:
            json_product = json.dumps(product.__dict__)
            json_products.append(json_product)
        return jsonify(json.dumps(json_products, indent=4))

    except Exception as e:
        print(e)
        return 'json error'

