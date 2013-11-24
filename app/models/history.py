from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.database.db_config import Base, db_session
from app.models.user import User
from app.models.profile_requests import ProfileRequest


class History(list):
	def __init__(self, *args, **kwargs):
		full_profile_request = ProfileRequest()
		full_profile_requests = full_profile_request.get_requests()
		for request in full_profile_requests:
			self.append(request)
