from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        wanted = self.top
        self.top = self.top.next
        wanted.next = None
        return wanted.value

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.top is None:
            raise InvalidOperationError('Method not allowed on empty collection')
        return self.top.value
