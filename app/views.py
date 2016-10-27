from flask import render_template
from app import app
from flask_security import login_required

# Public Routes
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	""" Index or home view. """
	return render_template('public/index.html', title='Home')

@app.route('/about')
@app.route('/team')
def about():
	return render_template('public/about.html', title='About Us')

@app.route('/services')
def services():
	return render_template('public/services.html', title='Our Services')

@app.route('/blog')
def blog():
	return render_template('public/blog.html', title='Blog')

@app.route('/portfolio')
@app.route('/work')
def portfolio():
	return render_template('public/portfolio.html', title='Our Work')

@app.route('/contact')
def contact():
	return render_template('public/contact.html', title='Contact Us')

# Administrative Routes

@app.route('/admin')
@login_required
def admin():
	""" Administrative interface """
	user = {'nickname': 'Mr. Trav'}
	return render_template('admin/index.html', title='Admin Dashboard', user=user)

# Error Handling Pages
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500