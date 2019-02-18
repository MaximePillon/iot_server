from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Length, EqualTo


class RegisterForm(FlaskForm):
    """Registration form."""
    firstname = StringField('firstname', validators=[Required(), Length(1, 255)])
    lastname = StringField('lastname', validators=[Required(), Length(1, 255)])
    email = StringField('email', validators=[Required(), Length(1, 255)])
    password = PasswordField('Password', validators=[Required()])
    password_again = PasswordField('Password again',
                                   validators=[Required(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """Login form."""
    email = StringField('email', validators=[Required(), Length(1, 64)])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')
