from repeateated_word import repeate
import pytest

def test_with_no_repeat():
    string = "Please split this string"

    expect = ''
    actual = repeate(string)
    assert actual == expect

def test_with_repeat():
    string = 'Take oh take me with you, you alone'
    expect = 'take'
    actual = repeate(string)
    assert actual == expect
