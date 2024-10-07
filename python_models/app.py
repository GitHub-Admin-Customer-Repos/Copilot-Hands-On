import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime
from models import User, Product, Order, Review

# In-memory storage for simplicity
users = []
products = []
orders = []
reviews = []

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _parse_body(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        return json.loads(post_data)

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')
        if len(path_parts) == 1:
            if path_parts[0] == 'users':
                self._set_headers()
                self.wfile.write(json.dumps([user.to_dict() for user in users]).encode())
            elif path_parts[0] == 'products':
                self._set_headers()
                self.wfile.write(json.dumps([product.to_dict() for product in products]).encode())
            elif path_parts[0] == 'orders':
                self._set_headers()
                self.wfile.write(json.dumps([order.to_dict() for order in orders]).encode())
            elif path_parts[0] == 'reviews':
                self._set_headers()
                self.wfile.write(json.dumps([review.to_dict() for review in reviews]).encode())
        elif len(path_parts) == 2:
            resource, resource_id = path_parts
            resource_id = int(resource_id)
            if resource == 'users':
                user = next((u for u in users if u.user_id == resource_id), None)
                if user:
                    self._set_headers()
                    self.wfile.write(json.dumps(user.to_dict()).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "User not found"}).encode())
            elif resource == 'products':
                product = next((p for p in products if p.product_id == resource_id), None)
                if product:
                    self._set_headers()
                    self.wfile.write(json.dumps(product.to_dict()).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Product not found"}).encode())
            elif resource == 'orders':
                order = next((o for o in orders if o.order_id == resource_id), None)
                if order:
                    self._set_headers()
                    self.wfile.write(json.dumps(order.to_dict()).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Order not found"}).encode())
            elif resource == 'reviews':
                review = next((r for r in reviews if r.review_id == resource_id), None)
                if review:
                    self._set_headers()
                    self.wfile.write(json.dumps(review.to_dict()).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Review not found"}).encode())

    def do_POST(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')
        if len(path_parts) == 1:
            resource = path_parts[0]
            data = self._parse_body()
            if resource == 'users':
                user = User(len(users) + 1, data['name'], data['email'])
                users.append(user)
                self._set_headers(201)
                self.wfile.write(json.dumps(user.to_dict()).encode())
            elif resource == 'products':
                product = Product(len(products) + 1, data['name'], data['description'], data['price'])
                products.append(product)
                self._set_headers(201)
                self.wfile.write(json.dumps(product.to_dict()).encode())
            elif resource == 'orders':
                order = Order(len(orders) + 1, data['user_id'], datetime.now())
                orders.append(order)
                self._set_headers(201)
                self.wfile.write(json.dumps(order.to_dict()).encode())
            elif resource == 'reviews':
                review = Review(len(reviews) + 1, data['user_id'], data['product_id'], data['rating'], data['comment'])
                reviews.append(review)
                self._set_headers(201)
                self.wfile.write(json.dumps(review.to_dict()).encode())

    def do_PUT(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')
        if len(path_parts) == 2:
            resource, resource_id = path_parts
            resource_id = int(resource_id)
            data = self._parse_body()
            if resource == 'users':
                user = next((u for u in users if u.user_id == resource_id), None)
                if user:
                    user.name = data.get('name', user.name)
                    user.email = data.get('email', user.email)
                    self._set_headers()
                    self.wfile.write(json.dumps(user.to_dict()).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "User not found"}).encode())
            elif resource == 'products':
                product = next((p for p in products if p.product_id == resource_id), None)
                if product:
                    product.name = data.get('name', product.name)
                    product.description = data.get('description', product.description)
                    product.price = data.get('price', product.price)
                    self._set_headers()
                    self.wfile.write(json.dumps(product.to_dict()).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Product not found"}).encode())
            elif resource == 'orders':
                order = next((o for o in orders if o.order_id == resource_id), None)
                if order:
                    order.user_id = data.get('user_id', order.user_id)
                    self._set_headers()
                    self.wfile.write(json.dumps(order.to_dict()).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Order not found"}).encode())
            elif resource == 'reviews':
                review = next((r for r in reviews if r.review_id == resource_id), None)
                if review:
                    review.rating = data.get('rating', review.rating)
                    review.comment = data.get('comment', review.comment)
                    self._set_headers()
                    self.wfile.write(json.dumps(review.to_dict()).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({"error": "Review not found"}).encode())

    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.strip('/').split('/')
        if len(path_parts) == 2:
            resource, resource_id = path_parts
            resource_id = int(resource_id)
            if resource == 'users':
                global users
                users = [u for u in users if u.user_id != resource_id]
                self._set_headers(204)
            elif resource == 'products':
                global products
                products = [p for p in products if p.product_id != resource_id]
                self._set_headers(204)
            elif resource == 'orders':
                global orders
                orders = [o for o in orders if o.order_id != resource_id]
                self._set_headers(204)
            elif resource == 'reviews':
                global reviews
                reviews = [r for r in reviews if r.review_id != resource_id]
                self._set_headers(204)

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()