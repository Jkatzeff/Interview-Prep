class Foo:
	def __init__(self,val):
		self.val = val
	def __str__(self):
		return str(self.val)+":"+str(self.__dict__)

x = Foo(3)
print(x)