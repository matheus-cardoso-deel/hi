from app import hi
from app.database.db_config import db_session
from app.models.event import Event
from app.models.user import User
from datetime import datetime
from flask import request, session, jsonify

@hi.route("/full-profile-request/<id>", methods=['GET', 'POST'])
def create_full_profile_request(id):
	if request.method == 'POST':
		if int(id) != session['user_session']:
			profile_request = Event()
			if not profile_request.exists(id):
				full_profile_request = Event(sender=session['user_session'], 
											 reciver=id, 
											 kind="full_profile_request", 
											 option="sended",
											 created_at=datetime.now())
				db_session.add(full_profile_request)
				db_session.commit()
				return 'success'
	return 'badaccess'

@hi.route("/full-profile-request/<sender_id>/accept")
def accept_full_profile_request(sender_id):
	full_profile_request = Event.query.filter_by(sender=sender_id, reciver=session['user_session'])
	if full_profile_request:
		full_profile_request.option = "accepted"
		db_session.commit()
		return "success"
	return "fail"

@hi.route("/events/seen", methods=['GET', 'POST'])
def seen_all_events():
	events = Event.query.filter_by(seen="false", reciver=session['user_session'])
	if events:	
		for event in events:
			event.seen = "true"
		db_session.commit()