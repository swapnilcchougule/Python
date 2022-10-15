#!/usr/bin/python

# creating dictionary
customer = {
 "name": "John Smith",    # key:value pair 
 "age": 28,
 "is_verified": True
}

# Accessing Values in Dictionary
print ("Name of the customer : ", customer["name"])      # returns “John Smith”
print ("age of the customer : ",customer["age"])         # returns “John Smith”

print ("*" * 20 )

# Updating Dictionary
customer["name"] = "John Cena"   # update existing entry
print ("Updated name of the customer : ", customer["name"])        

print ("*" * 20 )

# creating new entry (key-value pair) in dictionary
customer['Company'] = "Bosch";   # Add new entry
print ("New entry in dictionary  ['Company']  : ",customer["Company"])      # returns “John Smith”

print ("*" * 20 )

print (customer)               # returns “dictionary, customer”

print ("*" * 20 )

# Delete Dictionary Elements
del customer['name'];     # remove entry with key 'Name'
print (customer)          # returns “dictionary, customer”

print ("*" * 20 )

customer.clear();         # remove all entries in dict
print (customer)          # returns “dictionary, customer”

print ("*" * 20 )

del customer ;            # delete entire dictionary
# print (customer)          # returns “dictionary, customer”
print ("*" * 20 )

#print (customer["type"]) # throws an error

 
 
 
 
 
