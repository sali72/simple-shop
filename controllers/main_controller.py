import json
from models.models import db
from services.main_service import create_logic

def index():
    return {'status': 'OK',
            'localhost:5000/machines/create': 'Create table in mysql database',
            'localhost:5000/machines/insert': 'Insert data in mysql database table(Inserttable)'}


def create():
    
    return create_logic()


# # insert data into table.
# def insert():
    
#     insert_logic()    