from Node import Node

firstElement = Node(42)
new_element_value = 123

previous_node = firstElement

while True:
	
	print(previous_node)

	if previous_node.getNext() == None:
		
		newNode = Node(new_element_value)
		previous_node.setNext(newNode)
		print(newNode)
		print('Last is found')
		break


	previous_node = previous_node.getNext()