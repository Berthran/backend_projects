from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
     # All form fields will be imported classes
     username = StringField('Username',
                            validators=[DataRequired(),
                                        Length(min=2, max=20)])
     email = StringField('Email',
                         validators=[DataRequired(),
                                     Email()])
     password = PasswordField('Password',
                              validators=[DataRequired()])
     confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
     submit = SubmitField('Sign Up')

     def validate_username(self, username):
          # Checks if username is exists
          user = User.query.filter_by(username=username.data).first()
          if user:
               raise ValidationError("That username is taken please choose a different one")
          
     def validate_email(self, email):
          # Checks if email is exists
          user = User.query.filter_by(email=email.data).first()
          if user:
               raise ValidationError("That email is taken please choose a different one")


class LoginForm(FlaskForm):
     email = StringField('Email',
                         validators=[DataRequired(),
                                     Email()])
     password = PasswordField('Password',
                              validators=[DataRequired()])
     remember = BooleanField('Remember Me')
     submit = SubmitField('Login')