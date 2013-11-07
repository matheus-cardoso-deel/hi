import md5

from app import hi
from app.database.db_config import db_session
from app.forms import RegisterForm
from app.models.profile_request import ProfileRequest
from app.models.user import User
from flask import render_template, request, redirect, url_for, session, jsonify, send_from_directory


IMG_UPLOAD_FOLDER = 'app/uploads/users/images'
ICON_UPLOAD_FOLDER = 'app/uploads/users/images'

@hi.route("/user/image/<path:filename>")
def user_image(filename):
	return send_from_directory("uploads/users/images", filename)

@hi.route("/user/icon/<path:filename>")
def user_icon(filename):
	return send_from_directory("uploads/users/icons", filename)

@hi.route("/register", methods=['GET', 'POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == 'POST':
		file = request.files[form.image.name].read()
		if not file == None:
			user = User(name=form.name.data,
						username=form.username.data,
						email=form.email.data,
						password=md5.new(form.password.data).hexdigest(),
						description=form.description.data)
	        user.save_image(file)
	        db_session.add(user)
	        db_session.commit()
	        print user.icon_url
	        return redirect(url_for('login'))
	return render_template('register.html', form=form)

@hi.route("/user/<id>", methods=['GET', 'POST'])
def show_user(id):
	if request.method == 'GET':
		user = User.query.get(id)
		full_profile_request = ProfileRequest()
		full_profile_request.exists(id)
		has_request = False
		if full_profile_request != None:
			has_request = True
			if full_profile_request.is_accepted():
				user_information = user.complex_information_to_json()
			else:
				user_information = user.simple_information_to_json()
		else:
			user_information = user.simple_information_to_json()
		user_information['has_request'] = has_request
		return render_template('user_information.html', user_information=user_information, **User.query.get(session['user_session']).to_json())
	else:
		return redirect(url_for('home'))

@hi.route("/update/location", methods=['GET', 'POST'])
def update_location():
	if request.method == 'GET':
		return redirect(url_for('home'))
	else:
		user = User.query.get(session['user_session'])
		user.latitude = float(request.form['lat'])
		user.longitude = float(request.form['lon'])
		db_session.commit()
		near_users = user.get_near_users()
		print jsonify(near_users)
		return jsonify(near_users)

@hi.route("/show", methods=['GET', 'POST'])
def show_self():
	if request.method == 'POST':
		print request.form['name']
		user = User.query.get(session['user_session'])
		user.name = request.form['name']
		user.email = request.form['email']
		user.description = request.form['description']
		db_session.commit()
	return render_template('show.html', **User.query.get(session['user_session']).to_json())