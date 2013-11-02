# -*- coding : utf8 -*-

from app import hi
from app.database.db_config import init_db, db_session
from app.models.user import User
from flask import render_template, request, session

init_db()

@hi.route("/")
@hi.route("/index")
def index():
	return render_template('index.html')

@hi.route("/home", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html', **User.query.get(session['user_session']).to_json())
	else:
		return render_template('404.html')

@hi.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()