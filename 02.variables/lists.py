#!usr/bin/python3

# theory @ https://www.tutorialspoint.com/python/python_lists.htm
# lists :- datatype list of comma-separated values (items) between square brackets.

# creating lists

list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

# Accessing Values in Lists

print (list1[0])
print (list2[0:4])
print (list3[2:])

print ("*" * 50)     

# Updating Lists
list1[0] = "Maths"
print(list1)

print ("*" * 50)     

# Delete List Elements
del list2[2];
print(list2)

print ("*" * 50)     

# Basic List Operations
print(list1)          # Prints complete list
print(list1[0])       # Prints first element of the list
print(list1[-1])      # Prints last element of the list
print(list1[0:3])     # Prints elements of the list starting from 0th till 3rd
print (list1[1:])     # Prints elements of the list starting from 0th element
print(list1 + list2 + list3)  # Prints concatenated list
print(list2 * 5)      # Prints the contents of the list 5 times 
print (len(list1))    # Length
print (2 in list2)    # Membership (result TRUE if 2 is available in list2) 
for x in [list2]: print (x) # iteration in list
for x in list2: print (x) # iteration in list
list3.append("e")         # adds "e" to the end
print(list3)
list3.insert(0, "e") # adds "e" at index position of 0
print(list3)
list3.remove('e')
print(list3)
List4 = [9,8,7,6,5,'a','d','c','b','B','A','C','D', 'zara', 'abc', 'xyz'];
print(List4.sort())



