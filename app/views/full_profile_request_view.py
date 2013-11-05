import md5

from app import hi
from app.database.db_config import db_session
from app.models.profileRequest import ProfileRequest
from app.models.user import User
from datetime import datetime
from flask import request, session, jsonify
from sqlalchemy import or_, and_

@hi.route("/fullProfileRequest/<id>", methods=['GET', 'POST'])
def create_full_profile_request(id):
	if request.method == 'POST':
		if int(id) != session['user_session']:
			if has_full_profile_request(id) == None:
				full_profile_request = ProfileRequest(sender=session['user_session'], reciver=id, date=datetime.now(), accepted=0)
				db_session.add(full_profile_request)
				db_session.commit()
				return 'success'
	return 'fail'

def has_full_profile_request(id):
	full_profile_request = db_session.query(ProfileRequest).filter(
                or_(
                        and_(
                        ProfileRequest.sender == session['user_session'],
                        ProfileRequest.reciver == id,), 
                        and_(
                        ProfileRequest.sender == id,
                        ProfileRequest.reciver == session['user_session'],)
                        )
                ).first()
	return full_profile_request

def full_profile_request_accepted(full_profile_request):
	if full_profile_request.accepted == 1:
		return True
	return False