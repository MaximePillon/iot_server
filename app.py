from flask import Flask
from flask_simplelogin import SimpleLogin
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy()

#todo
# Database configuration
POSTGRES = {
    'user': 'username',
    'pw': 'password',
    'db': 'iotproject',
    'host': 'localhost',
    'port': '5432',
}
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

# Login configuration
app.config['SECRET_KEY'] = 'this-is-a-secret-key'

messages = {
    'login_success': 'Successfully logged in',
    'login_failure': 'No user corresponding to inserted data',
    'is_logged_in': 'Actually logged in',
    'logout': 'Disconnected',
    'login_required': 'You has to be logged in',
    'access_denied': 'Access denied',
    'auth_error': 'Error'
}

db.init_app(app)
SimpleLogin(app, messages=messages)

if __name__ == '__main__':
    app.run()

