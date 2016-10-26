#!venv_FD/bin/python
from app import app, db

if __name__ == '__main__':
	app.run(
		host=app.config['HOST'], 
		port=app.config['PORT'], 
		debug=app.config['DEBUG']
	)