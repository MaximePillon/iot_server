from flask import request, redirect, url_for, flash, session, render_template, Blueprint
from app import db
from src.forms.UserForm import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from src.models.UserModel import User
from flask_login import LoginManager, UserMixin, login_user, logout_user, \
    current_user
from werkzeug.security import generate_password_hash
import flask_login


user = Blueprint('user', __name__)


@user.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        # if user is logged in we get out of here
        return redirect(url_for('front.index'))

    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('Email already exists.')
            return redirect(url_for('register'))

        # add new user to the database
        user = User(firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=generate_password_hash(form.password.data),
                    status="active")
        db.session.add(user)
        db.session.commit()

        # redirect with success
        session['email'] = user.email
        return redirect(url_for('front.index'))
    return render_template('register.html', form=form)


@user.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return render_template(url_for('front.index'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_password(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('user.login'))

        login_user(user)
        flash('You are logged in')
        return redirect(url_for('front.index'))
    return render_template('login.html', form=form)


@user.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('front.index'))
