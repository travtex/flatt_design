# flatt_design/app/views/admin.py

from flask import Blueprint, render_template

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def admin_index():
	""" Administrative interface """
	user = {'nickname': 'Mr. Trav'}
	return render_template('admin/index.html', title='Admin Dashboard', user=user)