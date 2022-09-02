from data_structures.hashtable import Hashtable


def left_join(table_a, table_b):
    """
    Arguments: Two hashmaps
    Return: a List with the keys of table a and the values from both table a and table b (if available)
    """
    joined_list = []  # O(1)

    for key, value in table_a.items():  # O(N)
        if table_b.get(key):  # O(N) Where N is how big table_b is
            joined_list.append([key, value, table_b.get(key)])  # O(1)

        else:
            joined_list.append([key, value, 'NONE'])  # O(1)

    print(joined_list)  # O(1) #O(N)
    return joined_list  # O(1)
