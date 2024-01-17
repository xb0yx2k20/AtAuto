from flask_bcrypt import Bcrypt
from flask import Flask
from models import Car, CarPhoto, adminLog, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
bcrypt = Bcrypt(app) 

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        car1 = Car(Mark='Toyota', Model='Rav4', Year=2020, Engine = '3.5',hp = 280, GearBox = 'AT', odo = 123)
        photocar1 = CarPhoto(car_id=car1.CarID, url='https://mn365.ru/wp-content/uploads/2022/12/1592144830_toyota_rav4_2013-1.jpg')
        photocar2 = CarPhoto(car_id=car1.CarID, url='https://s0.rbk.ru/v6_top_pics/resized/1024xH/media/img/2/82/754788767211822.jpeg')
        car1 = Car(Mark='Toyota', Model='Rav4', Year=2020, Engine='3.5', hp=280, GearBox='AT', odo=123)
        photocar1 = CarPhoto(car_id=car1.CarID,
                             url='https://mn365.ru/wp-content/uploads/2022/12/1592144830_toyota_rav4_2013-1.jpg')
        photocar2 = CarPhoto(car_id=car1.CarID,
                             url='https://s0.rbk.ru/v6_top_pics/resized/1024xH/media/img/2/82/754788767211822.jpeg')
        car1.photos.append(photocar1)
        car1.photos.append(photocar2)

        car2 = Car(Mark='Kia', Model='K5', Year=2018, Engine = '1.5', hp = 150, GearBox = 'AT')
        car3 = Car(Mark='Dodge', Model='Charger', Year=2023, Engine = '6.2', hp = 702, GearBox = 'MT')
        car2 = Car(Mark='Kia', Model='K5', Year=2018, Engine='1.5', hp=150, GearBox='AT')
        car3 = Car(Mark='Dodge', Model='Charger', Year=2023, Engine='6.2', hp=702, GearBox='MT')


        hashed_password = bcrypt.generate_password_hash('user_password').decode('utf-8')
        print(hashed_password)
        new_user = adminLog(login='admin', password=hashed_password)
        db.session.add_all([new_user, car1, photocar1, photocar2, car2, car3])
        db.session.commit()

        