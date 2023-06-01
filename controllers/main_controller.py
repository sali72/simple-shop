import json
from models.models import db
from services.main_service import create_logic
from security import admin_only
from services.product_service import *
from flask import render_template

def index():
    products = read_all_product_logic()
    return render_template('home.html' )

@admin_only
def create():
    
    return create_logic()



