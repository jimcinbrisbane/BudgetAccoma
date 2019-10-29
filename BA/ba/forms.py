from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField, PasswordField, IntegerField, validators, FileField, BooleanField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed



# register form
class RegestierForm(FlaskForm):

    #get user data
    user_name = StringField('Username*', validators=[InputRequired()])
    mobile = IntegerField('mobile_number*', validators=[InputRequired()])
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

    title = StringField('Fancy Title', validators=[InputRequired()],render_kw={"placeholder": "Get an eye tracking title"})
    description = StringField('Room Description', validators=[InputRequired()],render_kw={"placeholder": "What makes your properity stand out?"})
    image = FileField('Image (png,jpeg,jpg only)', validators=[FileRequired(),FileAllowed({ 'jpg', 'JPG', 'png', 'PNG'}, 'Images only!')])
   
    price = IntegerField('Price Per Week', validators=[InputRequired()], render_kw={"placeholder": "140"})
    address = StringField('Address and Postcode', validators=[InputRequired()],render_kw={"placeholder": "2 George Street, Brisbane, 4000"})
    mobile = IntegerField('Contact Number', validators=[InputRequired()])
    water = BooleanField('Water Included?')
    wifi = BooleanField('WiFi Included?')
    eletricity = BooleanField('Power Bill Included?')
    gas = BooleanField('Gas Included?')

    submit= SubmitField("Create")

# Search form
class searchForm(FlaskForm):
    price=StringField('Max Price In Your Range',validators=[InputRequired()], render_kw={"placeholder": "$100/w"})
    location=StringField('Enter a Postcode',validators=[InputRequired()],render_kw={"placeholder": "4000"})
    submit = SubmitField('Search')