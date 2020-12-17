from quick_sort.quick_sort import quick_sort


def test_import():
    assert quick_sort


def test_single_list():
    arr = [5]
    left = 0
    right = 0
    quick_sort(arr,left, right)
    actual = arr
    expect = [5]
    assert actual == expect


def test_already_sorted_list():
    arr = [1, 2, 3, 4, 5]
    left = 0
    right = 4
    quick_sort(arr,left, right)
    actual = arr
    expect = [1, 2, 3, 4, 5]
    assert actual == expect


def test_unsorted_list():
    arr = [3, 6, 2, 4]
    left = 0
    right = 3
    quick_sort(arr,left, right)
    actual = arr
    expect = [2, 3, 4, 6]
    assert actual == expect
