""": Make a dictionary containing three major rivers and the country 
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs 
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary."""


# Create a dictionary of three major rivers and the countries they run through
rivers = {
    'Amazon': 'Brazil',
    'Nile': 'Egypt',
    'Yangtze': 'China'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print the name of each river
print("\nThe following rivers are included in the dictionary:")
for river in rivers.keys():
    print(river)

# Print the name of each country
print("\nThe following countries are included in the dictionary:")
for country in rivers.values():
    print(country)


