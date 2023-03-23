""" Ordinal numbers indicate their position in a list, such 
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
•	 Store the numbers 1 through 9 in a list.
•	 Loop through the list.
•	 Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 
7th 8th 9th", and each result should be on a separate line.
"""

current_users = ['john', 'mary', 'jane', 'steve', 'mike']
new_users = ['joe', 'JANE', 'steve', 'carol', 'MIKE']

for user in new_users:
    if user.lower() in [u.lower() for u in current_users]:
        print(f"Sorry, {user} is already taken. Please enter a new username.")
    else:
        print(f"Great, {user} is available!")