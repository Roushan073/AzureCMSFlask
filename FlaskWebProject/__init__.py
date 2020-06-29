"""
The flask application package.
"""
from logging.handlers import RotatingFileHandler
import logging
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Below line will ensure redirect_uri to use https scheme when deployed to App Service
app.wsgi_app = ProxyFix(app.wsgi_app)

# TODO: Add any logging levels and handlers with app.logger
handler = RotatingFileHandler('flask-cms.log', maxBytes=0, backupCount=1)
app.logger.setLevel(logging.INFO)
app.logger.addHandler(handler)

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
