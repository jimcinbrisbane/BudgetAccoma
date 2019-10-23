from flask import Blueprint,render_template, redirect, url_for, request
from flask_login import UserMixin, LoginManager
from .models import User, Item, Bid
from .forms import RegestierForm, LoginForm, itemForm, searchForm
import datetime
from . import db
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
from . import create_app


#initialize login management
login_manager = LoginManager()

#create name of the login function that lets users login
login_manager.login_view ='auth.login'

#create a user load in function that goes by userID
@login_manager.user_loader

#this is the login function




def load_user(user_id):
    return User.query.get(int(user_id))

# - store the user information - #


#if its okay, set the logged in user
login_user(user)