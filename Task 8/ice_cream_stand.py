"""An ice cream stand is a specific kind of restaurant. Write 
a class called IceCreamStand that inherits from the Restaurant class you wrote 
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of 
the class will work; just pick the one you like better. Add an attribute called 
flavors that stores a list of ice cream flavors. Write a method that displays 
these flavors. Create an instance of IceCreamStand, and call this method."""

from three_resturants import Resturant

class IceCreamStand(Resturant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
        
    def display_flavors(self):
        print("Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")
            
ice_cream_stand = IceCreamStand(restaurant_name="ice cream stand", cuisine_type="ice cream")
ice_cream_stand.flavors = ["vanilla", "chocolate", "strawberry"]
ice_cream_stand.display_flavors()
