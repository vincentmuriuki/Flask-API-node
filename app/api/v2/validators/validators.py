import re
import string
from flask import jsonify
from werkzeug.exceptions import BadRequest, NotFound
class Validators(object):
    """
    This class ensures the validity of user credentials, i.e. 
    the length and combination of the password
    the email and username
    """

    def password_validator(self, password):
        self.password = password
        if len(self.password) < 6:
            raise BadRequest("Password is short!")

        elif len(self.password)>15:
            raise BadRequest("Password is too long")
        else:
            return self.password