"""
This program calculates the number of islands in a 2D-matrix.
An island is a one or a group of ones.
This program does not factor in ones arrange diagonally.
"""
def countIslands(matrix):
	noOfIslands = 0
	prev_Value = 0
	for i in matrix:
		prev_Value = 0
		for j in i:
			if j == 1 and prev_Value == 0:
				noOfIslands += 1
				prev_Value = 1
			elif j == 0:
				prev_Value = 0
	return noOfIslands
matrix0 = [[1, 0, 1, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1, 0]]
matrix1 = [[1, 0, 1], [0, 0, 0], [1, 1, 1]]
matrix2 = [[1, 1, 0, 1], [0, 1, 1, 1], [0, 1, 1, 0]]
print(countIslands(matrix0))
print(countIslands(matrix1))
print(countIslands(matrix2))
