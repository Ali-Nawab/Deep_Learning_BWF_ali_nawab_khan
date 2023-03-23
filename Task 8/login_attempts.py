"""Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write 
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented 
properly, and then call reset_login_attempts(). Print login_attempts again to 
make sure it was reset to 0.
"""


class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is a {self.age}-year-old {self.gender}.")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0



# Create a user
user1 = User("John", "Doe", 25, "male")

# Increment login attempts
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# Check login attempts
print(f"Login attempts: {user1.login_attempts}")

# Reset login attempts
user1.reset_login_attempts()

# Check login attempts again
print(f"Login attempts after reset: {user1.login_attempts}")


