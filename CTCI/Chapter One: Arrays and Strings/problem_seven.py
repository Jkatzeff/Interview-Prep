#Rotate Matrix (holy crap can't believe I got this one without errors!)

def rotate(A):
    n = len(A)
    if n<1 or n!=len(A[0]): return A
    for layer in range(n//2 ):
        for i in range(layer, n-1-layer):
            temp = A[i][layer]
            A[i][layer]=A[n-1-layer][i]
            A[n-1-layer][i]=A[n-1-i][n-1-layer]
            A[n-1-i][n-1-layer]=A[layer][n-1-i]
            A[layer][n-1-i]=temp

tests = [[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],[[]]]
vals = [[[7,4,1],[8,5,2],[9,6,3]],[[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]] ,[[]]]

for test, val in zip(tests,vals):
	print( rotate(test)==val)