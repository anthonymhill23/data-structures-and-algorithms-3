from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    This class is a subclass of the Binary Tree Class with the Add and Contains methods both passing in a value.
    """

    def __init__(self):
        self.root = None

    def __str__(self):
        def str_recursive(node, current):
            current += str(node.value)
            current += " L -> "
            if node.left is not None:
                current += str_recursive(node.left, current)
            else:
                current += "None"
            current += " R -> "
            if node.right is not None:
                current += str_recursive(node.right, current)
            else:
                current += "None"
            return current

        return str_recursive(self.root, "")

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current_node = self.root
        added = False
        while not added:
            if current_node.value >= value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    added = True
                else:
                    current_node = current_node.left
            elif current_node.value < value:
                if current_node.right is None:
                    current_node.right = Node(value)
                    added = True
                else:
                    current_node = current_node.right

    def contains(self, value):
        done = False
        current_node = self.root
        while not done:
            if current_node.value == value:
                return True
            elif current_node.value > value:
                if current_node.left is None:
                    done = True
                else:
                    current_node = current_node.left
            elif current_node.value < value:
                if current_node.right is None:
                    done = True
                else:
                    current_node = current_node.right
        return False
