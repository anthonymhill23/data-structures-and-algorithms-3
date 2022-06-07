class LinkedList:
    """
    This module will allow me to create a Linked List by  creating notes and adding them to the beginning of the Linked lists, also while settling their value. The list will only flow one way ( A good analogy would be (as far as I understand it) water trickling down hill. That only flows one way.
    
    
     )
    """

    def __init__(self):
        self.head = None
        self.list = []

    def __str__(self):
        string = ""
        current = self.head
        while current:
            string += f"{{ {current.value} }} -> "
            current = current.next
        string += 'NULL'
        return string

    def insert(self, data=None):
        """
        This will insert a new node
        """
        self.head = Node(data, self.head)

    def append(self, data):
        """
        This appends it to the end of the linked list
        """
        new_node = Node(data)
        current = self.head

        if not self.head:
            self.head = new_node
            return

        while current.next:
            current = current.next

        current.next = new_node

    def insert_before(self, query, value):
        """
        Insert Node before target value
        """
        if self.head is None:
            raise TargetError
        elif self.head.value == query:
            self.insert(value)
            return
        current = self.head
        while current:
            try:
                if current.next.value == query:
                    old_next = current.next
                    current.next = Node(value, old_next)
                    break
                current = current.next
            except:
                raise TargetError


    def insert_after(self, query, value):
        """
        Insert Node after target value
        """
        if self.head is None:
            raise TargetError
        current = self.head
        while current:
            if current.value is query:
                current.next = Node(value, current.next)
                break
            if current.next is None:
                raise TargetError
            current = current.next
 
    def kth_from_end(self, index):
        idx_archive = []
        current = self.head
        while current:
            idx_archive.append(current.value)
            current = current.next
        idx_archive.reverse()
        if index >= len(idx_archive):
            raise TargetError
        if index < 0:
            raise TargetError
        return idx_archive[index]            

    def includes(self, query):
        """
        Does the linked list have queried value? 
        """
        current = self.head
        while current:
            if current.value is query:
                return True
            current = current.next
        return False

    def display(self):
        return self.head.value


class Node:
    """
    Node the base of a linked list.
    """
    def __init__(self, data=None, next_=None):
        self.value = data
        self.next = next_


class TargetError(Exception):
    """
    Custom Exception
    """