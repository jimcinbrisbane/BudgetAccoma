from flask import Blueprint,render_template, redirect, url_for, request, flash
from flask_login import LoginManager,login_user,current_user,logout_user, login_required
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
@mainbp.route('/search', methods = ['POST'])
def search():
    search_form = searchForm()
    if (search_form.validate_on_submit()):
        print('Search Form Submitted')
        price = search_form.price.data
        price = int(price)
        price = price + 5
        print(price)
        location = search_form.location.data
        search = "%{}%".format(location)
        try:
         room = Item.query.filter(price <= price,Item.address.like(search)).all()
        #if price and location is not None:
         #   info = Item.message.match("%"+ location +"%").all()  
        #elif price is None:
          #  info = Item.query.filter_by(Item.message.match("%"+ location +"%")).all() 
        #elif location is None:
         #   info = Item.query.filter_by(price<=int(price)).all() 
        except:
            flash("sorry no room fits this criteria, please try again")
            room = Item.query.order_by(Item.id.desc()).limit(3).all()
        #if price and location is not None:
         #   info = Item.message.match("%"+ location +"%").all()  
        #elif price is None:
          #  info = Item.query.filter_by(Item.message.match("%"+ location +"%")).all() 
        #elif location is None:
         #   info = Item.query.filter_by(price<=int(price)).all() 
        return render_template('searchresult.html', room = room,search_form = search_form
)
############################################
# homepage route
@mainbp.route('/')
def index():
    search_form = searchForm()
    tag_line='Budget Accomadation: Cheap Sharehouse For Broke You!'
    room = Item.query.order_by(Item.id.desc()).limit(9).all()
    return render_template('homepage.html', room = room, search_form = search_form, tag_line=tag_line)

############################################
#item form route
@mainbp.route('/landlord')
def post():
    search_form = searchForm()
    if current_user.is_anonymous:
        return redirect('/login')
    else:
        print(current_user.name)

    tag_line="I'm the landlord"
    
    aform = itemForm()

    return render_template('index_reuse.html', tag_line=tag_line, search_form = search_form,aform=aform)


#item form route
@mainbp.route('/landlordlist')
def postitems():
    if current_user.is_anonymous:
        return redirect('/login')
    else:
        print(current_user.name)

    search_form = searchForm()
    tag_line="I'm the landlord"
    print(current_user.id)
    room = Item.query.filter(Item.user_id == current_user.id).order_by(Item.id.desc()).all()
    return render_template('landlordlist.html', room = room,search_form = search_form, tag_line=tag_line)

#information page/room information route
@mainbp.route('/landlorditem/<id>')
def landlorditem(id):
    if current_user.is_anonymous:
        return redirect('/login')
    else:
        print(current_user.name)

    search_form = searchForm()
    tag_line='Budget Accomadation: Cheap Sharehouse For Broke You!'
    info = Item.query.filter_by(id=id).first()  
    aform = itemForm(obj=info)
    biditem = Bid.query.filter_by(item_id = id).all()
    return render_template('landlorditem.html',biditem=biditem, search_form = search_form,aform=aform, tag_line=tag_line, info=info)
@mainbp.route('/sold/<id>')
def itemsold(id):
    #Delete Details
     Item.query.filter_by(id=id).first().sold = True
     db.session.commit()

    #return to main page
     return redirect('/landlordlist')
@mainbp.route('/remove/<id>')
def itemdelete(id):
    #Delete Details
     Item.query.filter_by(id=id).delete()
     db.session.commit()

    #return to main page
     return redirect('/landlordlist')


#information page/room information route
@mainbp.route('/sharehouse/<id>')
def sharehousePage(id):
    search_form = searchForm()
    info = Item.query.filter_by(id=id).first()  
    tag_line='Budget Accomadation: Cheap Sharehouse For Broke You!'
    name = Item.query.filter_by(id=id).first()  
    return render_template('roomInfo.html', search_form = search_form,tag_line=tag_line, info=info)

#############################################
#         D A T A B A S E - P A T H         #                
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
                user_id = current_user.id,
                sold = 1
                )

    #add the object to the db session
    db.session.add(newitem)
    
    #commit to the database
    db.session.commit()
    flash('Successfully created new travel destination', 'success')
    print('Successfully created new room info', 'success')
    return redirect(url_for('main.index'))


