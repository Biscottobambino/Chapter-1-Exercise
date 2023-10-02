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