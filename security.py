from flask_login import LoginManager, current_user, logout_user
from functools import wraps
from flask import abort
from services.user_service import read_one_user_logic


login_manager = LoginManager()

# admin_only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_anonymous or current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)        
    return decorated_function

@login_manager.user_loader
def load_user(user_id):
    return read_one_user_logic(user_id)