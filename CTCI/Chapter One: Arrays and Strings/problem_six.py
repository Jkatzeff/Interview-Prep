#String compression

def compress(s):
	curr_index = 0
	ans = []
	while curr_index<len(s):
		next_index = curr_index + 1
		while next_index < len(s) and s[next_index]==s[curr_index]:
			next_index+=1
		ans.append(s[curr_index]+str(next_index-curr_index))
		curr_index = next_index
	ans_str = ''.join(ans)
	return ans_str if len(ans_str)<len(s) else s


tests = ["aabcccccaaa","a","aaaaa","abcabc","aaabbbccc",""]
vals = ["a2b1c5a3","a","a5","abcabc","a3b3c3",""]
for test, val in zip(tests,vals):
	print( compress(test)==val)