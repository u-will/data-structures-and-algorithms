from insertion_sort.insertion_sort import insertion_sort

def test_unsortedArray():
    arr = [9,8,6,4,0]
    insertion_sort(arr)
    actual = arr
    expect = [0,4,6,8,9]
    assert actual == expect

def test_sortedArray():
    arr= [1,2,3,4,5]
    insertion_sort(arr)
    actual = arr
    expect =[1,2,3,4,5]
    assert actual == expect
