from flask_login import login_required
from flask import Flask, jsonify, render_template, Blueprint


front = Blueprint('front', __name__)


@front.route('/weather_view')
@login_required
def weather_view():
    return 'this is the weather view'


@front.route('/')
def index():
    return render_template('index.html')


@front.route('/admin')
@login_required
def weather_station_edit(id):
    return 'Admin home page ' + id

