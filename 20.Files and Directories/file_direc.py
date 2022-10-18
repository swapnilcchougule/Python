#!/usr/bin/python3

# pathlib — Object-oriented filesystem paths
# https://docs.python.org/3/library/pathlib.html#module-pathlib

from pathlib import Path     # import Path from 

path = Path('ecommerce')

for file in path.glob('*'):   # itterate through folder ecommerce     
	print(file)           # show all files in folder ecommerce
	
print (path.exists())         # does path to ecommerce exist ?
print(path.cwd())             # show current working directory      

Path1 = Path('emails')        
print(Path1.exists())         # does path to emails exist ?          
#Path1.mkdir()                 # make email directors
print(Path1.exists())

	
