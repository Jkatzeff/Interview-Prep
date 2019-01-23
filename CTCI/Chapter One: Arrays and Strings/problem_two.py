#1.2: Check Permutations: Given Two Strings, write a method to decide if one is
#	  a permutation of the other.

from collections import Counter
def is_permutation(s1,s2):
	return Counter(s1)==Counter(s2)


tests=[["abc","bac"], ["","a"], ["abcdef","abefcd"],["aaa","a"], ["aab", "bba"]]

expected = [True, False, True, False, False]
for test,expect in zip(tests,expected):
	print(is_permutation(*test)==expect)