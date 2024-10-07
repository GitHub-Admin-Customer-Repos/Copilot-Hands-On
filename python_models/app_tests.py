import unittest
from datetime import datetime
from models import User, Product, Order, Review

class TestUserModel(unittest.TestCase):
    def test_user_creation(self):
        user = User(1, "John Doe", "john@example.com")
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john@example.com")

    def test_user_to_dict(self):
        user = User(1, "John Doe", "john@example.com")
        self.assertEqual(user.to_dict(), {"user_id": 1, "name": "John Doe", "email": "john@example.com"})

class TestProductModel(unittest.TestCase):
    def test_product_creation(self):
        product = Product(1, "Laptop", "A powerful laptop", 999.99)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.description, "A powerful laptop")
        self.assertEqual(product.price, 999.99)

    def test_product_to_dict(self):
        product = Product(1, "Laptop", "A powerful laptop", 999.99)
        self.assertEqual(product.to_dict(), {"product_id": 1, "name": "Laptop", "description": "A powerful laptop", "price": 999.99})

class TestOrderModel(unittest.TestCase):
    def test_order_creation(self):
        order = Order(1, 1, datetime.now())
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.user_id, 1)
        self.assertIsInstance(order.order_date, datetime)
        self.assertEqual(order.items, [])

    def test_order_to_dict(self):
        order_date = datetime.now()
        order = Order(1, 1, order_date)
        self.assertEqual(order.to_dict(), {"order_id": 1, "user_id": 1, "order_date": order_date.isoformat(), "items": []})

class TestReviewModel(unittest.TestCase):
    def test_review_creation(self):
        review = Review(1, 1, 1, 5, "Great product!")
        self.assertEqual(review.review_id, 1)
        self.assertEqual(review.user_id, 1)
        self.assertEqual(review.product_id, 1)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.comment, "Great product!")

    def test_review_to_dict(self):
        review = Review(1, 1, 1, 5, "Great product!")
        self.assertEqual(review.to_dict(), {"review_id": 1, "user_id": 1, "product_id": 1, "rating": 5, "comment": "Great product!"})

if __name__ == '__main__':
    unittest.main()