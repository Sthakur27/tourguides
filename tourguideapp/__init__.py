from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
app=Flask(__name__)
app.secret_key = 'tgrulz'
app.config.from_pyfile('config.py')
Bootstrap(app)
app.config['SQLALCHEMY_POOL_RECYCLE'] = 280
db = SQLAlchemy(app)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
from tourguideapp.views import *
