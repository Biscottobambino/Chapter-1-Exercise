"""
CHAPTER 7 EXERCISE 4 - LARGE SHIRTS 

Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function

should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional

arguments to make a shirt. Call the function a second time using keyword arguments.
"""
#Create a function, and set default size to large, and the message to 'i love python'
def make_shirt(size = 'large',message = 'I love python'):
  #Create statement about the size and message of your tshirt. 
  print("\nMy Tshirt's size is going to be " + size )
  print('The shirt will say, "' + message + '"')

make_shirt()#call default function
#call function by positional, and keyword arguments vvv
make_shirt('medium','may the force be with you') 
make_shirt(message = 'do or do not, there is no try', size = 'small')

"""
OUTPUT: 

My Tshirt's size is going to be large
The shirt will say, "I love python"

My Tshirt's size is going to be medium
The shirt will say, "may the force be with you"

My Tshirt's size is going to be small
The shirt will say, "do or do not, there is no try"
"""