from models.models import  db
from models.models import User
from services.main_service import exception_handler
import werkzeug

# main methods
@exception_handler
def create_user_logic(user:User):
    entered_password = user.password
    hashed_pass = werkzeug.security.generate_password_hash(entered_password, method='pbkdf2:sha256', salt_length=8)
    user.password = hashed_pass
    db.session.add(user)
    db.session.commit()
    return {"success": "User created"}, 200

@exception_handler   
def read_all_user_logic():
    return db.session.query(User).all()

@exception_handler
def read_user_by_email_logic(email):
    return db.session.execute(db.select(User).filter_by(email=email)).scalar()

@exception_handler
def read_one_user_logic(id):
    return db.session.query(User).get(id)

@exception_handler
def update_user_logic(id, updated_user:User):
    user = read_one_user_logic(id)
    user.name = updated_user.name
    user.description = updated_user.description
    user.count = updated_user.count
    user.price = updated_user.price
    user.receipts = updated_user.receipts
    db.session.commit()
    return {"success": "User updated"}, 200

@exception_handler
def delete_user_logic(id):
    user = read_one_user_logic(id)
    db.session.delete(user)
    db.session.commit()
    return {"success": "User deleted"}, 200
    


    



