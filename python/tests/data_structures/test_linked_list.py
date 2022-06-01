import pytest
from data_structures.linked_list import LinkedList


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"

def test_insert_into_init_list():
    linked = LinkedList()
    linked.insert("apple")
    linked.insert("banana")
    assert linked.head.value == "banana"

def test_apple_still_there():
    linked = LinkedList()
    linked.insert("apple")
    linked.insert("banana")
    assert linked.head.next.value == "apple"

# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"

# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"



def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")

def test_list_append_as_string():
    linked_list = LinkedList()

    linked_list.insert("banana")
    linked_list.insert("cucumber")
    linked_list.append("apple")

    assert str(linked_list) == "{ cucumber } -> { banana } -> { apple } -> NULL"
