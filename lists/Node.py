class Node():

	def __init__ (self, value):
		
		self.next_node = None
		self.value = value

	def getNext(self):
		
		return self.next_node

	def setNext(self, next_node):
		
		self.next_node = next_node

	def getValue(self):
		
		return self.value

	def setValue(self, value):
		
		self.value = value

	def __str__ (self):
		
		return str(self.value)