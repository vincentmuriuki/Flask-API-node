
from flask_restful import Resource
from flask import request, jsonify, make_response
# local
from ..models.order_models import OrdersOps

class OrdersViews(Resource, OrdersOps):
    """docstring for Orders"""
    def __init__(self):
        self.ops = OrdersOps()

    def get(self):
        orders = self.ops.getall()
        return make_response(
            jsonify(
                {
                    'message': 'Order List',
                    'Status': 'Ok',
                    'Orders': orders
                }
            ), 201
        )

    def post(self):
        data = request.get_json()
        name = data['name']
        price = data['price']
        quantity = data['quantity']

        response = self.ops.save(name, price, quantity)
        return make_response(
            jsonify(
                {
                    'Status': 'Pending',
                    'message': 'Order Posted!',
                    'Order Details': response
        }))

class SingleOrder(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass