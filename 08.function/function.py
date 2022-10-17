#!/usr/bin/python3

# Function definition is here

def printme(str):
   "This prints a passed string into this function"
   print (str)


def greet(name):
   print (f'Hi welcome {name} ..!')   # formated string
   
   
def square(number):
	return number * number   
	  

# function call
printme("First call..!")
printme("Second call..!")
greet( "john" )            # pass argument "john" to parameter "name"
greet( "Swapnil" )
result = square(5)
print(result) 
