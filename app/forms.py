from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


 
class ContactForm(FlaskForm):
  name = StringField("Name", validators=[DataRequired('Please enter your name.')], render_kw={"placeholder": "Name"})
  email = StringField("Email", validators=[DataRequired('Please enter your email.'), Email('Please enter your email.')], render_kw={"placeholder": "Email"})
  subject = StringField("Subject", validators=[DataRequired('Please include a subject.')], render_kw={"placeholder": "Subject"})
  message = TextAreaField("Message", validators=[DataRequired('Please enter a message.')], render_kw={"placeholder": "Message", "cols": "30", "rows": "7"})
  submit = SubmitField("Send")




