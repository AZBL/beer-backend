from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firebase_uid = db.Column(db.String(255), unique=True,
                             nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)

    beers = relationship("Beer", backref="user_owner")

    def __repr__(self):
        return f"User('{self.first_name}', '{self.last_name}', '{self.email}')"


class Beer(db.Model):

    __tablename__ = 'beers'

    id = db.Column(db.Integer, primary_key=True)
    brewery = db.Column(db.String(50))
    name = db.Column(db.String(100), nullable=False)
    abv = db.Column(db.Float)
    style = db.Column(db.String(75))
    comments = db.Column(db.String(500))
    rating = db.Column(db.Float)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    owner = relationship("User")


class BeerSchema(ma.Schema):
    class Meta:
        fields = ['id', 'brewery', 'name', 'abv',
                  'style', 'comments', 'rating']


beer_schema = BeerSchema()
beers_schema = BeerSchema(many=True)
