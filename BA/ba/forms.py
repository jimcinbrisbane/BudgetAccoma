from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField, PasswordField, IntegerField, validators, FileField, BooleanField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed



# register form
class RegestierForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired()] )
    email = StringField('Email Address', validators=[InputRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField("Submit")



# place login
class LoginForm(FlaskForm):
    user = StringField('User', validators=[InputRequired()] )
    login = StringField('Password', validators=[InputRequired()])
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
