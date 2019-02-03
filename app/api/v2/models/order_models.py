import os
from ..db.conn import init_db
import psycopg2
from flask import jsonify, make_response
from ..jwt_auth.jwt_auth import token_required

class OrderModels():
    """
    This class handles Order operations
    """
    def __init__(self):
        url = os.getenv('DB_URL')
        self.conn = psycopg2.connect(url)

    def post_order(self, name, price):
        self.name = name
        self.price = price

        curr = self.conn.cursor()

        query = """
            INSERT INTO orders (name, price)
                VALUES(
                    '%s', '%s'
                ) RETURNING id
        """ % (self.name, self.price)

        curr.execute(query)

        id = curr.fetchone()
        self.conn.commit()

        return id
        
        # curr.execute("SELECT * FROM orders WHERE id='%s'" %self.)

    def get_all_orders(self):
        curr = self.conn.cursor()
        curr.execute("SELECT * from orders")
        orders = curr.fetchall()
        return orders

    def fetchone(self, id):
        curr = self.conn.cursor()
        curr.execute("SELECT * FROM orders WHERE id='%s'" % id)
        order = curr.fetchone()
        return order


    def updateorderstatus(self, id, status):
        curr = self.conn.cursor()
        curr.execute(" UPDATE orders SET status = 'Delivered' WHERE id = '%s'" %s)
        self.conn.commit()
        curr.close()
        return status


    def delete_order(self, id):
        curr = self.conn.cursor()
        curr.execute("DELETE FROM orders WHERE id='%s'" % id)
        curr.close()
        return {
            'Message': 'Deleted!'
        }