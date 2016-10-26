from flask import render_template
from app import app

# Error Handling Pages
@app.errorhandler(404)
def page_not_found(e):
	return render_template('public/404.html'), 404

@app.errorhandler(500)
def server_error(e):
	return render_template('public/500.html'), 500