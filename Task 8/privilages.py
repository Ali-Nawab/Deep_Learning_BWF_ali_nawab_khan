"""Write a separate Privileges class. The class should have one 
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance 
as an attribute in the Admin class. Create a new instance of Admin and use your 
method to show its privileges."""



class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        
    def describe_user(self):
        print(f"{self.first_name} {self.last_name}, {self.age} years old, from {self.location}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name}!")
        
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print(f"Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
        
        
admin = Admin("John", "Doe", 35, "New York")
admin.describe_user()
admin.privileges.show_privileges()


