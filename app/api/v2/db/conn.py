# system library imports
import os
import psycopg2
from flask import current_app

from .tables import queries

def init_db():
    """
    Database connection
    :param dbname: dbname
    :param host: Host
    :param user: User
    :param port: Port
    """
    url = os.environ.get('DB_URL')
    conn = psycopg2.connect(url)
    curr = conn.cursor()
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
        return conn
    except Exception as err:
        print(err)

def init_test_database():
    """
    Initialize the test database
    """
    url = os.environ.get('TEST_DB_URL')
    conn = psycopg2.connect(url)
    curr = conn.cursor()
    try:
        for query in queries:
            curr.execute(query)
        conn.commit()
    except Exception as err:
        print(err)

def tear_down():
    """
    Drop all tables in the test database
    """
    test_db_url = os.getenv('TEST_DB_URL')
    conn = psycopg2.connect(test_db_url)
    curr = conn.cursor()
    users = "DROP TABLE IF EXISTS users CASCADE"
    orders = "DROP TABLE IF EXISTS orders CASCADE"
    blacklist = "DROP TABLE IF EXISTS blacklist CASCADE"
    queries = [users, orders, blacklist]

    try:
        for query in queries:
            cursor.execute(query)
        conn.commit()
    except Exception as err:
        print(err)