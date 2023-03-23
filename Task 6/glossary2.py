"""Now that you know how to loop through a dictionary, clean 
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your 
glossary. When you run your program again, these new words and meanings 
should automatically be included in the output."""

# Initial dictionary of Python terms
python_terms = {
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
}

# Adding five more Python terms
python_terms['set'] = 'A collection of unique elements.'
python_terms['boolean'] = 'A value of either True or False.'
python_terms['module'] = 'A file containing Python code, saved with a .py extension.'
python_terms['function'] = 'A block of code that performs a specific task.'
python_terms['class'] = 'A blueprint for creating objects, which defines a set of attributes and methods.'

# Loop through the dictionary and print each key-value pair
for term, definition in python_terms.items():
    print(f"\n{term.title()}: {definition}")
