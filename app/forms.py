from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


 
class ContactForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired('Please enter your name.')])
  email = StringField("Email", validators=[DataRequired('Please enter your email.'), Email('Please enter your email.')])
  subject = StringField("Subject", validators=[DataRequired('Please include a subject.')])
  message = TextAreaField("Message", validators=[DataRequired('Please enter a message.')])
  submit = SubmitField("Send")




