from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

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
    CarID = db.Column(db.Integer, primary_key=True)
    Mark = db.Column(db.String)
    Model = db.Column(db.String)
    Year = db.Column(db.Integer, nullable=False)
    Engine = db.Column(db.String, nullable=False)
    hp = db.Column(db.Integer)
    GearBox = db.Column(db.String, CheckConstraint("GearBox IN ('at', 'mt', 'svt')"), nullable=False)
    #odo = db.Column(db.Integer)