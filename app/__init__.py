from flask import Flask
from config import Config

# To start using gunicorn - gunicorn app:app
app = Flask(__name__)
# Loads the config.py file
app.config.from_object(Config)


# Imports app/routes.py
from app import routes
