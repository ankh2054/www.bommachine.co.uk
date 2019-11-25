from flask import Flask


# To start using gunicorn - gunicorn app:app
app = Flask(__name__)
# Loads the config.py file
app.config.from_pyfile('config.py', silent=True)


# Imports app/routes.py
from app import routes
