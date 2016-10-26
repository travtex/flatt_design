from flask import Flask 

from .views.public import public
from .views.admin import admin

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config') # Dev config settings
app.config.from_pyfile('config.py') # Production config settings

app.register_blueprint(public)
app.register_blueprint(admin)

from app import views