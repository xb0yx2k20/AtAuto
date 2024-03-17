import bcrypt
from flask import Flask, Response, flash, render_template, request, redirect, url_for
from flask_admin.contrib import sqla
from models import Car, CarPhoto, adminLog, db
from adminView import CarView, LogView
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt 
from werkzeug.exceptions import HTTPException
from flask_basicauth import BasicAuth
from flask_bcrypt import check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1029384756'
db.init_app(app)
bcrypt = Bcrypt(app) 
basic_auth = BasicAuth(app)


with app.app_context():
    app.config['BASIC_AUTH_USERNAME'] = adminLog.query.first().login
    app.config['BASIC_AUTH_PASSWORD'] = adminLog.query.first().password

class MyModelView(sqla.ModelView):
    def is_accessible(self):
        auth = request.authorization
        if not auth or not bcrypt.check_password_hash(app.config['BASIC_AUTH_PASSWORD'], auth.password) or not bcrypt.check_password_hash(app.config['BASIC_AUTH_USERNAME'], auth.username):
            raise AuthException('Not authenticated.')
        else:
            return True


    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())

class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(message, Response(
            "You could not be authenticated. Please refresh the page.", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        ))

admin = Admin(app)
admin.add_view(CarView(Car, db.session))
admin.add_view(MyModelView(adminLog, db.session))
admin.add_view(MyModelView(CarPhoto, db.session))
    







@app.route('/')
def cars():
    cars_list = Car.query.all()    
    return render_template('cars.html', cars=cars_list)


@app.route('/search', methods=['GET'])
def cars_search():
    search_query = request.args.get('search', '')
    if search_query:
        cars_list = Car.query.filter(Car.Mark.ilike(f"%{search_query}%")).all()
    else:
        cars_list = Car.query.all()
    print(cars_list)
    return render_template('cars.html', cars=cars_list)


@app.route('/search/<car_inf>/<car_id>', methods=['GET'])
def car_info(car_inf, car_id):
    car = Car.query.filter_by(CarID=car_id).first()
    return render_template('car_info.html', carInfo=car)



@app.route('/upl', methods=['POST', 'GET'])
def upl():
    # pic = request.files['pic']

    # if not pic:
    #     return "ffalse"
    
    return render_template('upl.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
