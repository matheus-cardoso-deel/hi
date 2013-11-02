import md5

from app import hi
from flask import request, session, jsonify
from app.database.db_config import db_session
from app import app
from app.models.user import User

@hi.route("/sayHi/<id>", methods=['GET', 'POST'])
def say_hi():
	if request.method == 'GET':
		return hi_from(id)
	else:
		return say_hi(id)