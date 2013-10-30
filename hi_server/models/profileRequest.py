from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from hi_server.database.db_config import Base

class ProfileRequest(Base):
    __tablename__ = 'profile_requests'
    id = Column(Integer, primary_key=True)
    sender = Column(Integer, unique=False)
    reciver = Column(Integer, unique=False)
    date = Column(DateTime, unique=False)
    accepted = Column(Integer, unique=False)

    def __init__(self, name=None, sender=None, reciver=None, database=None, accepted=None):
        self.name = name
        self.sender = sender
        self.reciver = reciver
        self.database = database
        seld.accepted = accepted