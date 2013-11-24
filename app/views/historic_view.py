from app import hi
from app.database.db_config import db_session
from app.models.event import Event
from app.models.user import User
from datetime import datetime
from flask import request, session, jsonify

@hi.route("/historic", methods=['GET', 'POST'])
def my_hitoric():
	if request.method == 'GET':
		historic = Event.query.filter_by(reciver=session['user_session'])
		historic_json = {}
		for event in historic:
			historic_json[event.id] = event.to_json();
		return jsonify(historic_json)

@hi.route("/events/seen", methods=['GET', 'POST'])
def seen_all_events():
	events = Event.query.filter_by(seen="false", reciver=session['user_session'])
	if events:	
		for event in events:
			event.seen = "true"
		db_session.commit()