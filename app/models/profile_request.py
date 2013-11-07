from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.db_config import Base, db_session
from sqlalchemy import or_, and_

class ProfileRequest(Base):
    __tablename__ = 'profile_requests'
    
    id = Column(Integer, primary_key=True)
    sender = Column(Integer, unique=False)
    reciver = Column(Integer, unique=False)
    date = Column(DateTime, unique=False)
    accepted = Column(Integer, unique=False)

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.get('sender', None)
        self.reciver = kwargs.get('reciver', None)
        self.date = kwargs.get('date', None)
        self.accepted = kwargs.get('accepted', None)

    def exists(self, id):
        full_profile_request = db_session.query(ProfileRequest).filter(
                    or_(
                            and_(
                            ProfileRequest.sender == self.id,
                            ProfileRequest.reciver == id,), 
                            and_(
                            ProfileRequest.sender == id,
                            ProfileRequest.reciver == self.id,)
                            )
                    ).first()
        self = full_profile_request

    def is_accepted(self):
        if self.accepted == 1:
            return True
        return False