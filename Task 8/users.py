"""Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user’s information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user"""


class User:
    def __init__(self):
        self.first_name = "ALI NAWAB KHAN"
        self.last_name = "BANGASH"
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
        
user = User()
user.describe_user()
user.greet_user()