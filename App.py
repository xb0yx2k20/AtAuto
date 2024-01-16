from flask import Flask, render_template, request, redirect, url_for
from models import Car, CarPhoto, db
from adminView import CarView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import flask_login


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1029384756'

db.init_app(app)


@app.route('/cars')
def cars():
    cars_list = Car.query.all()    
    return render_template('cars.html', cars=cars_list)


@app.route('/cars/search', methods=['GET'])
def cars_search():
    search_query = request.args.get('search', '')
    if search_query:
        cars_list = Car.query.filter(Car.Mark.ilike(f"%{search_query}%")).all()
    else:
        cars_list = Car.query.all()
    print(cars_list)
    return render_template('cars.html', cars=cars_list)


@app.route('/cars/<car_inf>/<car_id>', methods=['GET'])
def car_info(car_inf, car_id):
    car = Car.query.filter_by(CarID=car_id).first()
    return render_template('car_info.html', carInfo=car)


@app.route('/adminLog/', methods=['POST', 'GET'])
def admin_log():
    return render_template('admin_log.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
