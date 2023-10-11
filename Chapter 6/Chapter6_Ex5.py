"""
CHAPTER 6 EXERCISE 5 - NO PASTRAMI 

Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code

near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all

occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

"""
#Create another list for Orders, and finished orders
sandwich_orders= [ 'Pastrami', 'Falafel', 'Meatball','Salami', 'Pastrami', 'Vegan', 'beef', 'pastrami']
finished_sandwiches=[]

print("We're sorry, we don't have anymore pastrami")
while 'Pastrami' in sandwich_orders:
  sandwich_orders.remove('Pastrami')

#once the pastrami is removed from the list, print the remaining sandwiches as normal 
while sandwich_orders: 
  current_sandwich = sandwich_orders.pop()
  print("Im working on your\t" + current_sandwich + " sandwich")
  finished_sandwiches.append(current_sandwich)

print('\n')
for sandwich in finished_sandwiches:
  print("Your order of "+ sandwich +"is ready!")

"""

OUTPUT: 
We're sorry, we don't have anymore pastrami
Im working on your  pastrami sandwich
Im working on your  beef sandwich
Im working on your  Vegan sandwich
Im working on your  Salami sandwich
Im working on your  Meatball sandwich
Im working on your  Falafel sandwich


Your order of pastramiis ready!
Your order of beefis ready!
Your order of Veganis ready!
Your order of Salamiis ready!
Your order of Meatballis ready!
Your order of Falafelis ready!

"""
