from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField, PasswordField, IntegerField, validators, FileField, BooleanField
from wtforms.validators import InputRequired
ALLOWED_FILE= { 'jpg', 'JPG', 'png', 'PNG'}

# register form
class RegestierForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired()] )
    email = StringField('Email Address', validators=[InputRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


# place login
class LoginForm(FlaskForm):
    user = StringField('Title', validators=[InputRequired()] )
    login = StringField('', validators=[InputRequired()])
    submit = SubmitField("Submit")

#4
class itemForm(FlaskForm):
    title = StringField('Fancy Title', validators=[InputRequired()])
    description = StringField('Room Description', validators=[InputRequired()])
    image= FileField('Room Image'),
    #FileAllowed(ALLOWED_FILE, message='support jpg and png')])    
    price = IntegerField('price', validators=[InputRequired()])
    address = StringField('Address', validators=[InputRequired()])
    mobile = IntegerField('Contact Number', validators=[InputRequired()])
    water = BooleanField('Water Included?')
    wifi = BooleanField('WiFi Included?')
    eletricity = BooleanField('Power Bill Included?')
    gas = BooleanField('Gas Included?')
    submit= SubmitField("Create")
