#!/usr/bin/python3

# https://www.javatpoint.com/multithreading-in-python-3

#import thread # import the thread module  

from _thread import *
__all__ = ("error", "LockType", "start_new_thread", "interrupt_main", "exit", "allocate_lock", "get_ident", "stack_size", "acquire", "release", "locked")
import time			  					# import time module  
  
  
def cal_sqre(num): 		  					# define the cal_sqre function  
    print(" Calculate the square root of the given number")  
    for n in num:   
        time.sleep(0.3)          					# at each iteration it waits for 0.3 time  
        print(' Square is : ', n * n)   				# print Square
  
  
def cal_cube(num): # define the cal_cube() function  
    print(" Calculate the cube of  the given number")  
    for n in num:   
        time.sleep(0.3) 						# at each iteration it waits for 0.3 time  
        print(" Cube is : ", n * n *n)				# print Cubes
 
  
arr = [4, 5, 6, 7, 2] # given array  
t1 = time.time()                                        		# get total time to execute the functions  
print("1.time before executing the functions is :", t1) 		# print it
cal_sqre(arr) 						  		# call cal_sqre() function  
t2 = time.time()                                        		# get total time to execute the functions  
print("2. total time to execute the cal_sqre fun is :", t2-t1) 	# print it
cal_cube(arr) 								# call cal_cube() function  
t3 = time.time()                                       		# get total time to execute the functions  
print("3. total time to execute the cal_sqre fun is :", t3-t2) 	# print it
print(" Total time taken by threads is :", time.time() - t1) 	# print the total time  





