from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.db_config import Base, db_session
from app.models.user import User
from sqlalchemy import or_, and_
from flask import session

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    sender = Column(Integer, unique=False)
    reciver = Column(Integer, unique=False)
    created_at = Column(DateTime, unique=False)
    updated_at = Column(DateTime, unique=False)
    kind = Column(String, unique=False)
    seen = Column(String, unique=False)
    option = Column(String, unique=False)

    def __init__(self, *args, **kwargs):
        self.sender = kwargs.get('sender', None)
        self.reciver = kwargs.get('reciver', None)
        self.kind = kwargs.get('kind', None)
        self.seen = kwargs.get('seen', 'false')
        self.option = kwargs.get('option', None)
        self.created_at = kwargs.get('created_at', None)
        self.updated_at = kwargs.get('updated_at', None)


    def to_json(self):
        sender = User.query.get(self.sender)
        return {'id' : self.id,
                'sender' : self.sender,
                'sender_name' : sender.name,
                'reciver' : self.reciver,
                'kind' : self.kind,
                'option' : self.option,
                'created_at' : self.created_at,
                'updated_at' : self.updated_at}

    def exists(self, id):
        full_profile_requests = db_session.query(Event).filter(
                    or_(
                            and_(
                            Event.sender == session['user_session'],
                            Event.reciver == id,
                            Event.kind == 'full_profile_request'),
                            and_(
                            Event.sender == id,
                            Event.reciver == session['user_session'],
                            Event.kind == 'full_profile_request')
                            )
                    ).first()
        print full_profile_requests
        if full_profile_requests:
            return True
        else:
            return False

    def is_accepted(self):
        if self.option == "accepted":
            return True
        return False

    def accept_request(self):
        self.option = "accepted"
        if db_session.commit():
            return True
        return False