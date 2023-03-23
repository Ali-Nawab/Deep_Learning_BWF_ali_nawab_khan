"""Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite 
number for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few 
friends and get some actual data for your program."""


favorite_numbers = {
    'Alice': 42,
    'Bob': 7,
    'Charlie': 13,
    'Dave': 23,
    'Eve': 17
}

for name, number in favorite_numbers.items():
    print(name + "'s favorite number is " + str(number))
