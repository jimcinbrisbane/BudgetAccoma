from flask import Blueprint,render_template, redirect, url_for, request
from .models import User,Item,Bid
from .forms import RegestierForm
from .forms import LoginForm
from .forms import itemForm

from . import db

mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    tag_line='Budget Accomadation: Cheap Sharehouse For Broke You!'

    return render_template('homepage.html', tag_line=tag_line)
#@mainbp.route('/<id>') 
#def show(id): 
  #destination = Destination.query.filter_by(id=id).first()  
  #cform = cokForm()
 # return render_template('user.html', destination=destination)
 #form=RegestierForm()
 #form2=LoginForm() 
@mainbp.route('/landlord')
def post():
    tag_line="I'm the landlord"
    
    aform = itemForm()

    return render_template('index_reuse.html', tag_line=tag_line,
                    #form=form, form2=form2, 
                    aform=aform)
@mainbp.route('/<id>') 
def show(id): 
  destination = Item.query.filter_by(id=id).first()  
  return render_template('u.html', destination=destination)

@mainbp.route('/create', methods = ['GET','POST'])
def create_item():
  aform = itemForm()
  if aform.validate_on_submit():
    # if the form was successfully submitted
    # access the values in the form data
    print([aform.title.data,aform.description.data,aform.gas.data,aform.price.data,aform.water.data,aform.address.data,aform.gas.data,aform.mobile.data])
    newitem = Item(id = "jsjakaka",
                title=aform.title.data, 
                description=aform.description.data,
                image="working on it",
                price= aform.price.data,
                address=aform.address.data,
                water = aform.water.data,
                wifi = aform.wifi.data,
                eletricity = aform.eletricity.data,
                gas = aform.gas.data,
                mobile = aform.mobile.data
                #user_id = "working on it",
                )
    # add the object to the db session
    db.session.add(newitem)
    # commit to the database
    db.session.commit()
    #flash('Successfully created new travel destination', 'success')
    print('Successfully created new room info', 'success')
    return redirect(url_for('main.index'))




