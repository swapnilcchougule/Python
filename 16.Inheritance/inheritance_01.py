#!/usr/bin/python3

class parent:
	def display(self,Msg):
  		print("This msg is from : ",Msg)


class chlid(parent):
	def father(self):
		print("This is from father class") 
	
	
class grandchlid(parent):
	pass  


obj_c  = chlid() 		# creat object of chlid class
obj_gc = grandchlid()  	# creat object of grandchlid class
obj_c.display('child')
obj_gc.display('grand_child')

obj_c.father()
