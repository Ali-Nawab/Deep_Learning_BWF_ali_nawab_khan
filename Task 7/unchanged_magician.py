"""Start with your work from Exercise 8-10. Call the 
function make_great() with a copy of the list of magicians’ names. Because the 
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.
"""

def make_great(magicians):
    """Add 'Great' to each magician's name."""
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = "Great " + magician
        great_magicians.append(great_magician)
    return great_magicians

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

# Start with a list of magicians
magicians = ['David Copperfield', 'David Blaine', 'Harry Houdini', 'Penn Jillette', 'Teller']

# Make a copy of the list and add "Great" to each magician's name
great_magicians = make_great(magicians[:])

# Show the original list of magicians
print("\nOriginal list of magicians:")
show_magicians(magicians)

# Show the new list of great magicians
print("\nList of 'Great' magicians:")
show_magicians(great_magicians)

