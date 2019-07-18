#Single-link Linked List

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def getData(self):
        return self.value

    def setData(self, newValue):
        self.value = newValue

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, newNext):
        self.nextNode = newNext

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.nodeCount = 0

    def getNodeCount(self):
        return self.count

    def insertNode(self, nodeData):
        newNode = Node(data)
        newNode.setNextNode(self.head)
        self.head = newNode

    def searchList(self, target):
        currentNode = self.head

        return None

    def deleteAt(self, index):
        if index > self.count-1:
            return

    
        
