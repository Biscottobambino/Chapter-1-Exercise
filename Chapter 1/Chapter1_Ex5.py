"""
Chapter 1 Exercise 5 
Write a Python program which accepts the radius of a circle from the user and compute the area.


"""

from math import pi

r=float(input("input the radius of the circle ="))
print("the area of the circle with radius" + str(r) + "is" + str(pi *r**2))
