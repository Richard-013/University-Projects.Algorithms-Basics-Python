class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        '''Pushes the given item to the top of the stack'''
        self.stack.append(item)
        
    def pop(self):
        '''Pops the item at the top of the stack'''
        return self.stack.pop(len(self.stack) - 1)

    def printStack(self):
        for item in self.stack:
            print(item)

class Queue:
    def __init__(self):
        self.queue = list()

    def push(self, item):
        '''Pushes the given item to the back of the queue'''
        self.queue.append(item)

    def pop(self):
        '''Pops the item at the front of the queue'''
        return self.queue.pop(0)

    def printQueue(self):
        for item in self.queue:
            print(item)

print("TEST: STACK\n")

testStack = Stack()
testStack.push(87)
testStack.push(43)
testStack.push(13)
testStack.push(98)
testStack.push(57)

testStack.printStack()
print("\nExpected: 57  ---  Actual:", testStack.pop())
print("Expected: 98  ---  Actual:", testStack.pop())
print("\n------------------------------")
print("\nTEST: QUEUE\n")

testQueue = Queue()
testQueue.push(87)
testQueue.push(43)
testQueue.push(13)
testQueue.push(98)
testQueue.push(57)

testQueue.printQueue()
print("\nExpected: 87  ---  Actual:", testQueue.pop())
print("Expected: 43  ---  Actual:", testQueue.pop())

