'''
For User and Post models
'''

from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    # The id column will be the primary key
    id = db.Column(db.Integer, primary_key=True)
    # The username column will be unique and nullable
    username = db.Column(db.String(20), unique=True, nullable=False)
    # The email column will be unique and nullable
    email = db.Column(db.String(120), unique=True, nullable=False) 
    # The image_file column will be unique and nullable
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    # The password column will be nullable
    password = db.Column(db.String(60), nullable=False)
    # The posts relationship will be created
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    # The id column will be the primary key
    id = db.Column(db.Integer, primary_key=True)
    # The title column will be nullable
    title = db.Column(db.String(100), nullable=False)
    # The date_posted column will be nullable
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    # The content column will be nullable
    content = db.Column(db.Text, nullable=False)
    # The user_id column will be the foreign key
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        print("within repr")
        return f"Post('{self.title}', '{self.date_posted}')"
