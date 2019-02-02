from functools import reduce
#d is gonna keep track of factorials already done
d = dict()
def fact(n):
	if n<0: return -1
	if n<=1: return 1
	return reduce(lambda x,y: x*y, range(1,n+1), 1)
def nChooseK(n,k):
	top = -1
	bottom = -1
	if n in d.keys():
		top = d[n]
	else: top = fact(n)
	if k in d.keys():
		bottom=d[k]*d[n-k]
	else:
		bottom = fact(k)*fact(n-k)
	return top//bottom
#[1,4,6,4,1]
def kth_row(k):
	if k%2 == 0:
		firsthalf = [nChooseK(k,i) for i in range(k//2)]
		return firsthalf+[nChooseK(k,k//2+1)]+list(reversed(firsthalf))
	else:
		firsthalf = [nChooseK(k,i) for i in range(k//2)]
		return firsthalf+list(reversed(firsthalf))
print(kth_row(33))