from sqlalchemy import Column, Integer, String
from database.database import Base

class ProfileRequest(Base):
    __tablename__ = 'profileRequest'
    id = Column(Integer, primary_key=True)
    sender = Column(Integer, unique=False)
    reciver = Column(Integer, unique=False)
    date = Column(Integer, unique=False)
    accepted = Column(Integer, unique=False)

    def __init__(self, name=None, sender=None, reciver=None, database=None, accepted=None):
        self.name = name
        self.sender = sender
        self.reciver = reciver
        self.database = database
        seld.accepted = accepted