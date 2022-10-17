#!/usr/bin/python3
class Point:                     # class class_Name:
	def move(self):           # member function move
		print("move")
	

	def draw(self):           # member function draw
		print("draw")
		
				
	def __init__(self):
		print("Constructor invocked")

Point()  # create an objects to check constructor

print('*' * 50)

obj1=Point()	# create object of class point and store in var obj1
obj1.move()     # call function move using object
obj1.draw()     # call function draw using object

print('*' * 50)

obj1.x=10      # create attribute x 
obj1.y=20      # create attribute y
print(obj1.x)
print(obj1.y)



