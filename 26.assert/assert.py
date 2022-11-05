#!/usr/bin/python3

# https://www.codecademy.com/resources/docs/python/assert
# syntax : assert some_condition, assert_message
# The assert keyword can be used to validate a value (or evaluate some other condition):


fav_color = 'blue'
assert fav_color == 'blue' , 'Yes, the color is fav_color'

things_that_float = ['bread', 'apples', 'small rocks','mud1']
assert 'mud' in things_that_float, 'this string is not present in the list'
