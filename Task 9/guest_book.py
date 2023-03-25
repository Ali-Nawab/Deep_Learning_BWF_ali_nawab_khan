"""Write a while loop that prompts users for their name. When 
they enter their name, print a greeting to the screen and add a line recording 
their visit in a file called guest_book.txt. Make sure each entry appears on a 
new line in the file."""

while True: # loop until the user enters 'quit'.
    name = input("Please enter your name: ") # prompt the user for their name.
    if name == 'quit': # if the user enters 'quit', break out of the loop.
        break
    else:
        with open('guest_book.txt', 'a') as file_object: # open the file in append mode.
            file_object.write(name + "has visited the guest book.\n") # write the name to the file.
            print("hello " + name + "! Your name has been added to the guest book.") # print a greeting to the screen.
            
            
