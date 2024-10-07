from datetime import datetime
from typing import List

# User Model
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "email": self.email}

# Product Model
class Product:
    def __init__(self, product_id: int, name: str, description: str, price: float):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    def to_dict(self):
        return {"product_id": self.product_id, "name": self.name, "description": self.description, "price": self.price}

# Order Model
class Order:
    def __init__(self, order_id: int, user_id: int, order_date: datetime):
        self.order_id = order_id
        self.user_id = user_id
        self.order_date = order_date
        self.items = []

    def to_dict(self):
        return {"order_id": self.order_id, "user_id": self.user_id, "order_date": self.order_date.isoformat(), "items": self.items}

# Review Model
class Review:
    def __init__(self, review_id: int, user_id: int, product_id: int, rating: int, comment: str):
        self.review_id = review_id
        self.user_id = user_id
        self.product_id = product_id
        self.rating = rating
        self.comment = comment

    def to_dict(self):
        return {"review_id": self.review_id, "user_id": self.user_id, "product_id": self.product_id, "rating": self.rating, "comment": self.comment}