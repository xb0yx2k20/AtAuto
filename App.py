from flask import Flask, render_template, request, redirect, url_for
from models import Car, CarPhoto, db
from adminView import CarView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


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





admin = Admin(app)
admin.add_view(CarView(Car, db.session))
#admin.add_view(AlbumView(Car, db.session))
admin.add_view(ModelView(CarPhoto, db.session))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
