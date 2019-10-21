from flask import Blueprint, render_template, redirect, url_for, request
from .models import User, Item, Bid
from .forms import RegestierForm
from .forms import LoginForm
from .forms import itemForm
from .forms import searchForm
from .models import User
import datetime
from . import db
from werkzeug.utils import secure_filename
import os
from . import create_app

#initialize login management
login_manager = LoginManager()

#create name of the login function that lets users login
login_manager.init_app(app)

#create a user load in function that goes by userID
@login_manager.user_loader

def load_user(user_id):
    return User.query.get(init(userid))

# - store the user information - #

#if its okay, set the logged in user
login_user(logged_user)

#login supourt to a url route
@mainbp.route('/')
@login_required

#define the logout
@bp.route('/logout')
def logout():
    logout_user()
    return 'Successfully logged out the user'    

#Following the Authentication Blueprint
bp = Blueprint('auth', __name__)
@bp.route('/login', methods=['GET','POST'])
def login():
    loginForm = LoginForm()
    return render_template('user.html', form=loginForm,
    heading='Login')

#this is the login function
@mainbp.route('/log', methods = ['GET','POST'])
def log():
    login_form=LoginForm()
    error=None
    if(login_form.validate_on_submit()):
        username =login_form.user_name.data
        pass_word =login_form.pass_word.data
        u1 =User.query.filter_by(name = user_name).first()

        if u1 is None:
            error='Incorrect Username'
        elif not check_password_hash(u1.check_password_hash,password):
            error='Incorrect Password'
        if error is None:
            return redirect(url_for('main.index'))
        else:
            print(error)
            flash(error)
    return render_template('',login_form=login_form,heading='Login')