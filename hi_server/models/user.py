from sqlalchemy import Column, Integer, String, Float
from hi_server.database.db_config import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False)
    email = Column(String(120), unique=False)
    password = Column(String(120), unique=False)
    description = Column(String(120), unique=False)
    latitude = Column(Float, unique=False)
    longitude = Column(Float, unique=False)

    def __str__():
    	return self.name

    def __init__(self, name=None, email=None, password=None, description=None, latitude=None, longitude=None):
        self.name = name
        self.email = email
        self.password = password
        self.description = description
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return self.name

    def get_id(self):
        return self.id

    def to_json(self):
        return {'user' : {'id' : self.id, 'name' : self.name, 'email': self.email, 'description' : self.description}}

    def simple_information_to_json(self):
        return { 'id' : self.id, 'name': self.name, 'latitude' : self.latitude, 'longitude' : self.longitude }
