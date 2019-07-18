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

    def setNext(self, newNext):
        self.nextNode = newNext
