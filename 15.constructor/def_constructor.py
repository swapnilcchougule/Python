#!/usr/bin/python3

# __init__ is a special method called constructor. It gets called at the time of
# creating new objects. We use it to initialize our objects.
# self is refrence to current object

class class_Name:                    # class class_Name:
	def __init__(self):          # default constructor:
		print("Constructor invocked")     

class_Name()          # create an objects to check constructor
obj1 = class_Name()   # create object of class class_Name and store in var obj1

