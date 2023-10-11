"""
CHAPTER 6 EXERCISE 1 - PIZZA TOPPINGS 

Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,

print a message saying you’ll add that topping to their pizza.

"""
#Ask the user what toppings they want with prompt

prompt = "\nWhat pizza toppings do you fancy?"
prompt += "\nEnter 'finished' when you are done: "

# User input their toppings. Then once they are done they type 'finished' to break the loop. 
while True:
    topping = input(prompt)
    if topping != 'finished':
        print("  So, you'll have " + topping + " on your pizza.")
    else:
        break

"""
Output - 

What pizza toppings do you fancy?
Enter 'finished' when you are done: Peperoni 
  So, you'll have Peperoni  on your pizza.

What pizza toppings do you fancy?
Enter 'finished' when you are done: finished
 

"""