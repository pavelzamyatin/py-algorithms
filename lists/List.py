from Node import Node

class LinkedList():

    def __init__ (self):
        
        self.firstNode = None

    def append(self, value):
        
        if self.firstNode is None:
            self.firstNode = Node(value)
        else:
            previous_node = self.firstNode

            while True:
                if previous_node.getNext() is None:
                    newNode = Node(value)
                    previous_node.setNext(newNode)
                    break

                previous_node = previous_node.getNext()
            
    def pop(self):
        
        if self.firstNode is None:
            raise IndexError('Out of range')

        elif self.firstNode.getNext() is None:

            lastNode = self.firstNode
            self.firstNode = None

            return lastNode.getValue()

        else:
            lastNode = self.firstNode

            while True:
                
                if lastNode.getNext() is None:
                    currentNode.setNext(None)
                    break

                currentNode = lastNode
                lastNode = lastNode.getNext()

            return lastNode.getValue()

    def prepend(self, value):

        if self.firstNode is None:
            self.firstNode = Node(value)
        else:
            previous_node = self.firstNode
            self.firstNode = Node(value)
            self.firstNode.setNext(previous_node)

    def set(self):
        pass

    def get(self, index):
        
        previous_node = self.firstNode
        
        while True:
            if previous_node is None:
                raise IndexError()
            
            if index == 0:
                return previous_node.getValue()

            index -= 1
            previous_node = previous_node.getNext()


    def length(self):
        return len(self)

    def __str__ (self):

        if self.firstNode is None:
            return '[]'
        
        string = '['
        previous_node = self.firstNode

        while True:
            
            if previous_node.getNext() is None:
                string += str(previous_node)
                break
            
            else:
                string += str(previous_node) + ', '

            previous_node = previous_node.getNext()

        string += ']'

        return string

    def __len__ (self):

        length = 0

        if self.firstNode is None:
            return length

        else:
            previous_node = self.firstNode

            while True:
                length += 1

                if previous_node.getNext() is None:
                    break

                previous_node = previous_node.getNext()
                
        return length
