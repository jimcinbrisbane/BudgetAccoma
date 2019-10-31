# sql database sigma   
from . import db
from flask_login import UserMixin
from datetime import datetime

#user sigma
class User(db.Model, UserMixin):
    __tablename__='user' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(32), index=True, nullable=False)
    mobile = db.Column(db.String(32), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)
    def __repr__(self): #string print method
        return "<name: {}, emailid: {}, id: {}>".format(self.name, self.emailid, self.id)
    # relation to call user.comments and comment.created_by

#item sigma
class Item(db.Model, UserMixin):
    __tablename__ = 'item'
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(32))
    description = db.Column(db.String(255))
    image = db.Column(db.String(32))
    price = db.Column(db.Integer)
    address = db.Column(db.String(255))
    water = db.Column(db.Boolean)
    wifi = db.Column(db.Boolean)
    eletricity = db.Column(db.Boolean)
    gas = db.Column(db.Boolean)
    mobile = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sold = db.Column(db.Boolean)
    def __repr__(self): #string print method
        return "<id: {}, image: {}, title: {}, description: {}, price: {}, address: {},water:{},wifi{},eletricity{},gas{}>".format(self.id, self.image, self.title, self.description, self.price, self.address, self.water, self.wifi, self.eletricity, self.gas)

#bid sigma
class Bid(db.Model):
    __tablename__ = 'bid'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    user_name = db.Column(db.String, db.ForeignKey('user.name'))
    mobile = db.Column(db.Integer, db.ForeignKey('user.mobile'))
    item_id = db.Column(db.String, db.ForeignKey('item.id'))
    def __repr__(self): #string print method

         return "<id: {}, date: {}, user_name: {},item_id: {},mobile:{}>".format(self.id, self.date, self.user_name, self.item_id, self.mobile)
