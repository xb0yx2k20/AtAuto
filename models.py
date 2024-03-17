from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin
from sqlalchemy import CheckConstraint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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
    url = db.Column(db.LargeBinary)
    photo = db.Column(db.LargeBinary)


class adminLog(UserMixin, db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
