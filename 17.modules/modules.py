#!/usr/bin/python3

# A module is a file with some Python code. 
# We use modules to break up our program into multiple files. 
# There are 2 ways to import modules: we can 
# 1. import the entire module 
# 2. import specific objects in a module.

import converters                         # importing the entire converters module
print(converters.kg_to_lbs(70))

from converters import lbs_to_kg          # importing one function in the converters module
print(lbs_to_kg(155.55555555555554))

import math                               # Import built-in module math
print(dir(math))

