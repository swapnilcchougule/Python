#!/usr/bin/python3    

# We can define strings using single (‘ ‘) or double (“ “) quotes. 
# To define a multi-line string, we surround our string with tripe quotes (“””). 

name = 'swapnil chougule'
print(name)
print(name[0])   # returns the first character
print(name[1])   # returns the second character
print(name[-1])  # returns the first character from the end 
print(name[-2])  # returns the second character from the end 
print(name[0:6]) # We can slice a string using a similar notation: 

message = f'Hi, my name is {name}'
print(message)

print(message.upper())   # to convert to uppercase
print(message.lower())   # to convert to lowercase
print(message.title())   # to capitalize the first letter of every word
print(message.find('H')) # returns the index of the first occurrence of p(or -1 if not found)
print(message.find('h')) # returns the index of the first occurrence of p(or -1 if not found)
print(message.find('z')) # returns the index of the first occurrence of p(or -1 if not found)

print(message.replace('p', 'q')) # replace p by q
contains ='chougule' in message # To check if a string contains a character (or a sequence of characters), we use the in operator:
print (contains)


