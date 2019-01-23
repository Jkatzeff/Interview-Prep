#One away

def is_one_away(s1,s2):
	def handle_zero_diff(s1,s2):
		return [s1[i]!=s2[i] for i in range(len(s1))].count(True)<2
	def handle_one_diff(s1,s2):
		if len(s1)<len(s2):
			s1,s2=s2,s1
		idx1=idx2=0
		while idx2<len(s2) and s1[idx1]==s2[idx2]:
			idx1+=1
			idx2+=1
		if idx2==len(s2): return True
		idx1+=1
		while idx1<len(s1):
			if s1[idx1]!=s2[idx2]: return False
			idx1+=1
			idx2+=1
		return True

	distance = abs(len(s1)-len(s2))
	if distance>1: 
		return False
	elif distance==1:
		return handle_one_diff(s1,s2)
	else:
		return handle_zero_diff(s1,s2)

tests = [["pale", "ple"], ["pales", "pale"], ["pale", "bale"], ["pale", "bake"]]
vals = [True, True, True, False]
for test, val in zip(tests,vals):
	print( is_one_away(*test)==val)