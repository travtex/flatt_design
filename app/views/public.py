# flatt_design/app/views/public.py

from flask import Blueprint, render_template

public = Blueprint('public', __name__)

@public.route('/')
@public.route('/index')
@public.route('/home')
def index():
	""" Index or home view. """
	return render_template('public/index.html', title='Home')

@public.route('/about')
@public.route('/team')
def about():
	return render_template('public/about.html', title='About Us')

@public.route('/services')
def services():
	return render_template('public/services.html', title='Our Services')

@public.route('/blog')
def blog():
	return render_template('public/blog.html', title='Blog')

@public.route('/portfolio')
@public.route('/work')
def portfolio():
	return render_template('public/portfolio.html', title='Our Work')

@public.route('/contact')
def contact():
	return render_template('public/contact.html', title='Contact Us')