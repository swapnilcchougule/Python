#!/usr/bin/python3

# A package is a directory with __init__.py in it. 
# It can contain one or more modules.


import ecommerce.shipping                   # importing the entire shipping module 
ecommerce.shipping.calc_shipping()

from ecommerce import sales                 # importing the entire sales module             
sales.calc_shipping()

from ecommerce.sales import calc_shipping   # importing one function from the sales module
calc_shipping()

from ecommerce.sales import calc_shipping,calc_tax   # importing more function from the sales module
calc_tax()
calc_shipping()
