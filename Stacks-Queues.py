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

    def enqueue(self, item):
        '''Pushes the given item to the back of the queue'''
        self.queue.append(item)

    def dequeue(self):
        '''Removes the item at the front of the queue'''
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
testQueue.enqueue(87)
testQueue.enqueue(43)
testQueue.enqueue(13)
testQueue.enqueue(98)
testQueue.enqueue(57)

testQueue.printQueue()
print("\nExpected: 87  ---  Actual:", testQueue.dequeue())
print("Expected: 43  ---  Actual:", testQueue.dequeue())

