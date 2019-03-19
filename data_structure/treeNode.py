class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def setLeftChild(self, child):
		if self.left == None:
			self.left = child
		else:
			print("This Node has left child")

	def setRightChild(self, child):
		if self.right == None:
			self.right = child
		else:
			print("This Node has right child")

	def getLeftChild(self):
		if self.left == None:
			print("No left child")
			return None
		else:
			return self.left

	def getRightChild(self):
		if self.right == None:
			print("No right child")
			return None
		else:
			return self.right

	def getData(self):
		return data
