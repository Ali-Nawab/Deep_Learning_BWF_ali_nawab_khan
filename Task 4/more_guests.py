"""
You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the 
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still 
in your list.

"""

names = ['ALI', 'NAWAB', 'KHAN', 'BANGASH']
print("We have found a bigger dinner table so we can invite more people")
names.insert(0, 'HASSAN')
names.insert(2, 'HANIF')
names.append('SHAHID')

print(names[0].title() + " You are invited in dinner")
print(names[1].title() + " You are invited in dinner")
print(names[2].title() + " You are invited in dinner")
print(names[3].title() + " You are invited in dinner")
print(names[4].title() + " You are invited in dinner")
print(names[5].title() + " You are invited in dinner")
print(names[6].title() + " You are invited in dinner")
