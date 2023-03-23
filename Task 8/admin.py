"""An administrator is a special kind of user. Write a class called 
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) 
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list 
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of 
privileges. Create an instance of Admin, and call your method."""

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
        
class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        print(f"Admin privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
            
admin = Admin("John", "Doe", 35, "New York")
admin.describe_user()
admin.show_privileges()

