# -*- coding : utf8 -*-

from flask import render_template, request, redirect, url_for, session, jsonify
from database.db_config import init_db, db_session
from hi_server import app
from forms import LoginForm, RegisterForm
from models.user import User
import md5

init_db()

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'GET':
		return render_template('login.html', form=form)
	else:
		user = User.query.filter_by(email=form.email.data, password=md5.new(form.password.data).hexdigest()).first()
		if user != None:
			session['user_session'] = user.get_id()
			return redirect(url_for('home'))
		else:
			return redirect(url_for('login'))

@app.route("/logout")
def logout():
	session.pop('user_session', None)
	return redirect(url_for('index'))

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'GET':
		return render_template('register.html', form=form)
	else:
		c = User(form.name.data, form.email.data, md5.new(form.password.data).hexdigest(), form.description.data)
		db_session.add(c)
		db_session.commit()
		return redirect(url_for('login'))

@app.route("/home", methods=['GET', 'POST'])
def home():
	if 'user_session'in session:
		if request.method == 'GET':
			return render_template('home.html', **User.query.get(session['user_session']).to_json())
		else:
			return render_template('404.html')
	else:
		return redirect(url_for('login'))

@app.route("/user/<id>", methods=['GET', 'POST'])
def show_or_update():
	if request.method == 'GET':
		user = User.query.get(id)
		return render_template('show.html', user=user)
	else:
		return edit(request.form, id)

@app.route("/update/location", methods=['GET', 'POST'])
def update_location():
	if request.method == 'GET':
		return redirect(url_for('home'))
	else:
		user = User.query.get(session['user_session'])
		user.latitude = float(request.form['lat'])
		user.longitude = float(request.form['lon'])
		db_session.commit()
		near_users = get_near_users(user.latitude, user.longitude)
		print jsonify(near_users)
		return jsonify(near_users)

@app.route("/fullProfileRequest/<id>", methods=['GET', 'POST'])
def full_profile_request():
	if request.method == 'GET':
		return requests_from(id)
	else:
		return request_full_profile(id)

@app.route("/sayHi/<id>", methods=['GET', 'POST'])
def say_hi():
	if request.method == 'GET':
		return hi_from(id)
	else:
		return say_hi(id)


def get_near_users(lat, lon):
	max_lat = float(lat)+0.002
	min_lat = float(lat)-0.002
	max_lon = float(lon)+0.002
	min_lon = float(lon)-0.002
	users = db_session.query(User).filter(
		User.latitude<=max_lat, 
		User.latitude>=min_lat, 
		User.longitude<=max_lon, 
		User.longitude>=min_lon)
	users_json = {}
	for user in users:
		users_json[user.id] = user.simple_information_to_json()	
	return users_json

@app.before_request
def is_logged_in():
	if request.path == '/index' or request.path == '/login' or request.path == '/register':
		pass
	else:
		if not 'user_session' in session:
			return redirect(url_for('login'))

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()