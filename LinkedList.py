#Single-link Linked List

class Node(object):
    def __init__(self, value):
        self.value = value
        self.nextNode = None

    def getValue(self):
        '''Gets the value of the current node'''
        return self.value

    def setValue(self, newValue):
        '''Sets the value of the current node'''
        self.value = newValue

    def getNextNode(self):
        '''Gets the next node in the list'''
        return self.nextNode

    def setNextNode(self, newNext):
        '''Sets the next node to a new node'''
        self.nextNode = newNext

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.nodeCount = 0

    def getNodeCount(self):
        '''Gets the number of nodes in the list'''
        return self.count

    def insertNode(self, nodeData):
        '''Inserts new node at the head of the list'''
        newNode = Node(nodeData)
        newNode.setNextNode(self.head)
        self.head = newNode
        self.nodeCount += 1

    def searchList(self, target):
        '''Searches the list for a target value'''
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
        '''Deletes a node at a given index in the list'''
        if index > self.count-1:
            return
        if index == 0:
            self.head = self.head.getNextNode() #Deletes the head (index 0)
        else:
            count = 0
            currentNode = self.head
            while count < index - 1:
                currentNode = currentNode.getNextNode()
                count += 1

            currentNode.setNextNode(currentNode.getNextNode().getNextNode())
            self.count -= 1

    def printList(self):
        '''Prints the whole list'''
        currentNode = self.head
        if currentNode == None:
            print("List is empty")
        else:
            while(currentNode != None):
                print("Node:", currentNode.getValue())
                currentNode = currentNode.getNextNode()
        

testList = LinkedList()
testList.insertNode(45)
testList.insertNode(87)
testList.insertNode(12)
testList.insertNode(1)
testList.insertNode(43)
testList.printList()

print("TEST SET 1 --------------------------------")

print("Node Count:", testList.getNodeCount())
print("Search for 45:", testList.searchList(45))
print("Search for 900:", testList.searchList(900))

print("\nTEST SET 2 --------------------------------")

print("Node Count:", testList.getNodeCount())
print("Search for 45:", testList.searchList(12))
print("Attempting to delete 12")
print("Node Count:", testList.getNodeCount())
print("Search for 45:", testList.searchList(12))
testList.printList()

