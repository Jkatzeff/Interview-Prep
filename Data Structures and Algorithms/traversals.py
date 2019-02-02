from collections import defaultdict
from queue import Queue
class TreeNode:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

class GraphNode:
	def __init__(self, val):
		self.val = val
		self.children = []
	def set_children(self,arr):
		self.children = arr

def iterative_traversal(root):
	if not root: return
	stack = []
	while stack or root:
		while root:
			stack.append(root)
			root = root.left
		root = stack.pop()
		print(root.val)
		root = root.right

def DFS(root):
	if not root: return
	visited = defaultdict(bool)
	stack = [root]
	visited[root]=True
	while stack:
		root = stack.pop()
		print(root.val)
		for node in root.children:
			if not visited[node]:
				stack.append(node)
				visited[node]=True

def BFS(root):
	if not root: return
	q = Queue()
	q.put(root)
	visited = defaultdict(bool)
	visited[root]=True
	while not q.empty():
		root = q.get()
		print(root.val)
		for node in root.children:
			if not visited[node]:
				q.put(node)
				visited[node]=True

def run_graph_traversals():
	n1 = GraphNode(1)
	n2 = GraphNode(2)
	n3 = GraphNode(3)
	n4 = GraphNode(4)
	n5 = GraphNode(5)
	n6 = GraphNode(6)
	n7 = GraphNode(7)
	n8 = GraphNode(8)
	n9 = GraphNode(9)
	n1.set_children([n2,n3])
	n2.set_children([n1,n4,n5])
	n3.set_children([n1,n8,n9])
	n4.set_children([n2,n5])
	n5.set_children([n2,n4,n6])
	n6.set_children([n5,n7])
	n7.set_children([n6])
	n8.set_children([n3])
	n9.set_children([n3])
	print("RUNNING BFS")
	BFS(n1)
	print(); print();
	print("RUNNING DFS")
	DFS(n1)
	print(); print();

def run_tree_traversals():
	n1 = TreeNode(1)
	n2 = TreeNode(2)
	n3 = TreeNode(3)
	n4 = TreeNode(4)
	n5 = TreeNode(5)
	n6 = TreeNode(6)
	n7 = TreeNode(7)
	n4.left = n2
	n4.right = n6
	n2.left = n1
	n2.right = n3
	n6.left = n5
	n6.right = n7
	print("ITERATIVE TRAVERSAL")
	iterative_traversal(n4)

run_tree_traversals()