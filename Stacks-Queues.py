class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        '''Pushes the given item to the top of the stack'''
        self.stack.append(item)
        
    def pop(self):
        '''Pops the item at the top of the stack'''
        return self.stack.pop(len(self.stack) - 1)


class Queue:
    def __init__(self):
        self.queue = list()

    def push(self, item):
        '''Pushes the given item to the back of the queue'''
        self.queue.append(item)

    def pop(self):
        '''Pops the item at the front of the queue'''
        return self.queue.pop(0)

