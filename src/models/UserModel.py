from app import db

class UserModel(BaseModel):
    """Model for the user table"""
    __tablename__ = 'user'

    def __init__(self, firstname, lastname, email, password, status):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.status = status

    def __repr__(self):
        return '<E-mail %r>' % self.email

    id = db.Column('user_id', db.Integer, primary_key=True)
    firstname = db.Column('firstname', db.String(255))
    lastname = db.Column('lastname', db.String(255))
    email = db.Column('email', db.String(255), unique=True)
    password = db.Column('password', db.String)
    status = db.Column('status', db.String)

