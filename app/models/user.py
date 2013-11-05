from sqlalchemy import Column, Integer, String, Float
from app.database.db_config import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120), unique=False)
    description = Column(String(120), unique=False)
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
            User.id!=session['user_session'],
            User.latitude<=max_lat, 
            User.latitude>=min_lat, 
            User.longitude<=max_lon, 
            User.longitude>=min_lon)
        users_json = {}
        for user in users:
            users_json[user.id] = user.simple_information_to_json() 
        return users_json

    def get_id(self):
        return self.id

    def to_json(self):
        return {'user' : {
                    'id' : self.id, 
                    'name' : self.name, 
                    'email': self.email,
                    'password' : self.password,
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
                'longitude' : self.longitude }
