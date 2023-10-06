"""
CHAPTER 3, EXERCISE 6 - SHRINKING GUEST LIST 
You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.

•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

•Print a message to each of the two people still on your list, letting them know they’re still invited.

•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.    

"""

# Invite some people to dinner.
guests = ['Kenlee Labordo', 'Jim Daniel', 'Michael Massi']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

# Kenlee can't make it! Let's invite Yerahmiel instead.
del(guests[1])
guests.insert(1, 'Yerahmiel Sanchez')

# Print the invitations again.
name = guests[0].title()
print(f"\n{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

# We have a bigger table, so let's add some more people to the list.
print("\nWe have a bigger table!")
guests.insert(0, 'Nathan Bartolo')
guests.insert(2, 'James Magdangal')
guests.append('Caleb Hart')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

"""
Output:

Darrel Tan, please come to the party.
Nathan Bartolo, please come to the party.
Kenlee Labordo, please come to the party.

Sorry, Nathan Bartolo can't make it to the party.
Kenlee Labordo, please come to dinner.
Jim Daniel, please come to dinner.
Michael Massi, please come to dinner.

Sorry, Jim Daniel can't make it to dinner.

Kenlee Labordo, please come to dinner.
Yerahmiel Sanchez, please come to dinner.
Michael Massi, please come to dinner.

We have a bigger table!
Nathan Bartolo, please come to dinner.
Kenlee Labordo, please come to dinner.
James Magdangal, please come to dinner.
Yerahmiel Sanchez, please come to dinner.
Michael Massi, please come to dinner.
Caleb Hart, please come to dinner.

"""
