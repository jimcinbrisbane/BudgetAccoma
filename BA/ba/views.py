from flask import Blueprint,render_template, redirect, url_for, request
from flask_login import UserMixin, login_manager
from .models import User,Item,Bid
from .forms import RegestierForm, LoginForm, itemForm, searchForm
import datetime
from . import db
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
from . import create_app


#############################################
#               R O U T I N G               #                
#############################################

mainbp = Blueprint('main',__name__)
@mainbp.route('/search', methods = ['GET'])
def search():
    search_form = searchForm()
    if (search_form.validate_on_submit()):
        print('Search Form Submitted')
        #get username,password and email from the form
        price = search_form.price.data
        location = search_form.location.data
        #info = Item.query.filter_by(price=price,location=location).first()  
        return redirect(url_for('main.index'))

############################################
# homepage route
@mainbp.route('/')
def index():
    search_form = searchForm()
    tag_line='Budget Accomadation: Cheap Sharehouse For Broke You!'
    room = Item.query.order_by(Item.id.desc()).limit(3).all()
    return render_template('homepage.html', search_form = search_form, room = room, tag_line=tag_line)

############################################
#item form route
@mainbp.route('/landlord')
def post():
    tag_line="I'm the landlord"
    
    aform = itemForm()

    return render_template('index_reuse.html', tag_line=tag_line,
                    #form=form, form2=form2, 
                    aform=aform)

############################################
#information page/room information route
@mainbp.route('/sharehouse/<id>')
def sharehousePage(id):
    info = Item.query.filter_by(id=id).first()  
    tag_line='Budget Accomadation: Cheap Sharehouse For Broke You!'
    name = Item.query.filter_by(id=id).first()  
    return render_template('roomInfo.html', tag_line=tag_line, info=info)

#############################################
#        D A T A B A S E - P A T H          #                
#############################################

def check_upload_file(form):
          # get file data from form
          fp = form.image.data
          filename= fp.filename
          # get the current path of the module file... store file relative to this path
          BASE_PATH= os.path.dirname(__file__)
          #uploadfilelocation – directory of this file/static/image
          upload_path= os.path.join(BASE_PATH,'static/img', secure_filename(filename))
          # store relative path in DB as image location in HTML is relative
          db_upload_path= '/static/img/'+ secure_filename(filename)
          # save the file and return the dbupload path
          fp.save(upload_path)
          return db_upload_path

#############################################
#           C R E A T E - I T E M           #                
#############################################
#fetch item form and insert it to database

@mainbp.route('/create', methods = ['GET','POST'])
def create_item():
  aform = itemForm()
  if aform.validate_on_submit():
    db_file_path=check_upload_file(aform)
    print(db_file_path)
    # a simple function: doesnot handle errors in file types and file not being uploaded
    
    # if the form was successfully submitted, access the values in the form data
    print([aform.title.data,aform.description.data,aform.gas.data,aform.price.data,aform.water.data,aform.address.data,aform.gas.data,aform.mobile.data])
    
    #insert item into database
    newitem = Item(id = datetime.datetime.now().isoformat(),#as you can see I used datetime as Primary Key
                title=aform.title.data, 
                description=aform.description.data,
                image= db_file_path,
                price= aform.price.data,
                address=aform.address.data,
                water = aform.water.data,
                wifi = aform.wifi.data,
                eletricity = aform.eletricity.data,
                gas = aform.gas.data,
                mobile = aform.mobile.data,
                user_id = 1,
                )

    #add the object to the db session
    db.session.add(newitem)
    
    #commit to the database
    db.session.commit()
    #flash('Successfully created new travel destination', 'success')
    print('Successfully created new room info', 'success')
    return redirect(url_for('main.index'))


#############################################
#           R E G I S T R A T I O N         #                
#############################################

@mainbp.route('/reg')
def reg():
    registerform = RegestierForm()
    return render_template('register.html',registerform = registerform)

@mainbp.route('/register', methods = ['POST'])
def register():
    registerform = RegestierForm()
    if registerform.validate_on_submit():
        print('Register Form Submitted')
        #get username,password and email from the form
        username = registerform.user_name.data
        pass_word = registerform.password.data
        email = registerform.email.data

        #create password hash
        hashWord = generate_password_hash(pass_word)

        #create a new user account
        newUser = User(name=username, emailid=email, password_hash=hashWord)
        db.session.add(newUser)
        db.session.commit()

        #return to main page
        return redirect(url_for('main.index'))

#############################################
#                 L O G I N                 #                
#############################################
#initialize login management
login_manager = LoginManager()

#create name of the login function that lets users login
login_manager.login_view ='auth.login'

#create a user load in function that goes by userID
@login_manager.user_loader

#routing for login
@mainbp.route('/login')
def login():
    login_form = LoginForm()
    return render_template('login.html', login_form = login_form)

#this is the login function
@mainbp.route('/log', methods = ['GET','POST'])
def log():
    login_form=LoginForm()
    error=None
    if(login_form.validate_on_submit()):
        username = login_form.user_name.data
        pass_word = login_form.pass_word.data
        u1 = User.query.filter_by(name = user_name).first()

        if u1 is None:
            error='Incorrect Username'
        elif not check_password_hash(u1.check_password_hash,password):
            error='Incorrect Password'
        if error is None:
            login_user(u1)
            return redirect(url_for('main.index'))
        else:
            print(error)
            flash(error)

    return redirect(url_for('main.index'))

