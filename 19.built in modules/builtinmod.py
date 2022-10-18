#!/usr/bin/python3

import random          # import built in module

for i in range(5):
	print(random.random())
	
print('*' * 50)
	
for i in range(5):
	print(random.randint(10,100))
	
print('*' * 50)
	
members = ['john','mery','bob','sam']
leader = random.choice(members)
print(leader)

print('*' * 50)

dice = (1,2,3,4,5,6)
roll = random.choice(dice)
print(roll)

print('*' * 50)

class Dice_2:
	def roll(self):
		first = random.randint(1,6)
		second = random.randint(1,6)
		return first,second
		
dice_2 = Dice_2()		
print(dice_2.roll())		
		
		
		
		
		
		
		
		
		
		

