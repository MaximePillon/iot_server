from app import db


class BaseModel(db.model):
    """Equivalent to interface for all the project model"""
    __abstract__ = True

# can here develop general models
