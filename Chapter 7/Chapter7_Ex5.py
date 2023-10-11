"""
CHAPTER 7 EXERCISE 5 - CITIES 

Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,

such as Reykjavik is in Iceland. Give the parameter for the country a default value.

Call your function for three different cities, at least one of which is not in the default country.

"""
#create a function that accepts city and country 
def describe_city(city ,country = 'United Arab Emirates'):
  print('The city ' + city + ', is in '+ country)

describe_city('Dubai') # Default function
describe_city('Washington DC.',' United States') #unique function 
describe_city('Abu Dhabi')

"""
OUTPUT: 

The city Dubai, is in United Arab Emirates
The city Washington DC., is in  United States
The city Abu Dhabi, is in United Arab Emirates

"""