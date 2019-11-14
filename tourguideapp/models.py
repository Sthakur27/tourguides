#creates an SQLalchemy ORM mapping of database tables
from sqlalchemy import *
from sqlalchemy import Column, Integer, String
from tourguideapp import db
from flask_login import UserMixin
########################################################################
class User(db.Model, UserMixin):
    __tablename__="users" 
    id = db.Column(db.Integer, db.Sequence('user_seq',start=1,increment=1), primary_key=True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(45))
    password = db.Column(db.String(25))
    isGuide = db.Column(db.Integer)
    is_authenticated = True
    is_active = True
    is_anonymous = False
    def get_id(self):
        return str(self.id)

class Option(db.Model):
    __tablename__="options"
    id = db.Column(db.Integer,db.Sequence('option_seq',start=1,increment=1), primary_key=True)
    guide_id = db.Column(db.Integer)
    detail = db.Column(db.String(100))
    def __init__(self,gid,det):
        self.guide_id = gid
        self.detail = det

