from app import db
from sqlalchemy.orm import relationship
from src.models.SensorModel import Sensor

class Station(db.Model):
    """Model for the station table"""
    __tablename__ = 'station'

    id = db.Column('station_id', db.Integer, primary_key=True)
    city = db.Column('city', db.String(255))
    country = db.Column('country', db.String(255))
    postal_code = db.Column('postal_code', db.String(9))
    xlocation = db.Column('xlocation', db.String(10))
    ylocation = db.Column('ylocation', db.String(10))
    sensors = relationship("Sensor", back_populates="station")

    def __init__(self, **kwargs):
        super(Station, self).__init__(**kwargs)

    def __repr__(self):
        return '<Id %r>' % self.id


def load_station(station_id):
    """load a station"""
    return Station.query.get(int(station_id))


def load_all_station():
    """load every station"""
    return Station.query.all()
