class node:
	def __init__(self,data):
		self.data = data
		self.previous = None
		self.next = None

def display(self):
	current = self.head
	if self.head is None:
		print("list is empty")
		return
	else:
		print("Nodes of the circular Linked list:")
		print(current.data,"-->")
		while(current.next != self.head):
			current = current.next
			print(current.data,"-->")
	if self.head is None:
		print("list is empty")
class circularLinkedList:
	c1 = createList()
	c1.add("s")
	
