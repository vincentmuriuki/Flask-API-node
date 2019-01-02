# Standard library imports
import unittest
import json
import sys

# Local imports
# from api.v1 import *
from .api.v1 import create_app

class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_order_creation(self):
        sample_data = {
            "name": "Fish",
            "price": "1000",
            "quantity": "2"
        }
        response = self.client.post("/api/v1/orders",
        data=json.dumps(sample_data),
        headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data)['message'], "Order posted!")

    def test_get_orders(self):
        response = self.client.get(
            "/api/v1/orders",
            headers={"content-type": "application/json"}
            )
        self.assertEqual(response.status_code, 200)

    def test_if_can_get_order_by_id(self):
        response = self.client.get(
            "/api/v1/orders/1",
            headers={"content-type" : "application/json"}
        )
        self.assertEqual(response.status_code, 200)

    def test_if_can_update_order(self):
        response = self.client.put(
            "/api/v1/orders/1",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data)['message'], "Order updated!")
    
    def test_non_existing_order(self):
        response = self.client.get(
            "/api/v1/orders/1080",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data)['message'], "Order not found!")

    def test_if_can_delete_invalid_order(self):
        response = self.client.delete(
            "/api/v1/orders/1080",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.data)['message'],
        "Order Not found!")