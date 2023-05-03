from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

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


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Integer, primary_key=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    # one user has many receipts
    receipts = relationship("Receipt", back_populates='user')


class Receipt(db.Model):
    __tablename__ = 'receipt'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Integer, primary_key=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # one receipt has one user
    user = relationship("User", back_populates='receipts')
    # one receipt has many products
    products = relationship("ReceiptProduct", back_populates='receipt')


class ReceiptProduct(db.Model):
    __tablename__ = 'receipt_product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    count = db.Column(db.Integer)
    receipt_id = db.Column(db.Integer, db.ForeignKey("receipt.id"))
    # one receipt_product has one receipt
    receipt = relationship("User", back_populates='receipts')
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    # one receipt_product has one product
    product = relationship("Product", back_populates='receipts')


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), primary_key=False)
    description = db.Column(db.String(100))
    price = db.Column(db.Integer)
    # one product has many receipt_product
    receipt_products = relationship("ReceiptProduct", back_populates='product')
