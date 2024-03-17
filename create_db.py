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

        hashed_login = bcrypt.generate_password_hash('admin0').decode('utf-8')
        hashed_password = bcrypt.generate_password_hash('admin1').decode('utf-8')
        new_admin_log = adminLog(login=hashed_login, password=hashed_password)
        db.session.add(new_admin_log)
        db.session.commit()


       