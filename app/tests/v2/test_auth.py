
import unittest
from ....app import create_app
import json
from ....instance import config
from ...api.v2.db.conn import init_test_database

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = init_test_database()

    def tearDown(self):
        self.app_context.pop()

    def test_user_registration(self):
        """
        User signup tests
        """
        user = {
            'username': 'Vinc',
            'email': 'vinc@mail.com',
            'password': 'password'
        }
        response = self.client.post("/api/v1/auth/signup",
        data=json.dumps(user),
        headers={"content-type": "application/json"})

        self.assertEqual(json.loads(response.data)['message'], "User successfully registered!")
        self.assertEqual(response.status_code, 200)


    def test_register_existing_username(self):
        """
        Tests if a user can register using an existing username
        """
        user1 = {
            'username': 'Vinc',
            'email': 'vinc@mail.com',
            'password': 'password'
        }

        self.client.post('/api/v2/auth/signup',
        data=json.dumps(user1),
            headers={"content-type": "application/json"}
            )
        
        user2 = {
            'username': 'Vinc',
            'email': 'vinc@mail.com',
            'password': 'password'
        }

        response2 = self.client.post('/api/v2/auth/signup',
            data=json.dumps(user2),
            headers={"content-type": "application/json"}
            )
        
        self.assertEqual(response2.status_code, 404)
        self.assertEqual(json.loads(response2.data)['message'], "Username is taken!")

    def test_register_existing_email(self):
        """
        Tests if one can register with the same email twice
        """
        user1 = {
            'usename': 'Vinc',
            'email': 'vinc@mail.com',
            'password': 'password'
        }

        self.client.post('/api/v2/auth/signup',
            data=json.dumps(user1),
            headers={"content-type": "application/json"})

        user2 = {
            'username': 'Vinc',
            'email': 'vinc@mail.com',
            'password': 'password'
        }

        response2 = self.client.post('/api/v2/auth/signup',
            data=json.dumps(user2),
            headers={"content-type": "application/json"}
            )

        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response2.data)['message'], "Email is already registered! Login")
