from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField, PasswordField, IntegerField, validators, FileField, BooleanField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed



# register form
class RegestierForm(FlaskForm):

    #get user data
    user_name = StringField('Username*', validators=[InputRequired()])
    email = StringField('Email Address*', validators=[InputRequired()])
    password = PasswordField('Enter a Password*', validators = [InputRequired()])
    confirm = PasswordField('Confirm Password*', validators=[InputRequired()])
    submit = SubmitField("Submit")




# login form
class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[InputRequired()] )
    pass_word = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField("Submit")

# item form
class itemForm(FlaskForm):

    title = StringField('Fancy Title', validators=[InputRequired()])
    description = StringField('Room Description', validators=[InputRequired()])
    image = FileField('image', validators=[FileRequired(),FileAllowed({ 'jpg', 'JPG', 'png', 'PNG'}, 'Images only!')])
   
    price = IntegerField('Price', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    mobile = IntegerField('Contact Number', validators=[InputRequired()])
    water = BooleanField('Water Included?')
    wifi = BooleanField('WiFi Included?')
    eletricity = BooleanField('Power Bill Included?')
    gas = BooleanField('Gas Included?')

    submit= SubmitField("Create")

class searchForm(FlaskForm):
    price=StringField('Price',validators=[InputRequired])
    location=StringField('Location',validators=[InputRequired])
    submit = SubmitField('Search')