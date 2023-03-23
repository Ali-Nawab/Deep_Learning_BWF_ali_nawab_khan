"""Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. Call show_magicians() to 
see that the list has actually been modified."""


def make_great(magicians):
    for magician in magicians:
        print("The Great " + magician)
        
magicians = ["Ali", "Ahmed", "Asad", "Ahsan"]
print(make_great(magicians))