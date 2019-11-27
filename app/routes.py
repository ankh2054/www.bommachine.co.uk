from flask import render_template, request, flash
from app import app
# Imports ContactForm from app/forms.py
from app.forms import ContactForm
import requests
# Import additional functions from functions.py
from app.functions import btcprice



# Mailgun API for sending messages
mailgun_api = 'key-88828829f7b4e5434d674a1db2182d3b'
mailgun_url = 'https://api.mailgun.net/v3/sandbox773b6264f055401b8ae8e10b51aa68d2.mailgun.org/messages'




@app.route('/')
@app.route('/index')
def index():
     price = btcprice()
     return render_template('index.html', title='Home', price=price)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
     form = ContactForm()
     if request.method == 'POST':
        if form.validate() == False:
          flash('All fields are required.')
          return render_template('contact.html', form=form)
        else:
          # Post request to mailgun API
          requests.post(mailgun_url, 
                auth=("api", mailgun_api), 
                data={"from": "charles@bommachine.co.uk",
                "to": form.email.data,
                "subject": form.subject.data, 
                "text":form.message.data}
          )
          return render_template('contact.html', success=True)
 
     elif request.method == 'GET':
      return render_template('contact.html', form=form, title='Contact Us')


@app.route('/about')
def about():
     return render_template('about.html', title='About')



