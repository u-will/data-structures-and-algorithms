from multi_bracket_validation import check
def test_empty_string():
    actual = check("")
    expected = True
    assert actual == expected
def test_unmatched_openner():
    actual1 = check("{")
    actual2 = check("(")
    actual3 = check("[")
    expected = False
    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected
def test_unmatched_closer():
    actual1 = check("}")
    actual2 = check(")")
    actual3 = check("]")
    expected = False
    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected
def test_proper_brackets():
    actual1 = check("{[()]}")
    actual2 = check("{}")
    actual3 = check("[]")
    actual4 = check("()")
    actual5= check("[(){}]")
    expected = True
    assert actual1 == expected
    assert actual2 == expected
    assert actual3 == expected
    assert actual4 == expected
    assert actual5 == expected
