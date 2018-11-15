from flask_simplelogin import login_required
from flask import Flask, jsonify, render_template, request
from app import db
from flask_sqlalchemy import SQLAlchemy
from src.models.UserModel import UserModel


@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    if not db.session.query(UserModel).filter(UserModel.email == email).count()
        user = UserModel(request.form['firstname'],
                        request.form['lastname'],
                        email,
                        request.form['password'],
                        "customer")
        db.session.add(user)
        db.session.commit()
        return 'Success user creation'
    return 'cant create an user'

