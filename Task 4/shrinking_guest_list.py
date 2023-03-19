"""
You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two 
names remain in your list. Each time you pop a name from your list, print 
a message to that person letting them know you’re sorry you can’t invite 
them to dinner.
•	 Print a message to each of the two people still on your list, letting them 
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end 
of your program.

"""

names = ['ALI', 'NAWAB', 'KHAN', 'BANGASH']
print("We have found a bigger dinner table so we can invite more people")
names.insert(0, 'HASSAN')
names.insert(2, 'HANIF')
names.append('SHAHID')

print(names)
print("We can invite only two people for dinner")
names.pop()
names.pop(0)
names.remove('HANIF')
names.remove('KHAN')
names.pop(2)

print(names[0].title() + " You are invited in dinner")
print(names[1].title() + " You are invited in dinner")

print(names)

#del names[0]
#del names[1]
#del names[-2]
#del names[-1]

print(names)