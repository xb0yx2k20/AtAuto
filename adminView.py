from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


class CarView(ModelView):
    column_list = ['CarID', 'Mark', 'Model', 'Engine', 'hp', 'odo', 'GearBox', 'photos']


class LogView(ModelView):
    column_list = ['login', 'password']
