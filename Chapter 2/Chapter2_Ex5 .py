"""
CHAPTER 2, EXERCISE 5 - USB SHOPPER

A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
You will to use the arithmetic operators to complete this exercise.

"""

Bal=50
USB=6
a=int(Bal/USB)
b=float(Bal-USB*a)
print('She can buy',a,'USBs.')
print('She will have',b,'pounds remaining.')

"""
Output: 
She can buy 8 USBs.
She will have 2.0 pounds remaining.
"""
