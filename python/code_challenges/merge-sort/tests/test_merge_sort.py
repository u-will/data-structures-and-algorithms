
from merge_sort.merge_sort import mergesort



def test_singleArray():
    arr = [5]
    mergesort(arr)
    actual = arr
    expect = [5]
    assert actual == expect




def test_unsortedNegativeArray():
    arr = [-31, 2,0, 2, -15, 8]
    mergesort(arr)
    actual = arr
    expect = [-31, -15, 0, 2, 2, 8]
    assert actual == expect
