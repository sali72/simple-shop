import json
from models.models import db
from services.main_service import create_logic
from security import admin_only

def index():
    return {'status': 'OK',
            'localhost:5000/machines/create': 'Create table in mysql database',
            'localhost:5000/machines/insert': 'Insert data in mysql database table(Inserttable)'}

@admin_only
def create():
    
    return create_logic()



