#!/usr/bin/python3

class Parent:                        # define parent class
	parentAttr = 100
	def __init__(self):
		print ("calling parent constructor")
		
		
	def ParentMethod(self):
		print("calling parent method")
		
		
	def setAttr(self, attr):
      		Parent.parentAttr = attr
	
	
	def getAttr(self):
		print ("Parent attribute :", Parent.parentAttr)
			
class Child(Parent):
	def __init__(self):
		print ("calling child constructor")


	def ChildMethod(self):
		print("calling parent method")
				

c = Child()          # instance of child
c.ChildMethod()      # child calls its method
c.ParentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

