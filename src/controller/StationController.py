from flask import redirect, url_for, flash, session, render_template, Blueprint
from src.models.StationModel import load_all_station
from flask_login import login_required

station = Blueprint('station', __name__)


@station.route('/view', methods=['GET'])
@login_required
def view():
    stations = load_all_station()
    return render_template('station.html', stations=stations)


@station.route('/details', methods=['GET'])
@login_required
def details(to_details):
    return render_template('detailed_view.html', station=to_details)
