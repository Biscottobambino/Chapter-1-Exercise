"""
CHAPTER 1, EXERCISE 3 - PRINT DATE AND TIME 

Write a Python program to display the current date and time.
"""

import datetime #import date time function 
now = datetime.datetime.now()
print ('current date and time')
print(now.strftime("%Y-%m-d%H:%M:S"))

"""
Output:

current date and time
2023-10-d14:23:S

"""
