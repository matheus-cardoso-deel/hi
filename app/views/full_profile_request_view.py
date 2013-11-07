import md5

from app import hi
from app.database.db_config import db_session
from app.models.profile_request import ProfileRequest
from app.models.user import User
from datetime import datetime
from flask import request, session, jsonify

@hi.route("/fullProfileRequest/<id>", methods=['GET', 'POST'])
def create_full_profile_request(id):
	if request.method == 'POST':
		if int(id) != session['user_session']:
			if ProfileRequest.exists(id) == None:
				full_profile_request = ProfileRequest(sender=session['user_session'], reciver=id, date=datetime.now(), accepted=0)
				db_session.add(full_profile_request)
				db_session.commit()
				return 'success'
	return 'fail'

