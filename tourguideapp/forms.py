from tourguideapp.models import User,Option
from wtforms_alchemy import ModelForm, ModelFormField
import wtforms_alchemy
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, RadioField, StringField, SelectField, SelectMultipleField, FloatField, \
    BooleanField, FieldList, FormField, TextAreaField, PasswordField

from wtforms_components import IntegerField
from wtforms.fields.html5 import DateField, EmailField
from wtforms_alchemy.fields import QuerySelectField

from datetime import datetime, timedelta, date
from wtforms_components import Email
from wtforms.validators import Required, Optional, NumberRange

locations = ['Thailand','New York']
times = ['lunch','evening']
activities = ['art','nature','shopping']

class SearchForm(FlaskForm):
    locations = SelectMultipleField('Location(s)',choices=[(x,x) for x in locations])
    times = SelectMultipleField('Time(s)',choices=[(x,x) for x in times])
    activities = SelectMultipleField('Activities(s)',choices=[(x,x) for x in activities])
    submit = SubmitField("Search")

class TourGuideForm(FlaskForm):
    email=StringField("Email:  example@gmail.com")
    password= StringField("Password")
    locations = SelectMultipleField('Location(s)',choices=[(x,x) for x in locations])
    times = SelectMultipleField('Time(s)',choices=[(x,x) for x in times])
    activities = SelectMultipleField('Activities(s)',choices=[(x,x) for x in activities])
    submit = SubmitField('Add Tour Guide')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email()])
    password = PasswordField('Password')
    submit = SubmitField('Login')
    
class UserForm(FlaskForm):
    email=StringField("Email:  example@gmail.com")
    password= StringField("Password")
    submit = SubmitField('Add User')
    
class EditUserForm(UserForm):
    delete=SubmitField('Delete')

