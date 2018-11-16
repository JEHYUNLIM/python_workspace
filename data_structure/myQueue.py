import listNode

class CircularQueue:
	def __init__(self,n):
		self.head = listNode.ListNode(None)
		self.tail = self.head
		self.temp = self.head
		for i in range(0, n):
			self.temp.next = listNode.ListNode(None)
			self.temp = self.temp.next
		self.temp.next = self.tail
	
	def enQueue(self, data):
		if self.head.next == self.tail:
			print("Queue is full")
		else:
			self.head.data = data
			self.head = self.head.next
	
	def deQueue(self):
		if self.head == self.tail:
			print("Queue is empty")
		else:
			print 'dequeue', self.tail.data
			self.tail.data = None
			self.tail = self.tail.next

	def printQueue(self):
		temp = self.tail
		while temp!=self.head:
			print(temp.data)
			temp = temp.next

class LinearQueue:
	def __init__(self):
		self.head = listNode.ListNode(None)
		self.tail = self.head

	def enQueue(self, data):
		self.head.data = data
		self.head.next = listNode.ListNode(None)
		self.head = self.head.next

	def deQueue(self):
		if self.tail == self.head:
			print("Queue is empty")
		else:
			print 'dequeue', self.tail.data
			self.tail.data = None
			temp = self.tail
			self.tail = self.tail.next
			temp.next = None

	def printQueue(self):
		temp = self.tail
		while temp != self.head:
			print(temp.data)
			temp = temp.next

