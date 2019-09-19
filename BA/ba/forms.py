from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,DateField
from wtforms.validators import InputRequired, Email

# forms example 1
class ContactForm(FlaskForm):
    user_name = StringField('Name', validators=[InputRequired()] )
    email = StringField('Email Address', validators=[InputRequired()])
    submit = SubmitField("Submit")

# 2
class CommentForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()] )
    comment = StringField('Comment', validators=[InputRequired()])
    submit = SubmitField("Submit")
#3
class DestinationForm(FlaskForm):
    name= StringField('Title', validators=[InputRequired()] )
    description= StringField('Title', validators=[InputRequired()] )
    image= StringField('Title', validators=[InputRequired()] )
    currency= StringField('Title', validators=[InputRequired()] )