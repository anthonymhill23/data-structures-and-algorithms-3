import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


def test_set_apple():
    ht = Hashtable()
    ht.set('fruit', 'apple')
    fruit_index = ht.hash('fruit')
    actual = ht.buckets[fruit_index]
    expected = ('fruit','apple')
    assert actual.head.value == expected


def test_contains():
    ht = Hashtable()
    ht.set('fruit', 'apple')
    expected = True
    actual = ht.contains('fruit')
    assert actual == expected

def test_not_contains():
    ht = Hashtable()
    ht.set('cat', 'Josie')
    expected = False
    actual = ht.contains('act')
    assert actual == expected


def test_contains_zero():
    ht = Hashtable()
    ht.set(0, 0)
    expected = True
    actual = ht.contains(0)
    assert actual == expected


def test_keys():
    ht = Hashtable()
    ht.set('cat','Josie')
    ht.set('act','A Contemporary Theater')
    ht.set('tac','Taco Tuesday')
    actual = ht.keys()
    expected = {'cat','act','tac'}
    assert actual == expected

def test_not_in_keys():
    ht = Hashtable()
    ht.set('cat','Josie')
    ht.set('act','A Contemporary Theater')
    ht.set('gort','Taco Tuesday')
    actual = ht.keys()
    expected = {'cat','act','tac'}
    assert actual != expected

def test_set_update():
    ht = Hashtable()
    ht.set('cat','Josie')
    ht.set('cat', 'Pumpkin')
    actual = ht.get('cat')
    expected = 'Pumpkin'
    assert actual == expected
