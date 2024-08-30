# Initialize application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ad931a65cc99980ea69e0d34a308df47'

# The database URI that should be used for the connection.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creates an instance of the SQLAlchemy class
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes