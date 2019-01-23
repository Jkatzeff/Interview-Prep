#Zero Matrix
from collections import defaultdict
def zero_matrix(A):
	indices = []
	for i in range(len(A)):
		for j in range(len(A[0])):
			if A[i][j]==0:
				indices.append((i,j))
	seen = defaultdict(list)
	def zero(i,j,direction):
		if direction in seen[(i,j)]: return
		if not 0<=i<len(A) or not 0<=j<len(A[0]): return
		A[i][j]=0
		seen[(i,j)].append(direction)
		if direction == "hor":
			zero(i-1,j,direction)
			zero(i+1,j,direction)
		elif direction == "ver":
			zero(i,j-1,direction)
			zero(i,j+1,direction)
	for index in indices:
		zero(*index, "ver")
		zero(*index, "hor")
	return A


tests = [[[0,1,1],[1,1,1],[1,1,1]],[[1,1,1],[1,1,1]],[[0,1],[0,1],[0,1]]]
vals = [[[0,0,0],[0,1,1],[0,1,1]],[[1,1,1],[1,1,1]],[[0,0],[0,0],[0,0]]]
for test, val in zip(tests,vals):
	print( zero_matrix(test)==val)