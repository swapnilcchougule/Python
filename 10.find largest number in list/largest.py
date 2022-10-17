#!/usr/bin/python3
#find the largest number in the list1s
list1 = [1,2,3,4,55,6,7,8,9]
Max =list1[0]
for number in list1:
	if number > Max:
		Max = number 
print(Max)
