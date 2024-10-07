# GitHub Copilot Python Models Labs

We will be using a simple api project to practice enhancing an existing project with new functionality.  The project is a simple API that manages users and orders.  The project is written in Python and uses the Flask web framework.

# Directions

Use Copilot to determine the best way to enhance the project with new functionality.  This can include asking Copilot for how it thinks we can enhance the project as well as the code to implement the new functionality.

- Add Update Methods: Add methods to update fields of the models.
- Add Validation Methods: Add methods to validate the data before saving or updating.
- Manage Relationships: Add methods to manage relationships between models, such as adding items to an order
- Update the unit tests in app_tests.py to test the new functionality.

For example, below we update the User model to include update methods for name and email.  We then add validation to ensure name and email fields are not empty.

```
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {"user_id": self.user_id, "name": self.name, "email": self.email}

    def update(self, name: str = None, email: str = None):
        if name:
            self.name = name
        if email:
            self.email = email

    def validate(self):
        if not self.name or not self.email:
            raise ValueError("Name and email cannot be empty")
```
