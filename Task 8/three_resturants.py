"""Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance."""


class Resturant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")
        
restaurant = Resturant("pizza hut", "italian")
hotel = Resturant("hotel", "pakistani")
daba = Resturant("daba", "chinese")

restaurant.describe_restaurant()
hotel.describe_restaurant()
daba.describe_restaurant()