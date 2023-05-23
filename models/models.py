from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

db = SQLAlchemy()


class User(db.Model, SerializerMixin, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(1000), primary_key=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    # one user has many receipts
    receipts = relationship("Receipt", back_populates='user')


# receipt_product = db.Table(
#     'receipt_product',
#     db.Column('receipt_id', db.Integer, db.ForeignKey('receipt.id'), primary_key=True),
#     db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
# )

class ReceiptProduct(db.Model, SerializerMixin):
    __tablename__ = 'receipt_product'
    receipt_id = db.Column(db.Integer, db.ForeignKey('receipt.id'), primary_key=True)
    receipt = relationship("Receipt", back_populates='receipt_products')
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    product = relationship("Product", back_populates='receipt_products')
    count = db.Column(db.Integer)


class Receipt(db.Model, SerializerMixin):
    __tablename__ = 'receipt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Integer, primary_key=False)
    is_finalized = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # one receipt has one user
    user = relationship("User", back_populates='receipts')
    # one receipt has many receipt_products
    receipt_products = db.relationship('ReceiptProduct', back_populates='receipt')

    # products = db.relationship('Product', secondary=receipt_product, lazy='subquery', 
    #                 #  back_populates='receipts' , 
    #                 backref=db.backref('receipts', lazy=True))


class Product(db.Model, SerializerMixin):
    __tablename__ = 'product'

    serialize_only = ('id', 'name', 'description', 'price', 'count')
    # serialize_rules = ('-receipts')
    # serialize_rules = ('-users.login.users',)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, primary_key=False)
    description = db.Column(db.String(100))
    price = db.Column(db.Integer)
    count = db.Column(db.Integer)
    # one product has many receipt_product
    receipt_products = db.relationship('ReceiptProduct', back_populates='product')


