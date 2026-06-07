from functools import reduce

# Using reduce():
# Find the product of:
numbers = [2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)