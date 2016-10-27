from app import db
from flask_security import RoleMixin, UserMixin

class Base(db.Model):
	__abstract__ = True
	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
	modified_at = db.Column(db.DateTime, default=db.func.current_timestamp(),
					onupdate=db.func.current_timestamp())

roles_users = db.Table('roles_users',
						db.Column('user_id', db.Integer(),
								db.ForeignKey('auth_user.id')),
						db.Column('role_id', db.Integer(),
								db.ForeignKey('auth_role.id')))

class Role(Base, RoleMixin):
	__tablename__ = 'auth_role'
	name = db.Column(db.String(80), nullable=False, unique=True)
	description = db.Column(db.String(255))

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return '<Role %r>' % self.name

class User(Base, UserMixin):
	__tablename__ = 'auth_user'
	email = db.Column(db.String(255), nullable=False, unique=True)
	password = db.Column(db.String(255), nullable=False)
	username = db.Column(db.String(255), nullable=False, unique=True)
	first_name = db.Column(db.String(255))
	last_name = db.Column(db.String(255))
	active = db.Column(db.Boolean())
	last_login_at = db.Column(db.DateTime())
	current_login_at = db.Column(db.DateTime())
	last_login_ip = db.Column(db.String(45))
	current_login_ip = db.Column(db.String(45))
	login_count = db.Column(db.Integer)
	roles = db.relationship('Role', secondary=roles_users,
							backref=db.backref('users', lazy='dynamic'))

	def __repr__(self):
		return '<User %r>' % self.email