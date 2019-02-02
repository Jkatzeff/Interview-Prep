#x^2 - y^2 - z^2 = n
#x^2 = n+y^2 + z^2
import math
from collections import Counter
d = Counter()


for i in range(1000):
	if i%1000==0:
		print("iteration " + str(i))
		print(sum([1 for v in d.values() if v==10]))
	for j in range(1,i//2):
		n = i**2 - (i-j)**2 - (i-2*j)**2
		if n<=0 or n>=10**6: continue
		d[n]+=1

print(sum([1 for v in d.values() if v==10]))
print (sorted(d.keys())[0:20])