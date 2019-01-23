#Rotate Matrix (holy crap can't believe I got this one without errors!)

def rotate(A):
	n = len(A)
	if n<1 or n!=len(A[0]): return A
	for layer in range(n//2 + 1):
		for i in range(layer, n-1-layer):
			top = A[layer][layer+i]
			right = A[layer+i][n-1-layer]
			bottom = A[n-1-layer][n-1-layer-i]
			left = A[n-1-layer-i][layer]

			A[layer][layer+i]=left
			A[layer+i][n-1-layer]=top
			A[n-1-layer][n-1-layer-i]=right
			A[n-1-layer-i][layer]=bottom
	return A

tests = [[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[]]]
vals = [[[7,4,1],[8,5,2],[9,6,3]],[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]] ,[[]]]

for test, val in zip(tests,vals):
	print( rotate(test)==val)