# sql database sigma   
from . import db
from datetime import datetime

#user sigma
class User(db.Model):
    __tablename__='user' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(32), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)
    def __repr__(self): #string print method
        return "<name: {}, emailid: {}>".format(self.name, self.emailid)
    # relation to call user.comments and comment.created_by

#item sigma
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String(32))
    description = db.Column(db.String(255))
    image = db.Column(db.String(32))
    price = db.Column(db.String(10))
    address = db.Column(db.String(255))
    water = db.Column(db.Boolean)
    wifi = db.Column(db.Boolean)
    eletricity = db.Column(db.Boolean)
    gas = db.Column(db.Boolean)
    mobile = db.Column(db.Integer)
    #user_id = db.relationship('User', backref='user')
    def __repr__(self): #string print method
        return "<id: {}, image: {}>".format(self.id, self.image)

#bid sigma
class Bid(db.Model):
    __tablename__ = 'bid'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    perDesc = db.Column(db.String(512))
    lengthofstay = db.Column(db.String(255))


    #user_id = db.relationship('User', backref='user')
    #item_id = db.relationship('Item', backref='item')





