from flask import Flask, render_template, request, redirect, url_for
from models import Car, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/cars')
def cars():
    cars_list = Car.query.all()
    search_query = request.args.get('search', '')
    
    return render_template('cars.html', cars=cars_list)

@app.route('/cars/search', methods=['GET'])
def cars_search():
    search_query = request.args.get('search', '')
    if search_query:
        cars_list = Car.query.filter(Car.Mark.ilike(f"%{search_query}%")).all()
    else:
        cars_list = Car.query.all()
    return render_template('cars.html', cars=cars_list)

if __name__ == '__main__':
    app.run(debug=True)
