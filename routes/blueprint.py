from flask import Blueprint
from controllers.machineController import index, create

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)
# blueprint.route('/insert', methods=['GET'])(insert)