from data_structures.stack import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
        self.rear = node
        if self.front is None:
            self.front = node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        wanted = self.front
        self.front = self.front.next
        wanted.next = None
        return wanted.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.front.value

    def is_empty(self):
        return self.front is None

