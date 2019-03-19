import listNode

class MyStack:
	def __init__(self):
		self.top = None

	def push(self, data):
		temp = listNode.ListNode(data)
		temp.next = self.top
		self.top = temp

	def pop(self):
		if self.top == None:
			print("Stack is empty")
		else:
			print 'Pop ', self.top.data
			self.top = self.top.next

	def printStack(self):
		if self.top == None:
			print("Stack is empty")
		else:
			temp = self.top
			while temp!=None:
				print(temp.data)
				temp = temp.next

