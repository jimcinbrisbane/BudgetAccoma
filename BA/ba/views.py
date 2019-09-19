from flask import Blueprint,render_template, redirect, url_for, request
from .models import room,Destination
from .forms import ContactForm
from .forms import CommentForm
from .forms import DestinationForm

from . import db

mainbp = Blueprint('main',__name__)

@mainbp.route('/')
def index():
    tag_line='You need a vacation'
    rooms = get_room_list()
    form=ContactForm()
    form2=CommentForm() 
    aform = DestinationForm()

    return render_template('index_reuse.html', tag_line=tag_line,
                    form=form, form2=form2, rooms=rooms, aform=aform)
#@mainbp.route('/<id>') 
#def show(id): 
  #destination = Destination.query.filter_by(id=id).first()  
  #cform = cokForm()
 # return render_template('user.html', destination=destination)
@mainbp.route('/<id>') 
def show(id): 
  destination = Destination.query.filter_by(id=id).first()  
  return render_template('destinations/u.html', destination=destination)

@mainbp.route('/create', methods = ['GET', 'POST'])
def create():
  aform = DestinationForm()
  if aform.validate_on_submit():
    # if the form was successfully submitted
    # access the values in the form data
    destination = Destination(name=aform.name.data, 
                description=aform.description.data,
                image=aform.image.data,
                currency=aform.currency.data)
    # add the object to the db session
    db.session.add(destination)
    # commit to the database
    db.session.commit()

    #flash('Successfully created new travel destination', 'success')
    print('Successfully created new travel destination', 'success')
    return redirect(url_for('main.index'))

@mainbp.route('/contact', methods=['GET','POST'])
def create_contact():
     form = ContactForm()
     if form.validate_on_submit():
          print("Form has been submitted successfully")
          print(request.form['user_name'])
     return redirect(url_for('main.index'))

@mainbp.route('/comment', methods=['POST'])
def create_comment():
     form2 = CommentForm()
     if form2.validate_on_submit():
          print("Form has been submitted successfully")
          print(request.form['comment'])
     return redirect(url_for('main.index'))



def get_room_list():
    brisbane_room = room('Brisbane', 'brisbane.jpg',
    'As the capital of the Sunshine State, we are blessed with idyllic subtropical weather all year round.')

    sydney_room = room('Sydney', 'sydney.jpg',
    'From splendid Sydney Harbour, idyllic beaches and great national parks, to the marvellous creativity of the Sydney Opera House, dazzling entertainment and fascinating heritage, discover all the things to do and see throughout the year.')

    melbourne_room = room('Melbourne', 'melbourne.jpg',
     'A packed agenda of food, wine, sports and arts is your introduction to the best of Melbourne – from its creative, exciting city centre, to its buzzing neighbourhood hubs.')

    hlist = list()
    hlist.append(brisbane_room)
    hlist.append(sydney_room)
    hlist.append(melbourne_room)
    return hlist