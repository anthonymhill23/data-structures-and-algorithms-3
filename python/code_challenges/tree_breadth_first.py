from data_structures.binary_tree import Queue


def breadth_first(tree):
    def breadth_first(tree):
        breadth = Queue()
        tree_values = []

        if not tree:
            return tree_values
        if not tree.root:
            return tree_values
        if not breadth.front:
            breadth.enqueue(tree.root)
        while breadth.front:
            root = breadth.dequeue()
            tree_values.append(root.value)
            if root.left:
                breadth.enqueue(root.left)
            if root.right:
                breadth.enqueue(root.right)

        return (tree_values)
