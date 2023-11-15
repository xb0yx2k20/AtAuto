from flask import Flask, render_template, request
from models import Artist, Album, Song, Car, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)
'''
@app.route('/')
def songs():
    songs_list = Song.query.all()
    return render_template('songs.html', songs=songs_list)'''

@app.route('/car')
def cars():
    car_list = Car.query.all()
    search_query = request.args.get('search', '')
    cars_list = Car.query.filter(Car.Model.ilike(f"%{search_query}%")).all()
    return render_template('cars.html', cars=car_list)

if __name__ == '__main__':
    app.run(debug=True)