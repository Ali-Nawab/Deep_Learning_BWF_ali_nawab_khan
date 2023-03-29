name = input("Please enter your name: ")

with open('guest.txt', 'w') as file_object:
    file_object.write(name)
    print("Hello, " + name + "! Your name has been added to the guest book.")

