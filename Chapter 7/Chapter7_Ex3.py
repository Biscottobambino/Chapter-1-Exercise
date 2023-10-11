"""
CHAPTER 7 EXERCISE 3 - T-SHIRT 

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional

arguments to make a shirt. Call the function a second time using keyword arguments.

"""
#Create a function with positional arguments
def make_shirt(size,message):
  #Create statement about the size and message of your tshirt. 
  print("\nMy Tshirt's size is going to be " + size )
  print('The shirt will say, "' + message + '"')

make_shirt('medium', 'Star wars the clone wars ') #call by value
make_shirt(message="Revenge of the sith", size='Large') #Call by Reference

"""
OUTPUT: 

My Tshirt's size is going to be medium
The shirt will say, "Star wars the clone wars "

My Tshirt's size is going to be Large
The shirt will say, "Revenge of the sith"

"""