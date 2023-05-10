from flask import Blueprint
from controllers.main_controller import index, create
from controllers.product_controller import *


blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
# blueprint.route('/insert', methods=['GET'])(insert)

# product routs
blueprint.route('/products', methods=['GET'])(read_all_products)