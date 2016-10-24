from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	""" Index or home view. """
	user = {'nickname': 'Mr. Trav'} # Temp fake user
	return render_template('index.html', title='Home', user=user)

@app.route('/index/<string:name>')
def name(name):
	user = {'nickname': name}
	return render_template('index.html', title='Home', user=user)

@app.route('/admin')
def admin():
	""" Administrative interface """
	user = {'nickname': 'Mr. Trav'}
	return render_template('admin_index.html', title='Admin Dashboard', user=user)