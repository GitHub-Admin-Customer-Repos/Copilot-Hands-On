# GitHub Copilot Python Feature Engineering Harder


Let's assume we have a dataset of house prices with the following columns: house_id, num_rooms, num_bathrooms, square_feet, year_built, and price. Use Python with the pandas library.

Step-by-Step Plan:
- Load the dataset.
- Handle missing values.
- Encode categorical variables.
- Create new features:
	- Price per Square Foot: The ratio of the price to the square footage.
	- Age Group: Categorize houses into age groups (e.g., new, mid-age, old).
	- Room to Bathroom Ratio: The ratio of the number of rooms to the number of bathrooms.
	- Log Transformation of Price: The natural logarithm of the price to handle skewness.
	- Use Copilot to generate 2 more features.
- Create interaction features:
	- rooms_x_bathrooms: The product of the number of rooms and bathrooms.
- Scale numerical features.
- Save the engineered dataset.
