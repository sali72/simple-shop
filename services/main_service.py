import json
from models.models import  db
from functools import wraps

def create_logic():
    try:
        # create tables if not exists.
        db.create_all()
        db.session.commit()
        return '==================TABLES CREATED=================='

    except Exception as e:
        print(e)
        return '==================TABLES NOT CREATED!!!=================='

# exception_handler decorator
def exception_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)
            return {"error": "Something went wrong !"}, 400
    return wrapper
