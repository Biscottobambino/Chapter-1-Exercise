"""
CHAPTER 2, EXERCISE 3 - STRIPPING NAMES 

Tidy up the code to make it easier to understand
Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.
Print the name once, so the whitespace around the name is displayed.
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip()
"""
name = "\tKenlee Perez Labordo\n"

print("unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

"""
Output
unmodified:
    Kenlee Perez Labordo


Using lstrip():
Kenlee Perez Labordo


Using rstrip():
    Kenlee Perez Labordo

Using strip():
Kenlee Perez Labordo
"""
