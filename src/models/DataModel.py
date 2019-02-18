from app import db
from sqlalchemy.orm import relationship


class Data(db.Model):
    """Model for the data table"""
    ___tablename___ = 'data'

    id = db.Column('data_id', db.Integer, primary_key=True)
    value = db.Column('value', db.Integer)
    created_at = db.Column('created_at', db.TIMESTAMP)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.sensor_id'))
    sensor = relationship("Sensor", back_populates="data")

    def __init__(self, **kwargs):
        super(Data, self).__init__(**kwargs)

    def __repr__(self):
        return '<Id %r' % self.id
