from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)

# Database configuration
POSTGRES = {
    'user': 'iot_user',
    'pw': 'iot_password',
    'db': 'iotproject',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://iot_user:iot_password@localhost/iotproject'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SECRET_KEY'] = 'top-secret'
app.secret_key = 'this-is-a-secret-key'


db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
lm = LoginManager(app)
db.create_all()
migrate = Migrate(app, db)

from src.controller.FrontController import front
from src.controller.UserController import user

app.register_blueprint(front, url_prefix='/')
app.register_blueprint(user, url_prefix='/')

if __name__ == '__main__':
    app.run()

