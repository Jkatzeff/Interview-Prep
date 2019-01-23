#1.3: URLify
#	  In this implementation, process s as a char array so this problem makes
#	  sense in Python.
def URLify(s):
	if not s: return s
	n = len(s)
	def find_last_index():
		for i in range(n-1,-1,-1):
			if s[i]==" ": continue
			return i
	left_index = find_last_index()
	right_index = n-1
	while left_index != right_index:
		if s[left_index]!=" ":
			s[right_index]=s[left_index]
			right_index-=1
			left_index-=1
		else:
			s[right_index]="0"
			s[right_index-1]="2"
			s[right_index-2]="%"
			right_index-=3
			left_index-=1
	return s

print(''.join(URLify(list("Mr John Smith    "))))