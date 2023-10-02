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