#############################################
#           U P D A T E - I T E M           #                
#############################################
#fetch item form and insert it to database

@mainbp.route('/update', methods = ['GET','POST'])
def update_item():
  id =  request.args.get('id', None)
  aform = itemForm()
  if aform.validate_on_submit():
    db_file_path=check_upload_file(aform)
    print(db_file_path)
    # a simple function: doesnot handle errors in file types and file not being uploaded
    
    # if the form was successfully submitted, access the values in the form data
    
    #insert item into database
    #add the object to the db session
    
    
    data = {Item.title:aform.title.data, 
                Item.description:aform.description.data,
                Item.image: db_file_path,
                Item.price: aform.price.data,
                Item.address:aform.address.data,
                Item.water : aform.water.data,
                Item.wifi : aform.wifi.data,
                Item.eletricity : aform.eletricity.data,
                Item.gas : aform.gas.data,
                Item.mobile : aform.mobile.data}
    db.session.query(Item).filter_by(id=id).update(data)
    
    #commit to the database
    db.session.commit()
    flash('Successfully created new travel destination', 'success')
    print('Successfully created new room info', 'success')
    return redirect('/landlordlist')




#############################################
#           ADD BID                         #
#############################################
@mainbp.route('/bid/<id>', methods = ['GET','POST'])
def place_bid(id):
    newbid=Bid(date=datetime.datetime.now(),
            item_id=id,
            user_name=current_user.name,
            mobile=current_user.mobile,
            )
    print(datetime.datetime.now(),id,current_user.id)
    db.session.add(newbid)
    db.session.commit()
    flash('Successfully bid on the item','success')
    print('Successfully bid on item','success')
    return redirect(url_for('main.index'))
#############################################
#           R E G I S T R A T I O N         #                
#############################################

@mainbp.route('/reg')
def reg():
    registerform = RegestierForm()
    search_form = searchForm()
    return render_template('register.html',search_form = search_form,registerform = registerform)

@mainbp.route('/register', methods = ['POST'])
def register():
    registerform = RegestierForm()
    if registerform.validate_on_submit():
        print('Register Form Submitted')
        #get username,password and email from the form
        username = registerform.user_name.data
        pass_word = registerform.password.data
        email = registerform.email.data
        mobile = registerform.mobile.data


        #create password hash, salted for security
        hashWord = generate_password_hash(pass_word+username)

        #create a new user account
        try: 
            newUser = User(name=username, emailid=email, mobile=mobile, password_hash=hashWord)
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('main.login'))
        except:
            flash("Looks like the user name had been used, try another one!" )
            print("username duplcated")
            return redirect(url_for('main.reg'))

#############################################
#                 L O G I N                 #                
#############################################
#initialize login management
login_manager = LoginManager()

#create name of the login function that lets users login
login_manager.login_view ='auth.login'

#create a user load in function that goes by userID
@login_manager.user_loader
def load_user(user_id):
    return User.get(u1)

#routing for login
@mainbp.route('/login')
def login():
    login_form = LoginForm()
    search_form = searchForm()
    return render_template('login.html',search_form = search_form, login_form = login_form)

#this is the login function
@mainbp.route('/log', methods = ['GET','POST'])
def log():
    login_form=LoginForm()
    error=None
    if(login_form.validate_on_submit()):
        username = login_form.user_name.data
        pass_word = login_form.pass_word.data
        u1 = User.query.filter_by(name = username).first()

        if u1 is None:
            error='Incorrect Username'
            flash(error)
            print(error)
        elif not check_password_hash(u1.password_hash,pass_word+username):
            error='Incorrect Password'
            flash(error)
            print(error)
        if error is None:
            print(u1)
            login_user(u1)
            print(u1)
            return redirect(url_for('main.index'))
        else:
            return redirect(url_for('main.login'))
            print(error)
           #create a login failed page

   # return redirect(url_for('main.index'))

@mainbp.route("/logout")
def logout():
    if current_user.is_anonymous:
        return redirect('/login')
    else:
        print(current_user)

    logout_user()
    return redirect(url_for('main.index'))