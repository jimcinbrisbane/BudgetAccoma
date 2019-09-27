from flask import Blueprint,render_template, redirect, url_for, request
from .models import User,Item,Bid
from .forms import RegestierForm
from .forms import LoginForm
from .forms import itemForm
import datetime
from . import db
from werkzeug.utils import secure_filename
import os

def check_upload_file(form):
          # get file data from form
          fp = form.image.data
          filename= fp.filename
          # get the current path of the module file... store file relative to this path
          BASE_PATH= os.path.dirname(__file__)
          #uploadfilelocation – directory of this file/static/image
          upload_path= os.path.join(BASE_PATH,'static/img', secure_filename(filename))
          # store relative path in DB as image location in HTML is relative
          db_upload_path= '/static/image/'+ secure_filename(filename)
          # save the file and return the dbupload path
          fp.save(upload_path)
          return db_upload_path
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

@mainbp.route('/landlord')
def post():
    tag_line="I'm the landlord"
    
    aform = itemForm()

    return render_template('index_reuse.html', tag_line=tag_line,
                    #form=form, form2=form2, 
                    aform=aform)
@mainbp.route('/a/<id>') 
def show(id): 
  destination = Item.query.filter_by(id=id).first()  
  return render_template('u.html', destination=destination)

@mainbp.route('/create', methods = ['GET','POST'])
def create_item():
  aform = itemForm()
  if aform.validate_on_submit():
    db_file_path=check_upload_file(aform)
    print(db_file_path)

        # a simple function: doesnot   handleerrorsin filetypesand  filenot  beinguploaded
    
    # if the form was successfully submitted
    # access the values in the form data
    print([aform.title.data,aform.description.data,aform.gas.data,aform.price.data,aform.water.data,aform.address.data,aform.gas.data,aform.mobile.data])
    newitem = Item(id = datetime.datetime.now().isoformat(),
                title=aform.title.data, 
                description=aform.description.data,
                image= db_file_path,
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


