class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None

head = Node(0)
curr = head
for i in range(1,100):
	curr.next = Node(i)
	curr = curr.next

#just print vals
def print_elems(head):
	while head:
		print(head.val)
		head=head.next


#middle element
def middle_element(head):
	fast = slow = head
	while(fast and fast.next):
		fast=fast.next.next
		slow = slow.next
	print(slow.val)


#k'th from end
def kth_from_end(head,k):
	curr = head
	for i in range(k):
		if curr:
			curr=curr.next
	while curr:
		curr=curr.next
		head=head.next
	print(head.val)

def reverse_second_half(head):
	fast = slow = head
	prev = None
	while(fast and fast.next):
		fast=fast.next.next
		prev = slow
		slow = slow.next
	while slow:
		tmp = slow.next	
		slow.next = prev
		tmp,slow=slow,tmp
	while tmp:
		print(tmp.val)
		tmp=tmp.next
reverse_second_half(head)