""": Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include 
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have 
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take 
the poll.
"""


# favorite_languages.py code
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# List of people who should take the poll
people_to_poll = ['jen', 'phil', 'mike', 'susan']

# Loop through the list of people who should take the poll
for person in people_to_poll:
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for responding to the poll.")
    else:
        print(f"{person.title()}, please take the poll and let us know your favorite programming language!")
