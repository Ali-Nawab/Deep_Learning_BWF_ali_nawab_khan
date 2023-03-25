filename = 'file.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")
else:
    # Count the number of times 'the' appears in the file
    count = contents.lower().count('the')
    
    # Print the result
    print(f"The word 'the' appears {count} times in the file '{filename}'.")