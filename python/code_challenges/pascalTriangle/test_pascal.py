
from pascal import pascal

def test_print():
    actual = pascal(3)
    expected = [[1], [1,1], [1,2,1]]
    assert actual == expected

def test_print_4():
    actual = pascal(4)
    expected = [[1], [1,1], [1,2,1], [1,3,3,1]]
    assert actual == expected

def test_string_input():
    actual = pascal("n")
    expected = None
    assert actual == expected

def test_no_lines():
    actual = pascal(0)
    expected = []
    assert actual == expected

def test_no_input():
    actual = pascal()
    expected = []
    assert actual == expected

def test_non_integer():
    actual = pascal(10.1)
    expected = None
    assert actual == expected
