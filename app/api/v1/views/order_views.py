
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
            ), 200
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

    def __init__(self):
        self.ops = OrdersOps()

    def get(self, id):
        order = self.ops.getsingle(id)
        if order:
            return make_response(
                jsonify(
                    {
                        'Status': 'Ok',
                        'message': 'Order details',
                        'Orders' : order
                    }
                )
            )
        return make_response(
            jsonify({
            "message": "Order not found!"
        })
        )

    def put(self, id):
        order = self.ops.getsingle(id)
        if order:
            order.status = "Delivered"
            return make_response(
                jsonify({
                    'message': 'Order updated!',
                    'order' : order
                })
            )

    def delete(self, id):
        order = self.ops.getsingle(id)
        if not order:
            return make_response(
                jsonify({
                    'message': 'Order Not found!'
                })
            ), 404

        orders.remove(order)

        return make_response(
            jsonify({
                'message': 'Order deleted!'
            }), 200
        )