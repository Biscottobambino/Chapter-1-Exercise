"""
CHAPTER 6 EXERCISE 2 - MOVIE TICKETS 

A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if

they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their

age, and then tell them the cost of their movie ticket

"""
#create a prompt that asks user age 
Question1 = "How old are you?"
Question1 += "\nEnter 'finished' when you are done. "

while True: 
    age = input(Question1) 
    if age == 'finished':#once the user is done, they type 'finished'
        break
    age = int(age)
#create statement, that determines age by price of tickets. 
    if age < 3:
        print("  You're free to enter!'")
    elif age < 13:
        print("  Your ticket will cost you $10.")
    else:
        print("  Your ticket will cost you $15.")


"""
OUTUT: 

How old are you?
Enter 'finished' when you are done. - 6
  Your ticket will cost you $10.
How old are you?
Enter 'finished' when you are done. - 15
  Your ticket will cost you $15.
How old are you?
Enter 'finished' when you are done. - finished 

"""