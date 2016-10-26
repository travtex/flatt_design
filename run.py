#!venv_FD/bin/python
from app import app
app.run(debug=app.config['DEBUG'])