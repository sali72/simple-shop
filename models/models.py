from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()


# class Inserttable(db.Model):
#     '''Data for ON/OFF should be dumped in this table.'''
#     __tablename__ = 'inserttable'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     machineid = db.Column(db.Integer, primary_key=False)
#     stateid = db.Column(db.Integer, primary_key=False)
#     state = db.Column(db.String(80), nullable=False)

#     def __repr__(self):
#         return '<machineid %r>' % self.machineid


class User(db.Model, SerializerMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Integer, primary_key=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # one user has many receipts
    receipts = relationship("Receipt", back_populates='user')


receipt_product = db.Table(
    'receipt_product',
    db.Column('receipt_id', db.Integer, db.ForeignKey('receipt.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True)
)

class Receipt(db.Model, SerializerMixin):
    __tablename__ = 'receipt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Integer, primary_key=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # one receipt has one user
    user = relationship("User", back_populates='receipts')
    # one receipt has many products
    products = db.relationship('Product', secondary=receipt_product, back_populates='receipts')

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
    receipts = db.relationship('Receipt', secondary=receipt_product, back_populates='products')

