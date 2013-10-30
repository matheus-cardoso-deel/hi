from flask import request, session, jsonify
from hi_server.database.db_config import db_session
from hi_server import app
from hi_server.models.user import User
import md5

@app.route("/sayHi/<id>", methods=['GET', 'POST'])
def say_hi():
	if request.method == 'GET':
		return hi_from(id)
	else:
		return say_hi(id)