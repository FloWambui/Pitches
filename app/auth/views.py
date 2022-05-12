from click import password_option
from flask import render_template,redirect,url_for, flash, request
from . import auth
from ..models import User
from .forms import LoginForm,RegistrationForm
from .. import db
from flask_login import  login_user, logout_user, login_required
from ..email import  mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        
        login_user(user,login_form.remember.data)
        return redirect('/')

        flash('Invalid username or Password')

    title = "The Pitch Hub"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out')
    return redirect(url_for('auth.login'))


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        #mail_message("Thank you for registering with the Pitch Hub.","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)



