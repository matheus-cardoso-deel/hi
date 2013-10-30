from flask import render_template, request, redirect, url_for, session
from hi_server import app
from hi_server.forms import LoginForm
from hi_server.models.user import User
import md5


@app.before_request
def is_logged_in():
	if not 'user_session' in session:
		if not request.path in urls_allowed_without_auth:
			return redirect(url_for('login'))
	elif request.path in urls_blocked_with_auth:
			return redirect(url_for('home'))


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'GET':
		return render_template('login.html', form=form)
	else:
		user = User.query.filter_by(username=form.username.data, password=md5.new(form.password.data).hexdigest()).first()
		if user != None:
			session['user_session'] = user.get_id()
			return redirect(url_for('home'))
		else:
			return redirect(url_for('login'))

@app.route("/logout")
def logout():
	session.pop('user_session', None)
	return redirect(url_for('index'))


urls_allowed_without_auth = ('/index', '/register', '/login')
urls_blocked_with_auth = ('/register', '/login')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'