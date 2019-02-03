from flask_restful import Resource, reqparse
from flask import make_response, jsonify, request
from ..models.order_models import OrderModels
from ..jwt_auth.jwt_auth import token_required
# from flask_restful import reqparse, 
order_mod = OrderModels()

class Main(Resource):
	def get(self):
		return make_response(
			jsonify(
				{
					'Message': 'Welcome to my Api'
				}
				), 200
			)

class OrdersDl(Resource):
	"""
	This class takes care of placing new orders 
	"""
	# @token_required
	def post(self):
		data = request.get_json()
		name = data['name']
		price = data['price']

		id = order_mod.post_order(name=name, price=price)

		return jsonify(
				{
				'Message': 'Order Posted',
				'Order ID': id[0]
				}
			)
	# @token_required
	def get(self):
		orders = order_mod.get_all_orders()
		return make_response(
			jsonify(
				{
					'Message': 'Order list',
					'Orders': orders
				}
			)
		)

class IndividualOrders(Resource):
	def get(self, id):
		order = order_mod.fetchone(id)
		return make_response( jsonify(
			{
				'Order': order
			}
		))

	def put(self, id):
		parser = reqparse.RequestParser()
		parser.add_argument('status', type=str, required=True, help="Required!")
		args = parser.parse_args()
		print(args)
		status = args['status']
		order = order_mod.updateorderstatus(status, id)
		return jsonify({
			'Order': order
		})


	def delete(self, id):
		order = order_mod.delete_order(id)
		return order