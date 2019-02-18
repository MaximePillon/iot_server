from app import db, lm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    """Model for the user table"""
    __tablename__ = 'users'

    id = db.Column('user_id', db.Integer, primary_key=True)
    firstname = db.Column('firstname', db.String(255))
    lastname = db.Column('lastname', db.String(255))
    email = db.Column('email', db.String(255), unique=True)
    password = db.Column('password', db.String)
    status = db.Column('status', db.String)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<E-mail %r>' % self.email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def verify_password(self, password):
        return check_password_hash(self.password, password)


@lm.user_loader
def load_user(user_id):
    """User loader callback for Flask-Login."""
    return User.query.get(int(user_id))
