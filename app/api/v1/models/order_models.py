
orders = []

class OrdersOps():
    def __init__(self):
        self.orders = orders

    def save(self, name, price, quantity):
        order_parts = {
            'id': len(orders) + 1,
            'Description': {'Name of Snack' : name},
            'Price': price,
            'Quantity': quantity
        }
        self.orders.append(order_parts)

        return self.orders

    def getall(self):
        return self.orders

    def getsingle(self):
        for order in self.orders:
            if (order['id'] == id):
                return order

            return "Order not found!"