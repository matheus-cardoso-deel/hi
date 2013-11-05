from sqlalchemy import Column, Integer, String
from database.database import Base

class Hi(Base):
    __tablename__ = 'hi'
    
    id = Column(Integer, primary_key=True)
    sender = Column(Integer, db.ForeignKey('user.id'))
    reciver = Column(Integer, db.ForeignKey('user.id'))
    date = Column(Integer, unique=False)

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.get('sender', None)
        self.reciver = kwargs.get('reciver', None)
        self.date = kwargs.get('date', None)