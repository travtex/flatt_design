#!venv_FD/bin/python
from app import app, db, models
from flask_security import Security, SQLAlchemyUserDatastore

user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)


@app.before_first_request
def create_user():
	db.create_all()
	if not models.User.query.first():
		user_datastore.create_user(email=app.config['ADMIN_EMAIL'], 
									username=app.config['ADMIN_USERNAME'], 
									password=app.config['ADMIN_PASSWORD'])
		db.session.commit()

if __name__ == '__main__':
	app.run(
		host=app.config['HOST'], 
		port=app.config['PORT'], 
		debug=app.config['DEBUG']
	)