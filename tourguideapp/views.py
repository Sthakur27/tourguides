#provides backends for each url
from flask import request, redirect, render_template, url_for, \
    stream_with_context, \
    flash, send_from_directory

from tourguideapp.models import *
from tourguideapp.forms import *
from tourguideapp import app, db, login_manager
from flask import request,session,abort
from flask_login import LoginManager, login_user, login_required
import flask_login
import random
import urllib
import random
from flask_mail import Message

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/logout', methods=['GET','POST'])
def logout():
    flask_login.logout_user()
    return redirect(url_for('home'))

def redirect_dest():
    dest_url = request.args.get('next')
    if not dest_url:
        dest_url = url_for('home')
    return redirect(dest_url)

@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login',next=request.path))

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        #check if user exists and password matches
        if user and password == user.password:
            print(user.id)
            user = load_user(user.id)
            print(login_user(user))
            flash('Logged in successfully.', 'bg-success')
            return redirect_dest()
        else:
            flash('Wrong login', 'bg-danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route("/usersignup", methods=["GET", "POST"])
def usersignup():
    form = UserForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        flash('User successfully added', 'bg-success')
        return redirect(url_for('home'))
    else:
        for field in form.errors:
            for error in form.errors[field]:
                flash('{}:{}'.format(field, error), 'bg-danger')
        return render_template('login.html', action='/usersignup', form=form)

@app.route("/tourguidesignup", methods=["GET", "POST"])
def tourguidesignup():
    form = TourGuideForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        user.isGuide = 1
        db.session.flush()
        affiliate_data = form.locations.data + form.times.data + form.activities.data
        for ad in affiliate_data:
            print(ad)
            o = Option(user.id,ad)
            db.session.add(o)
        db.session.commit()
        flash('User successfully added', 'bg-success')
        return redirect(url_for('home'))
    else:
        for field in form.errors:
            for error in form.errors[field]:
                flash('{}:{}'.format(field, error), 'bg-danger')
        return render_template('form.html', action='/tourguidesignup', form=form)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/search',methods=['GET','POST'])
@login_required
def search():
    form = SearchForm(request.form)
    if request.method=='POST':
        users = User.query.filter_by(isGuide=1).all()
        loc = form.location.data
        time = form.time.data
        activity = form.activity.data
        print(users)
        for i in range(len(users)-1,-1,-1):
            flag = False
            if(loc != 'None' and not flag):
                option = Option.query.filter_by(guide_id = users[i].id).filter_by(detail = loc).first()
                if not option:
                    flag = True
            if(time != 'None' and not flag):
                option = Option.query.filter_by(guide_id = users[i].id).filter_by(detail = time).first()
                if not option:
                    flag = True
            if(activity != 'None' and not flag):
                option = Option.query.filter_by(guide_id = users[i].id).filter_by(detail = activity).first()
                if not option:
                    flag = True
            if flag:
                del(users[i])
        print(users)
        #return render_template('form.html', action='/search', form=form)      
        return render_template('searchresults.html',users=users)
    else:
        return render_template('form.html', action='/search', form=form)


        



