from flask import redirect, url_for, flash, session, render_template, Blueprint, request
from src.models.StationModel import load_all_station, load_station, load_voltage
from flask_login import login_required

station = Blueprint('station', __name__)


@station.route('/view', methods=['GET'])
@login_required
def view():
    stations = load_all_station()
    return render_template('station.html', stations=stations)


@station.route('/details', methods=['GET'])
@login_required
def details():
    base = load_station(request.args.get('station'))
    voltage = load_voltage(request.args.get('station'))
    return render_template('detailed_view.html', station=base, voltage=voltage)
