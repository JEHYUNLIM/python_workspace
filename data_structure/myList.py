import listNode

class MyList:
	def __init__(self):
		self.head = listNode.ListNode(None)
		self.tail = listNode.ListNode(None)
		self.head.next = self.tail
		self.tail.prev = self.head
		self.num = 0

	def append(self, data):
		temp = listNode.ListNode(data)
		self.head.next.prev = temp
		temp.prev = self.head
		temp.next = self.head.next
		self.head.next = temp
		self.num+=1

	def delete(self, n):
		if n>self.num:
			print("This List has %d Nodes" %self.num)
			return
		elif n<0:
			print("Cannot delete negative")
			return
		temp = self.head
		for i in range(0, n):
			temp = temp.next
		print 'Delete', temp.data
		temp.prev.next = temp.next
		temp.next.prev = temp.prev
		temp.next = None
		temp.prev = None
		self.num-=1

	def printList(self):
		temp = self.head
		while temp.next != self.tail:
			temp = temp.next
			print(temp.data)

	def search(self,n):
		if n>self.num:
                        print("This List has %d Nodes" %self.num)
                        return
                elif n<0:
                        print("Cannot search negative")
                        return
		temp = self.head
		for i in range(0, n):
			temp = temp.next
		print(temp.data)
