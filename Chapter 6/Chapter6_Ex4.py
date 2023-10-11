"""
CHAPTER 6 EXERCISE 4 - DELI 

Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,

move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

"""

#Create another list for Orders, and finished orders
sandwich_orders= [ 'Pastrami', 'Falafel', 'Meatball','Salami']
finished_sandwiches=[]

#Loop through the list of sandwich orders and print a message for each order
while sandwich_orders: 
  current_sandwich = sandwich_orders.pop()
  print("Im working on your\t" + current_sandwich + " sandwich")
  finished_sandwiches.append(current_sandwich)
#Once the order is done, display a message telling the user their sandwich is ready. 
print('\n')
for sandwich in finished_sandwiches:
  print("Your order of "+ sandwich +"is ready!")

"""
OUTPUT - 

Im working on your  Salami sandwich
Im working on your  Meatball sandwich
Im working on your  Falafel sandwich
Im working on your  Pastrami sandwich


Your order of Salamiis ready!
Your order of Meatballis ready!
Your order of Falafelis ready!
Your order of Pastramiis ready!

"""

  
  