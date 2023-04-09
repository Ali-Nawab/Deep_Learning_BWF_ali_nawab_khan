class Employee:
    company_name = "Google"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee is created!")
    
    def show_details(self):
        print(f"Employee name is {self.name} and salary is {self.salary} in {self.company_name}")
        
    @classmethod
    def class_method(cls, name):
        Employee.company_name = name
        
    
e1 = Employee("Ali", 1000) # Employee is created!

e1.show_details() # Employee name is Ali and salary is 1000 in Google

Employee.class_method("Microsoft") # Company name is changed for all instances.

e1.show_details() # Employee name is Ali and salary is 1000 in Microsoft

e2 = Employee("Nawab", 2000) # Employee is created!

e2.company_name = "Amazon" # Company name is changed for e2 instance only.

e2.show_details() # Employee name is Nawab and salary is 2000 in Amazon