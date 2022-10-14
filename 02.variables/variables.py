#!/usr/bin/python3    

#We use variables to temporarily store data in computer’s memory. 

# int , float and string

price = 10
rating = 4.5
name = 'Swapnil'
is_published = True
print(price, ': price is an integer (a whole number without a decimal point)')
print(rating,": rating is a float (a number with a decimal point)")
print(name,": name is a string (a sequence of characters)")
print(is_published,": is_published is a boolean. Boolean values can be True or False.")
print (name[2:])      # Prints string starting from 3rd character

# Multiple Assignment

a = b = c = 1  
print(a,b,c)
a,b,c = 1,2,"john"
print(a,b,c)

# Python Lists -> []
# elements and size can be changed

list1 = [ 'abcd', 786 , 2.23, 'john', 70.2 ]  
list2 = [123, 'cena', name]

print(list1)          # Prints complete list
print(list1[0])       # Prints first element of the tuple
print(list1[0:3])     # Prints elements of the tuple starting from 0th till 3rd
print (list1[1:])     # Prints elements of the tuple starting from 0th element
print(list1 + list2)  # Prints concatenated list
print(list2 * 5)      # Prints the contents of the tuple 5 times      

list1[2] = 1000     # Valid syntax with list
print (list1)     


# Python Tuples -> ()
# Tuples can be thought of as read-only lists and cannot be updated.

tuple1 = ( 'abcd', 786 , 2.23, 'john', 70.2 ) 
tuple2 = (123, 'cena', name)

print(tuple1)          # Prints complete list
print(tuple1[0])       # Prints first element of the tuple
print(tuple1[0:3])     # Prints elements of the tuple starting from 0th till 3rd
print (tuple1[1:])     # Prints elements of the tuple starting from 0th element
print(tuple1+ tuple2)  # Prints concatenated list
print(tuple2 * 5)      # Prints the contents of the tuple 5 times      
# tuple1[2] = 500      # inalid syntax with tuple
# print (tuple1)     












           

