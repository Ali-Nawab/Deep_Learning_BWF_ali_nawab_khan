""": A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output."""




glossary = {
    'variable': 'A named storage location in memory used to hold a value.',
    'function': 'A named block of code that performs a specific task.',
    'loop': 'A block of code that repeatedly executes a set of statements while a condition is true.',
    'class': 'A blueprint for creating objects that defines a set of attributes and methods.',
    'module': 'A file containing Python definitions and statements that can be imported and used in other Python code.'
}

for word, meaning in glossary.items():
    print(word.title() + ": " + meaning)
    print() # prints a blank line after each word-meaning pair
