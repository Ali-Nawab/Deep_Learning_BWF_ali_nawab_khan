"""Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods."""



class Resturant:
    def __init__(self):
        self.restaurant_name = "Pizza Hut"
        self.cuisine_type = "Italian"
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")
        
restaurant = Resturant()
restaurant.describe_restaurant()
restaurant.open_restaurant()