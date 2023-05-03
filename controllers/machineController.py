import json
from models.machine import Inserttable, db
from services.user_service import insert_logic, create_logic

def index():
    return {'status': 'OK',
            'localhost:5000/machines/create': 'Create table in mysql database',
            'localhost:5000/machines/insert': 'Insert data in mysql database table(Inserttable)'}


def create():
    
    create_logic()


# insert data into table.
def insert():
    
    insert_logic()    