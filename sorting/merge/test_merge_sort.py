from merge_sort import merge_sort, merge


def test_import_merge_sort():
    assert merge_sort


def test_import_merge():
    assert merge


def test_already_sorted():
    already_sorted_list = [1, 2, 3, 4, 5]
    actual = merge_sort(already_sorted_list)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_close_to_sorted():
    close_to_sorted_list = [1, 2, 4, 3, 5]
    actual = merge_sort(close_to_sorted_list)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_descending_list():
    descending_order_list = [5, 4, 3, 2, 1]
    actual = merge_sort(descending_order_list)
    expected = [1, 2, 3, 4, 5]
    assert actual == expected


def test_duplicate_number():
    duplicates_list = [1, 2, 2, 4, 4, 2, 3, 3, 5]
    actual = merge_sort(duplicates_list)
    expected = [1, 2, 2, 2, 3, 3, 4, 4, 5]
    assert actual == expected


def test_negatives():
    negative_number_list = [-1, -2, -3, 4, 5]
    actual = merge_sort(negative_number_list)
    expected = [-3, -2, -1, 4, 5]
    assert actual == expected


def test_floats():
    float_list = [0.1, 0.2, 0.4, 0.3, 0.5]
    actual = merge_sort(float_list)
    expected = [0.1, 0.2, 0.3, 0.4, 0.5]
    assert actual == expected