"""
CHAPTER 3, EXERCISE 5 - CHANGE GUEST LIST 
You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.

•Print a second set of invitation messages, one for each person who is still in your list.
"""

# Invitation the dinner party.
guests = ['Darrel Tan', 'Nathan Bartolo', 'Kenlee Labordo']

name = guests[0].title()
print(f"{name}, please come to the party.")

name = guests[1].title()
print(f"{name}, please come to the party.")

name = guests[2].title()
print(f"{name}, please come to the party.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to the party.")

# Darrel can't make it! Let's invite Naomi instead.
del(guests[1])
guests.insert(1, 'Naomi Molina')


name = guests[0].title()
print(f"\n{name}, please come to the party.")

name = guests[1].title()
print(f"\n{name}, please come to the party.")

name = guests[2].title()
print(f"\n{name}, please come to the party.")

""" 
Output: 

Darrel Tan, please come to the party.
Nathan Bartolo, please come to the party.
Kenlee Labordo, please come to the party.

Sorry, Nathan Bartolo can't make it to the party.

Darrel Tan, please come to the party.

Naomi Molina, please come to the party.

Kenlee Labordo, please come to the party.
"""
