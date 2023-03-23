"""Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It 
should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a 
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was 
stored correctly."""

def info_about_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

profile = info_about_car("toyota", "corolla", color="white", year="2019", price="1.5 million")
print(profile)