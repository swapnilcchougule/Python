#!/usr/bin/python3
list1 = [1,2,2,3,3,4,55,55,6,7,8,9] # list with duplicates
unique = []                         # list with removed duplicates
for number in list1:
	if number not in unique:
		unique.append(number)
print(unique)
