import os

from sqlalchemy import Column, Integer, String, Float
from app.database.db_config import Base, db_session
from app.models.image_helper import resize_to_icon_size

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120), unique=False)
    description = Column(String(120), unique=False)
    image_url = Column(String(120), unique=False)
    icon_url = Column(String(120), unique=False)
    latitude = Column(Float, unique=False)
    longitude = Column(Float, unique=False)

    def __str__():
    	return self.name

    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', None)
        self.username = kwargs.get('username', None)
        self.email = kwargs.get('email', None)
        self.password = kwargs.get('password', None)
        self.description = kwargs.get('description', None)
        self.latitude = kwargs.get('latitude', None)
        self.longitude = kwargs.get('longitude', None)

    def __repr__(self):
        return self.name

    def get_near_users(self):
        max_lat = float(self.latitude)+0.002
        min_lat = float(self.latitude)-0.002
        max_lon = float(self.longitude)+0.002
        min_lon = float(self.longitude)-0.002
        users = db_session.query(User).filter(
            User.id!=self.id,
            User.latitude<=max_lat, 
            User.latitude>=min_lat, 
            User.longitude<=max_lon, 
            User.longitude>=min_lon)
        users_json = {}
        for user in users:
            users_json[user.id] = user.simple_information_to_json() 
        return users_json

    def save_image(self, file):
        image_path = self.username+".jpg"
        icon_path = self.username+".png"
        #diretorio real
        open(os.path.join('app/uploads/users/images', image_path), 'w+').write(file)
        open(os.path.join('app/uploads/users/icons', icon_path), 'w+').write(file)
        #Bug, tem que ter os 2 diretorios pra acessar imagem
        open(os.path.join('uploads/users/images', image_path), 'w+').write(file)
        open(os.path.join('uploads/users/icons', icon_path), 'w+').write(file)
        resize_to_icon_size(icon_path)
        self.image_url = "/user/image/"+image_path
        self.icon_url = "/user/icon/"+icon_path


    def get_id(self):
        return self.id

    def to_json(self):
        return {'user' : {
                    'id' : self.id, 
                    'name' : self.name, 
                    'email': self.email,
                    'password' : self.password,
                    'image_url' : self.image_url,
                    'icon_url' : self.icon_url,
                    'description' : self.description}}

    def complex_information_to_json(self):
        return {'id' : self.id, 
                'name' : self.name, 
                'email': self.email, 
                'description' : self.description,
                'latitude' : self.latitude, 
                'longitude' : self.longitude }

    def simple_information_to_json(self):
        return {'id' : self.id, 
                'name': self.name, 
                'latitude' : self.latitude,
                'image_url' : self.image_url,
                'icon_url' : self.icon_url,
                'longitude' : self.longitude }
