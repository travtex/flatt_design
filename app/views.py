from flask import render_template
from app import app

# Public Routes
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	""" Index or home view. """
	return render_template('index.html', title='Home')

@app.route('/about')
@app.route('/team')
def about():
	return render_template('about.html', title='About Us')

@app.route('/services')
def services():
	return render_template('services.html', title='Our Services')

@app.route('/blog')
def blog():
	return render_template('blog.html', title='Blog')

@app.route('/portfolio')
@app.route('/work')
def portfolio():
	return render_template('portfolio.html', title='Our Work')

@app.route('/contact')
def contact():
	return render_template('contact.html', title='Contact Us')

# Administrative Routes

@app.route('/admin')
def admin():
	""" Administrative interface """
	user = {'nickname': 'Mr. Trav'}
	return render_template('admin_index.html', title='Admin Dashboard', user=user)

# Error Handling Pages
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500