class Node:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None

n1 = Node(5)
n1.left = Node(1)
n1.left.left = Node(5)
n1.left.right = Node(5)
n1.right = Node(5)
n1.right.right = Node(5)

n2 = Node(3)
n2.left = Node(3)
n2.right = Node(3)
n2.right.right=Node(1)

def num_univalue_subtrees(root):
	def helper(root):
		if not root: 
			return (0,True)
		(Lval, is_uni_left) = helper(root.left)
		(Rval, is_uni_right) = helper(root.right)
		all_same = True
		if (root.left and root.left.val != root.val) or \
		(root.right and root.right.val != root.val):
			all_same = False
		is_uni = all_same and is_uni_left and is_uni_right
		return (is_uni+Lval+Rval, is_uni)
	return helper(root)[0]

print(num_univalue_subtrees(n2))