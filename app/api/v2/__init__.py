from flask import Blueprint

from flask_restful import Api

from .views.orders import Main, OrdersDl, IndividualOrders
from .views.users import LandingPage, UserReg, Login

version2 = Blueprint('api2', __name__, url_prefix='/api/v2')

api = Api(version2)

api.add_resource(Main, '/home')
api.add_resource(LandingPage, '/')
api.add_resource(UserReg, '/auth/signup', '/users-list')
api.add_resource(Login, '/auth/login', '/usr-data/<id>')
api.add_resource(OrdersDl, '/order', '/order-list')
api.add_resource(IndividualOrders, '/orders/<id>')