# import jwt
from flask import jsonify, request, make_response
# import bcrypt
from functools import wraps
import os

def token_required(f):
    """
    A deecorator function that ensures that a specific resouce is accessed only by Authorized users
    only if their auth access tokens are valid
    :param f:
    :return:
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            # return make_response(jsonify({
            #     'status': 'failed',
            #     'message': 'Token is missing!'
            # })), 401
            return jsonify({
                'status': 'failed',
                'Message': 'Token is missing'
            })

        try:
            data = jwt.decode(token, os.getenv("SECRET_KEY"))
            current_user = auth_models.get_user_details_with_id(user_id=data['user_id'])
            
        except Exception as e:
            return jsonify(
                {
                    "message" : "Invalid token! this is why : {}".format(e)
                }
            ), 401

            if isinstance(data, str):
                message = data
            return make_response(jsonify({
                'status': 'failed',
                'message': message
            })), 401

        return f(current_user, *args, **kwargs)

    return decorated

def response(status, message, status_code):
    """
    A method to make Http responses if provided the status, message, and status code
    :param status: Status
    :param message: Message
    :param status_code: Http status code
    """
    return make_response(jsonify({
        'status': status,
        'message': message,
    })), status_code

def auth_response(status, message, token, status_code):
    """
    A metthod to make Http response to send the auth token
    :param status: STatus
    :param message: Message
    :param token: Authorization Token
    :param status code: Http status code
    :return Http Json response
    """
    return make_response(jsonify({
        'status': status,
        'message': message,
        'token': token.decode("utf-8")
    }))