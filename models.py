from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    # define the name of the table
    __tablename__ = "user"

    # define the columns of the table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username
