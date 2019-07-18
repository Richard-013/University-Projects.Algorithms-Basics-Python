#Single-link Linked List

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def getValue(self):
        return self.value

    def setValue(self, newValue):
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

        while(True):
            if currentNode.getValue != target:
                if currentNode.getNextNode() == None:
                    break
                else:
                    currentNode = currentNode.getNextNode()
            else:
                return currentNode

        return None

    def deleteAt(self, index):
        if index > self.count-1:
            return

    def printList(self):
        currentNode = self.head
        if currentNode == None:
            print("List is empty")
        else:
            while(currentNode != None):
                print("Node:", currentNode.getValue())
                currentNode = currentNode.getNextNode()
        
