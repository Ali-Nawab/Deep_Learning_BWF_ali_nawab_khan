"""Modify the make_shirt() function so that shirts are large 
by default with a message that reads I love Python. Make a large shirt and a 
medium shirt with the default message, and a shirt of any size with a different 
message"""


def make_shirt(size = "large", message = "I love Python"):
    print("The size of the shirt is " + size + " and the message is " + message + ".")
    
make_shirt("medium", "i am studying deep learning")