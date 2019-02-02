for i in range(1,10**7):
	s = set(str(i))
	for j in range(2,7):
		if s!=set(str(i*j)):
			break
		elif j==6:
			print(i)