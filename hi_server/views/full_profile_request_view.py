from flask import request, session, jsonify
from hi_server.database.db_config import db_session
from hi_server import app
from hi_server.models.user import User
import md5

@app.route("/fullProfileRequest/<id>", methods=['GET', 'POST'])
def full_profile_request():
	if request.method == 'GET':
		return requests_from(id)
	else:
		return request_full_profile(id)