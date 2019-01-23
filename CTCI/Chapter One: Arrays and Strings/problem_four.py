#Palindrome Permutation

from collections import Counter
def is_palindrome_permutation(s):
	ct = Counter(s.lower().replace(" ", ""))
	return sum(1 for v in ct.values() if v%2==1)<2


tests = ["abc", "aabaa", "abb", "acdtrhhtcda", "", "t", "aaabbb"]
vals = [False, True, True, True, True, True, False]
for test, val in zip(tests,vals):
	print( is_palindrome_permutation(test)==val)