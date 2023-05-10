from flask import Blueprint
from flask_restful import Resource, Api
from controllers.main_controller import index, create
from controllers.product_controller import Products


blueprint = Blueprint('api', __name__)
api = Api(blueprint)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)

# blueprint.route('/insert', methods=['GET'])(insert)

# product routs
api.add_resource(Products, '/products')
