from ..models.auth_models import AuthModels
# from ..jwt.jwt import token_required
from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from ..validators.validators import Validators
import jwt
import os

from werkzeug.security import generate_password_hash, check_password_hash
auth_mod = AuthModels()
validators = Validators()
class LandingPage(Resource):
    def get(self):
        return make_response(
			jsonify(
				{
					'Message': 'Welcome to the Auth area!'
				}
				), 200
			)

class UserReg(Resource):
	"""
	This class handles user registration
	"""
	def post(self):
		data = request.get_json()
		username = auth_mod.check_if_username_exists(data['username'])
		email = auth_mod.check_if_email_exists(data['email'])
		
		# password = data['password']
		password = validators.password_validator(data['password'])
		encrypted_pass = generate_password_hash(password, method='sha256')
		# admin = data['admin']

		usr_id = auth_mod.register_user(username=username, email=email, password=encrypted_pass)

		return jsonify(
			{
			'Message': 'Registration success',
			'User id': usr_id[0]
			}
		)

	def get(self):
		users = auth_mod.get_all_users()
		return make_response(
			jsonify( {
				'Message' : 'All Users',
				'Users': users
			})
		)

class Login(Resource):
	"""
	This class is used to log in a user provided the credentials are correct
	"""
	def post(self):
		data = request.get_json()
		email = data['email']
		password = data['password']

		if not email or not password:
			return make_response(jsonify(
				{
					'Message': 'Incorrect credentials'
				}
			)), 404

		user = auth_mod.get_user_email(email)
		if not user:
			return jsonify({
				'Message': 'User not registered'
			})

		else:
			encrypted_pass = auth_mod.get_login_pass(email)
			print(encrypted_pass)

			usr_id = auth_mod.get_user_id(email)
			if check_password_hash(encrypted_pass, password):
				token = jwt.JWT.encode(
					{
						"usr_id": usr_id,
						"expiry": dt.datetime.utcnow() + dt.timedelta(minutes=1)},
						os.getenv("SECRET_KEY"), 
						algorithm="HS256"
					
				)
				print(jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256']))

				return (
					{
						'token': token.decode('UTF-8')
					}
				)
			return {
				"Message": "Wrong password"
			}

	def get(self, id):
		user = auth_mod.fetch_one_user(id)
		return make_response(
			jsonify({
				'Message': 'User data',
				'details': user
			})
		)