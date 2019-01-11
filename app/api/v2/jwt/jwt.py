import jwt
from flask import jsonify, request
import bcrypt
from functools import wraps

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({
                "message": "Authentication token missing!"
            }), 401

        try:
            data = jwt.decode(token, os.getenv("SECRET_KEY"))
            current_user = user_models.get_user_details_with_id(user_id=data['user_id'])
        except Exception as e:
            return jsonify(
                {
                    "message" : "Invalid token! this is why : {}".format(e)
                }
            ), 401

        return f(current_user, *args, **kwargs)

    return decorated