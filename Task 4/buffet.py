# Define a tuple of basic foods offered by a buffet-style restaurant
basic_foods = ('Rice', 'Soup', 'Salad', 'Bread', 'Fruit')

# Print each food offered by the restaurant
print("Foods offered by the restaurant:")
for food in basic_foods:
    print(food)

# Try to modify one of the items and print the error message
try:
    basic_foods[0] = 'Noodles'
except TypeError:
    print("\nTuples are immutable. Cannot modify the items in a tuple.")

# Rewrite the tuple to replace two items with different foods
basic_foods = ('Noodles', 'Soup', 'Pizza', 'Bread', 'Dessert')

# Print each item on the revised menu
print("\nRevised menu:")
for item in basic_foods:
    print(item)
