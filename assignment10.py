# Define the list of children
children = [
    {"name": "Alice", "age": 2, "height": 95},
    {"name": "Bob", "age": 4, "height": 105},
    {"name": "Charlie", "age": 3, "height": 110},
    {"name": "David", "age": 5, "height": 102},
    {"name": "Eve", "age": 6, "height": 99}
]

# Define the lambda function for eligibility criteria
criteria = lambda child: child['age'] > 3 and child['height'] > 100

# Filter the list of children using the criteria lambda function
eligible_children = list(filter(criteria, children))

# Print the eligible children
print("Eligible children for the fun park:", eligible_children)
