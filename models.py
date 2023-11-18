from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import CheckConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(4), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artist = db.relationship('Artist', backref=db.backref('albums', lazy=True))

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    length = db.Column(db.String(4), nullable=False)
    track_number = db.Column(db.Integer, nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    album = db.relationship('Album', backref=db.backref('songs', lazy=True))

class Car(db.Model):
    __tablename__ = 'cars'
    CarID = db.Column(db.Integer, primary_key=True)
    Mark = db.Column(db.String)
    Model = db.Column(db.String)
    Year = db.Column(db.Integer, nullable=False)
    Engine = db.Column(db.String, nullable=False)
    hp = db.Column(db.Integer)
    odo = db.Column(db.Integer,  nullable=True)
    GearBox = db.Column(db.String, nullable=False)
    photos = db.relationship('CarPhoto', backref='car', lazy=True)
    ownsNum = db.Column(db.Integer,  nullable=True)
    price = db.Column(db.String)

class CarPhoto(db.Model):
    __tablename__ = 'car_photos'
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.CarID'))
    url = db.Column(db.String(200))
