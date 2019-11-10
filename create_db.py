#this file creates the sqlite database if it doesn't already exist
#do not run if 'ss.db' is already in ssapp/
from tourguideapp.settings import SQLALCHEMY_DATABASE_URI
from tourguideapp.settings import SQLALCHEMY_MIGRATE_REPO
from tourguideapp import db
import os.path
db.create_all()

