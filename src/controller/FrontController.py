from flask_simplelogin import login_required
from flask import Flask, jsonify, render_template

@app.route('/weather_view')
@login_required
def weather_view():
    return 'this is the weather view'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/admin')
@login_required(must=[be_admin])
def weather_station_edit(id):
    return 'Admin home page ' + id

