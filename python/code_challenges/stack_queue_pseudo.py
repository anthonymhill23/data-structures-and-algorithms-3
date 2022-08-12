from data_structures.stack import Stack,Node


class PseudoQueue:
    def __init__(self):
        self.first = Stack()
        self.second = Stack()

    def enqueue(self, value):
        node = Node(value)
        if self.first.is_empty():

            self.first.push(node)
        print(self.first.top)
        # self.second.push(value)

    def dequeue(self):
        self.first.pop()
        print(self.first.top)
        self.second.pop()







