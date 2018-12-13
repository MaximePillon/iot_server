from app import db
from sqlalchemy.orm import relationship

class Sensor(db.Model):
    """Model for the sensor table"""
    __tablename__ = 'sensor'

    id = db.Column('sensor_id', db.Integer, primary_key=True)
    voltage = db.Column('voltage', db.Integer)
    is_activated = db.Column('is_activated', db.Boolean)
    data_type = db.Column('data_type', db.String(100))
    name = db.Column('name', db.String(100))
    station_id = db.Column(db.Integer, db.ForeignKey('station.station_id'))
    station = relationship("Station", back_populates="sensors")

    def __init__(self, **kwargs):
        super(Sensor, self).__init__(**kwargs)

    def __repr__(self):
        return '<Id %r>' % self.id
