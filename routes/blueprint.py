from flask import Blueprint
from flask_restful import Resource, Api
from controllers.main_controller import index, create
from controllers.product_controller import ProductsList, Products
from controllers.user_controller import *
from controllers.receipt_controller import *


blueprint = Blueprint('api', __name__)
api = Api(blueprint)

blueprint.route('/', methods=['GET'])(index)
blueprint.route('/create', methods=['GET'])(create)

# product routs
api.add_resource(ProductsList, '/products')
api.add_resource(Products,  '/products/<int:id>')

# user routs
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(Register, '/register')
api.add_resource(UsersList, '/users')
api.add_resource(Users,  '/users/<int:id>')

# receipt routs
api.add_resource(AddToCart, '/add-to-cart')
api.add_resource(FinishPurchase, '/finish-purchase')