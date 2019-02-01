"""
A list of queries to create both users and orders table
"""
users = """
CREATE TABLE IF NOT EXISTS Users (
    id serial PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(600) NOT NULL,
    admin boolean DEFAULT False)
    """
orders = """
CREATE TABLE IF NOT EXISTS orders (
    id serial PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price VARCHAR (20) NOT NULL,
    order_date TIMESTAMP WITH TIME ZONE DEFAULT ('now'::text)::date NOT NULL,
    status VARCHAR(100) DEFAULT 'Active')
    """

blacklist = """
CREATE TABLE IF NOT EXISTS blacklist(
    usr_tokens character varying(300) NOT NULL
)
"""

queries = [users, orders, blacklist]