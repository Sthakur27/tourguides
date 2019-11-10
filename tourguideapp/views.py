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
    u = User.query.filter_by(email=user_id).first()
    return u

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
        user = load_user(email)
        #check if user exists and password matches
        if user and password == user.password:
            flash('Logged in successfully.', 'bg-success')
            login_user(user)
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
        return render_template('form.html', action='/usersignup', form=form)

@app.route("/tourguidesignup", methods=["GET", "POST"])
def tourguidesignup():
    form = TourGuideForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        flash('User successfully added', 'bg-success')
        return redirect(url_for('home'))
    else:
        '''
        for field in form.errors:
            for error in form.errors[field]:
                flash('{}:{}'.format(field, error), 'bg-danger')
        '''
        return render_template('form.html', action='/tourguidesignup', form=form)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/search',methods=['GET','POST'])
@login_required
def search():
    form = SearchForm(request.form)
    if request.method=='POST':
         try:
             #get the pool specified
             pool=Pool.query.filter_by(name=request.form['pool']).first()
             #get the users matching the username and password
             users=User.query.filter_by(username=request.form['username']).filter_by(password=request.form['password']).all()
             #check if any of those users are in the pool's userinfo
             user=None
             pool_users=pool.userinfo.split(' ')
             for u in users:
                  if(str(u.id) in pool_users):
                        user=u
             if(user):
                 #login the user and send to /poolinfo page
                 if(str(user.id) in pool.userinfo.split(' ')):
                      session['currentuser']=user.id
                      session['logged_in']=True
                      return redirect("/poolinfo/"+str(pool.id))
                 #even though error, I chose to use bg-success color(green) because it contrasts with the website background color(red)
                 flash("User not in Group",'bg-success') 
             else:
                 flash("User not Found",'bg-success')
             return redirect('/login')
         except:
             flash("Login Error",'bg-success')
             return redirect('/login')
         return redirect("/login")
    return render_template('search.html')


        



