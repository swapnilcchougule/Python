#!/usr/bin/python3

# https://www.tutorialspoint.com/python3/python_exceptions.htm

try:
	fh = open ("file", "w")
	fh.write("This is text to be written in the file")
except IOError:
	print ("Error: can\'t find file or read data")
else:
	print ("Written content in the file successfully")
fh.close()	


try:
	fh = open("testfile", "r")
	fh.write("This is my test file for exception handling!!")
except IOError:
	print ("Error: can\'t find file or read data")
else:
	print ("Written content in the file successfully")
fh.close()	


def functionName( level ):
   if level <1:
      raise Exception(level)
      # The code below to this would not be executed
      # if we raise the exception
   return level


try:
   l = functionName(10)
   print ("level = ",l) 
     
   l = functionName(10)
   print ("level = ",l)
      
   l = functionName(-10)
   print ("level = ",l)
      
   l = functionName(10)
   print ("level = ",l)
      
   l = functionName(10)  
   print ("level = ",l)
             
except Exception as e:
   print ("error in level argument",e.args[0])
   
   
   
   
   
   
   
   
   
   
