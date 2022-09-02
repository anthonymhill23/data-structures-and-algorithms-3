from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


def tree_intersection(tree_a, tree_b):
    matching_values = set()

    hashtable = Hashtable()

    tree_a_values = BinaryTree.pre_order(tree_a)
    tree_b_values = BinaryTree.pre_order(tree_b)

    for i in tree_a_values:
        hashtable.set(i, i)

    for i in tree_b_values:
        if hashtable.contains(i):
            matching_values.add(i)

    return matching_values
