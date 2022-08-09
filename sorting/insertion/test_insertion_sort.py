from insertion_sort import insertion_sort
import pytest


def test_insertion_sort_exists():
    assert insertion_sort


def test_sort_random_assortment():
    ran_list = [3, 7, 1]
    actual = insertion_sort(ran_list)
    expected = [1, 3, 7]
    assert actual == expected


def test_sort_descending():
    descending_list = [72, 63, 15]
    actual = insertion_sort(descending_list)
    expected = [15, 63, 72]
    assert actual == expected


def test_sort_of_large_list():
    large_list = [4, 8, 52, 23, 68, 24, 9, 100, 78, 42, 392, 19928, 576, 90]
    actual = insertion_sort(large_list)
    expected = [4, 8, 9, 23, 24, 42, 52, 68, 78, 90, 100, 392, 576, 19928]
    assert actual == expected


def test_duplicate_value():
    dup_list = [2, 2, 2, 10, 1, 3]
    actual = insertion_sort(dup_list)
    expected = [1, 2, 2, 2, 3, 10]
    assert actual == expected


def test_negative_values():
    neg_list = [-2, -3, 24, 38]
    actual = insertion_sort(neg_list)
    expected = [-3, -2, 24, 38]
    assert actual == expected
