from data_structures.kary_tree import KaryTree
from data_structures.queue import Queue


def fizz_buzz_tree(tree):
    queue = Queue()

    collection = []
    fizz_tree = KaryTree(tree.root)
    queue.enqueue(fizz_tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        new_node = fizz_buzz(node.value)
        collection.append(new_node)
        for child in node.children:
            queue.enqueue(child)

    return collection


def fizz_buzz(data):
    data = int(data)
    if data % 15 == 0:
        return "FizzBuzz"
    if data % 5 == 0:
        return "Buzz"
    if data % 3 == 0:
        return "Fizz"
    else:
        return str(data)
