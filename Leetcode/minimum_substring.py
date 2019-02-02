from collections import Counter
def minimum_substring(s,t):
	best_len = float('inf')
	ans = ""
	c = Counter(t)
	l=r=0
	ctr = len(c.keys())
	while r<len(s):
		end_char = s[r]
		if end_char in c.keys():
			c[end_char]-=1
			if c[end_char]==0: ctr-=1
		r+=1
		while ctr==0:
			if r-l<best_len:
				best_len = r-l
				ans = s[l:r]
			start_char = s[l]
			if start_char in c.keys():
				c[start_char]+=1
				if c[start_char]>0: ctr+=1
			l+=1
	return ans
print(minimum_substring("ADOBECODEBANC","ABC"))