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

search_locations = [(None,'Any')] + [(x,x) for x in locations]
search_times = [(None,'Any')] + [(x,x) for x in times]
search_activities = [(None,'Any')] + [(x,x) for x in activities]

class SearchForm(FlaskForm):
    location = SelectField('Location)',choices=search_locations)
    time = SelectField('Time',choices=search_times)
    activity = SelectField('Activity',choices=search_activities)
    submit = SubmitField("Search")

class TourGuideForm(FlaskForm):
    name = StringField("Name")
    email=StringField("Email:  example@gmail.com")
    password = PasswordField('Password')
    locations = SelectMultipleField('Location(s)',choices=[(x,x) for x in locations])
    times = SelectMultipleField('Time(s)',choices=[(x,x) for x in times])
    activities = SelectMultipleField('Activities(s)',choices=[(x,x) for x in activities])
    submit = SubmitField('Add Tour Guide')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[Email()])
    password = PasswordField('Password')
    submit = SubmitField('Login')
    
class UserForm(FlaskForm):
    name = StringField("Name")
    email=StringField("Email:  example@gmail.com")
    password = PasswordField('Password')
    submit = SubmitField('Add User')
    
class EditUserForm(UserForm):
    delete=SubmitField('Delete')

