# from ..jwt.jwt import token_required
import psycopg2
# import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, make_response
from ..db.conn import init_db
import os
from werkzeug.exceptions import BadRequest

class AuthModels():
    """
    This class holds methods for user authentication and authorization
    """
    def __init__(self):
        url = os.getenv('DB_URL')
        self.conn = psycopg2.connect(url)

    def check_if_email_exists(self, email):
        self.email = email
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE email='%s'" % self.email)
        existing_email = cur.fetchone()
        cur.close()
        if existing_email:
            raise BadRequest("User exists!")

        else:
            return self.email
            
    def check_if_username_exists(self, username):
        self.username = username
        curr = self.conn.cursor()
        curr.execute("SELECT * FROM users WHERE username='%s'" % self.username)
        existing_username = curr.fetchone()
        if existing_username:
            raise BadRequest("Username is taken!")

        else:
            return self.username
            
    def register_user(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        # self.admin = admin

        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO users (username, email, password)
                VALUES(
                    '%s', '%s', '%s'
                ) RETURNING id
                """ % (self.username, self.email, self.password))

        id = cur.fetchone()
        self.conn.commit()
        cur.execute("SELECT * FROM users WHERE email='%s'" % self.email)
        user = cur.fetchone()
        print("User is" +str(user))
        return id

    def get_user_email(self, email):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE email='%s'" %email)
        user = cur.fetchone()
        return user

    def get_login_pass(self, email):
        cur = self.conn.cursor()
        cur.execute("SELECT password FROM users WHERE email='%s'" % email)
        hashed_password = cur.fetchone()[0]
        return hashed_password

    def get_user_id(self, email):
        cur = self.conn.cursor()
        cur.execute("SELECT id FROM users WHERE email='%s'" % email)
        usr_id = cur.fetchone()
        return usr_id

    def login_user(self, email, password):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE email='%s'" % email)
        id = cur.fetchone()
        return id

    def get_user_data_with_id(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE id='%s'" % id)
        usr_data = cur.fetchone()
        return usr_data

    def get_all_users(self):
        curr = self.conn.cursor()
        curr.execute("SELECT * FROM users")
        users = curr.fetchall()
        return users

    def create_admin(self):
        curr = self.conn.cursor()
        curr.execute("""
            INSERT INTO users (username, email, password, admin)
                VALUES(
                    'admin', 'email', 'password', 'True'
                )RETURNING id
                """
        )

        admin_user = curr.fetchone()
        return admin_user

    def fetch_one_user(self, id):
        curr = self.conn.cursor()
        curr.execute("SELECT * from users WHERE id='%s'" %id)
        user = curr.fetchone()
        return user