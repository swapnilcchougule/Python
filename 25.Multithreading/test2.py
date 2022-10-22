#!/usr/bin/python3

# https://www.javatpoint.com/multithreading-in-python-3

#import thread			 			# import the thread module  
from _thread import *
__all__ = ("error", "LockType", "start_new_thread", "interrupt_main", "exit", "allocate_lock", "get_ident", "stack_size", "acquire", "release", "locked")
import time 			 			# import time module  
import threading   					# A threading module is made up of a Thread class, which is instantiated to create a Python thread.


def cal_sqre(num): 		 			# define a square calculating function  
    print(" Calculate the square root of the given number")  
    for n in num: 		 			# Use for loop   
        time.sleep(0.3) 	 			# at each iteration it waits for 0.3 time  
        print(' Square is : ', n * n)     		# print Square
  
  
def cal_cube(num):		 			# define a cube calculating function  
    print(" Calculate the cube of  the given number")  
    for n in num: 		 			# for loop  
        time.sleep(0.3) 	 			# at each iteration it waits for 0.3 time  
        print(" Cube is : ", n * n *n)   		# print Cube
  
arr = [4, 5, 6, 7, 2] 					# given array  
t = time.time()                 			# get total time to execute the functions  
print("1.time before executing the functions is :",t) # print it
#cal_cube(arr)  
#cal_sqre(arr)  

# Declaration of the thread parameters: It contains the target function, argument, and kwargs as the parameter in the Thread() class.
# Target: It defines the function name that is executed by the thread.
# Args: It defines the arguments that are passed to the target function name.
th1 = threading.Thread(target=cal_sqre, args=(arr, ))  
th2 = threading.Thread(target=cal_cube, args=(arr, ))  
# A start() method is used to initiate the activity of a thread. And it calls only once for each thread so that the execution of the thread can begin.
th1.start()   
th2.start()  
# A join() method is used to block the execution of another code until the thread terminates.
th1.join()  
th2.join()  
print(" Thread 1 and Thread 2 have finished their execution.")
print(" Total time taking by threads is :", time.time() - t) # print the total time  
print("*" * 50) # print it
t = time.time()                 			# get total time to execute the functions  
cal_cube(arr)  
cal_sqre(arr) 
print(" Total time taking by threads is :", time.time() - t) # print the total time  
  
