#!/usr/bin/python3

# https://www.tutorialspoint.com/python/python_multithreading.htm
# https://www.javatpoint.com/multithreading-in-python-3

#import thread			 			# import the thread module  
from _thread import *
__all__ = ("error", "LockType", "start_new_thread", "interrupt_main", "exit", "allocate_lock", "get_ident", "stack_size", "acquire", "release", "locked")
import time 			 			# import time module  
import threading   					# A threading module is made up of a Thread class, which is instantiated to create a Python thread. 

def print_time(threadName):
	count=0
	while count < 5:
		time.sleep(0.3)
		count +=1
		print ("Thread running : ",threadName,count)
		
			
try:
	th1 = threading.Thread(target=print_time, args=('Thr-1 :', ))   
	th2 = threading.Thread(target=print_time, args=('Thr-2 :', ))                 
	th1.start()   
	th2.start() 
except:
	print ("Error: unable to start thread")
while 1:
   pass
