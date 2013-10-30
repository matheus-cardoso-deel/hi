from flask import render_template, request, redirect, url_for, session, jsonify
from hi_server.database.db_config import db_session
from hi_server import app
from hi_server.forms import RegisterForm
from hi_server.models.user import User
from hi_server.models.profileRequest import ProfileRequest
from hi_server.views.full_profile_request_view import has_full_profile_request, full_profile_request_accepted
import md5

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST' and form.validate():
		c = User(form.name.data, form.username.data, form.email.data, md5.new(form.password.data).hexdigest(), form.description.data)
		db_session.add(c)
		db_session.commit()
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route("/user/<id>", methods=['GET', 'POST'])
def show_user(id):
	if request.method == 'GET':
		user = User.query.get(id)
		full_profile_request = has_full_profile_request(id)
		has_request = False
		if full_profile_request != None:
			has_request = True
			if full_profile_request_accepted(full_profile_request):
				user_information = user.complex_information_to_json()
			else:
				user_information = user.simple_information_to_json()
		else:
			user_information = user.simple_information_to_json()
		user_information['has_request'] = has_request
		return render_template('user_information.html', user_information=user_information, **User.query.get(session['user_session']).to_json())

	else:
		return redirect(url_for('home'))

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

@app.route("/show", methods=['GET', 'POST'])
def show_self():
	if request.method == 'POST':
		print request.form['name']
		user = User.query.get(session['user_session'])
		user.name = request.form['name']
		user.email = request.form['email']
		user.description = request.form['description']
		db_session.commit()
	return render_template('show.html', **User.query.get(session['user_session']).to_json())


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