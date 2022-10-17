#!/usr/bin/python3

matrix = [
[1,2,3],          # 1st row
[21,22,23],       # 2nd row
[31,32,33]        # 3rd row
]

print(matrix)
print(matrix[0][0])
print(matrix[2][2])

# iterating in matrix
for row in matrix:             # iterating rows
	for item in row:       # iterating column 
		print(item)

