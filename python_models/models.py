from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# In-memory storage for simplicity
users = []
products = []
orders = []
reviews = []

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

# Routes for User
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.to_dict() for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(len(users) + 1, data['name'], data['email'])
    users.append(user)
    return jsonify(user.to_dict()), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u.user_id == user_id), None)
    if user:
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = next((u for u in users if u.user_id == user_id), None)
    if user:
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        return jsonify(user.to_dict())
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u.user_id != user_id]
    return '', 204

# Routes for Product
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify([product.to_dict() for product in products])

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(len(products) + 1, data['name'], data['description'], data['price'])
    products.append(product)
    return jsonify(product.to_dict()), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p.product_id == product_id), None)
    if product:
        return jsonify(product.to_dict())
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    product = next((p for p in products if p.product_id == product_id), None)
    if product:
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        return jsonify(product.to_dict())
    return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p.product_id != product_id]
    return '', 204

# Routes for Order
@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([order.to_dict() for order in orders])

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order = Order(len(orders) + 1, data['user_id'], datetime.now())
    orders.append(order)
    return jsonify(order.to_dict()), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = next((o for o in orders if o.order_id == order_id), None)
    if order:
        return jsonify(order.to_dict())
    return jsonify({"error": "Order not found"}), 404

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data = request.json
    order = next((o for o in orders if o.order_id == order_id), None)
    if order:
        order.user_id = data.get('user_id', order.user_id)
        return jsonify(order.to_dict())
    return jsonify({"error": "Order not found"}), 404

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    global orders
    orders = [o for o in orders if o.order_id != order_id]
    return '', 204

# Routes for Review
@app.route('/reviews', methods=['GET'])
def get_reviews():
    return jsonify([review.to_dict() for review in reviews])

@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.json
    review = Review(len(reviews) + 1, data['user_id'], data['product_id'], data['rating'], data['comment'])
    reviews.append(review)
    return jsonify(review.to_dict()), 201

@app.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = next((r for r in reviews if r.review_id == review_id), None)
    if review:
        return jsonify(review.to_dict())
    return jsonify({"error": "Review not found"}), 404

@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    data = request.json
    review = next((r for r in reviews if r.review_id == review_id), None)
    if review:
        review.rating = data.get('rating', review.rating)
        review.comment = data.get('comment', review.comment)
        return jsonify(review.to_dict())
    return jsonify({"error": "Review not found"}), 404

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    global reviews
    reviews = [r for r in reviews if r.review_id != review_id]
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)