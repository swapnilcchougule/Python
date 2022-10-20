#!/usr/bin/python3

# https://www.tutorialspoint.com/python3/python_files_io.htm
# https://www.tutorialspoint.com/python3/os_file_methods.htm
# https://www.tutorialspoint.com/python3/file_methods.htm


# Opens a file for writing only. Overwrites the file if the file exists.
# If the file does not exist, creates a new file for writing.

fo = open("file.txt", "w")  			     
fo.write( "Python is a great language.\nYeah its great!!\n")

print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()		                      # Close opened file
print ("Closed or not : ", fo.closed)


# Opens a file for both reading and writing. The file pointer placed at the beginning of the file.

fo = open("file.txt", "r+")
str = fo.read(100)
print("Read string is :" , str)
#fo.close()		            # Close opened file

# Check current position
position = fo.tell()               # The tell() method tells you the current position within the file;
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)           # The seek(offset[, from]) method changes the current file position
str = fo.read(45)
print ("Again read String is : ", str)

# Reposition pointer at the beginning once again
position = fo.seek(40, 0)
str = fo.read(45)
print ("Again read String is : ", str)

fo.close()		              # Close opened file

import os
os.rename( "file.txt", "file1.txt" ) # os.rename(current_file_name, new_file_name)
#os.remove("file1.txt")              # remove() method to delete files
os.mkdir("test")                     # Create a directory "test"
 

	      
