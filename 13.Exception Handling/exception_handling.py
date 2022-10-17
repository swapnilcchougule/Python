#!/usr/bin/python3
# https://www.tutorialspoint.com/python/python_exceptions.htm
try:
	age = int (input("Age: "))
	income = 500
	risk = income / age
	print(age)
except ZeroDivisionError:
	print('Age cabbot be 0.')
except ValueError:
	print('Invalid value')

