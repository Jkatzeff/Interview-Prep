#1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
#	 What if you cannot use additional data structures? 

def unique_chars(s):
	used_chars = [0]*255 #O(1) Space
	for c in s:
		if used_chars[ord(c)]!=0:
			return False
		used_chars[ord(c)]=1
	return True


tests = ["abc", "bab", "abcdea", "1*a3f9", "", "12", "100000000001"]
expected = [True, False, False, True, True, True, False]
for test,expect in zip(tests,expected):
	print(unique_chars(test)==expect)