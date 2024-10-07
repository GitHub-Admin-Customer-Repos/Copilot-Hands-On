import unittest
from datetime import datetime
from models import User, Product, Order, Review

class TestModels(unittest.TestCase):

    def test_user_creation(self):
        user = User(1, "Alice", "alice@example.com")
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, "Alice")
        self.assertEqual(user.email, "alice@example.com")

    def test_product_creation(self):
        product = Product(1, "Laptop", "A high performance laptop", 1500.00)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "A high performance laptop")
        self.assertEqual(product.price, 1500.00)

    def test_order_creation(self):
        order = Order(1, 1, datetime.now())
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.user_id, 1)
        self.assertIsInstance(order.order_date, datetime)

    def test_review_creation(self):
        review = Review(1, 1, 1, 5, "Excellent product!")
        self.assertEqual(review.review_id, 1)
        self.assertEqual(review.user_id, 1)
        self.assertEqual(review.product_id, 1)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Excellent product!")

    def test_user_to_dict(self):
        user = User(1, "Alice", "alice@example.com")
        user_dict = user.to_dict()
        self.assertEqual(user_dict, {"user_id": 1, "name": "Alice", "email": "alice@example.com"})

    def test_product_to_dict(self):
        product = Product(1, "Laptop", "A high performance laptop", 1500.00)
        product_dict = product.to_dict()
        self.assertEqual(product_dict, {"product_id": 1, "name": "Laptop", "description": "A high performance laptop", "price": 1500.00})

    def test_order_to_dict(self):
        order = Order(1, 1, datetime.now())
        order_dict = order.to_dict()
        self.assertEqual(order_dict['order_id'], 1)
        self.assertEqual(order_dict['user_id'], 1)
        self.assertIsInstance(order_dict['order_date'], str)
        self.assertEqual(order_dict['items'], [])

    def test_review_to_dict(self):
        review = Review(1, 1, 1, 5, "Excellent product!")
        review_dict = review.to_dict()
        self.assertEqual(review_dict, {"review_id": 1, "user_id": 1, "product_id": 1, "rating": 5, "comment": "Excellent product!"})

if __name__ == '__main__':
    unittest.main()