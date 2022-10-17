#!/usr/bin/python3

# __init__ is a special method called constructor. It gets called at the time of
# creating new objects. We use it to initialize our objects.
# self is refrence to current object
   
class Car: 
	def __init__(self,brand,model,year,owner):          # Paramaterized constructor:	
		self.brand = brand                    # Attribute1
		self.model = model                    # Attribute2
		self.year = year                      # Attribute3
		self.owner = owner                    # Attribute4
		print ("brand :",self.brand,"\n" "model: ", self.model,"\n" "year: ", self.year)
	
	
	def display(self):	                      # Attribute5
		print ("The car details are : ",self.brand, self.model, self.year)
	def display_owner(self):	                      # Attribute5
		print ("owner :",self.owner,"\n")	 	

	 	
Car('a','b','c','d')	        # create an objects to check constructor	
car_obj1 = Car("Audi","A5",2023,'john')   # create object of class class_Name and store in var obj1
car_obj1.display()

print(hasattr(car_obj1, 'brand'))    # Returns true if 'brand' attribute exists
print(getattr(car_obj1, 'brand'))    # Returns value of 'brand' attribute
setattr(car_obj1, 'brand', 'BMW')    # Set attribute 'brand' as BMW
car_obj1.display()
car_obj1.display_owner()
delattr(car_obj1, 'owner')           # Delete attribute 'age'
car_obj1.display_owner()




