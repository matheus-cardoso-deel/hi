# -*- coding : utf8 -*-

from flask import render_template, request, session
from hi_server.database.db_config import init_db, db_session
from hi_server import app
from hi_server.models.user import User

init_db()

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/home", methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html', **User.query.get(session['user_session']).to_json())
	else:
		return render_template('404.html')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()