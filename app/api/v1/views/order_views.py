
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

#     def post(self):
#         pass

# class SingleOrder(Resource):
#     def get(self, id):
#         pass

#     def put(self, id):
#         pass

#     def delete(self, id):
#         pass