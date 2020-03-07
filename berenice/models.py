from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from berenice import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    pass
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    location_id = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    loc_items = db.relationship('Item', backref='location', lazy=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    pass
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Item(db.model):
    pass
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(16), nullable=False)
    model = db.Column(db.String(16), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    bodyType = db.Column(db.String(8), nullable=False)
    destId = db.Column(db.Integer, db.ForeignKey(
        'user.location_id'), nullable=False)
    shipStatus = db.Column(db.String(16), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)

    def __repr__(self):
        return f"Item('\n...{self.make}'\n\t '{self.model}' \n\t '{self.year}')"

