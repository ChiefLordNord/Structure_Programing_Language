def test_eval():
    """ test eval """
    print("testing eval()")
    assert eval("0") == 0, "Expect 0 to be 0"
    assert eval("1") == 1
    assert eval("99") == 99
    assert eval("1099") == 1099
    assert eval("-99") == -99
    assert eval("1.") == 1
    assert eval("1.23") == 1.23
    assert eval("-1.23") == -1.23
    assert eval("0.001") == 0.001  # Additional test case
    try:
        eval("1..2")
        assert False, "No error for 1..2"
    except Exception:
        print("got an error for 1..2")
    try:
        eval(" 1")
        assert False, "No error for [ 1]"
    except Exception:
        print("got an error for [ 1]")
    try:
        eval("--1")
        assert False, "No error for [--1]"
    except Exception:
        print("got an error for [--1]")

def test_parse_term():
    print("testing parse_term()")
    assert parse_term("3*4") == 12
    assert parse_term("3*4*5") == 60
    assert parse_term("3*4/2") == 6
    assert parse_term("3/4") == 0.75
    assert parse_term("3/4*2") == 1.5
    assert parse_term("6/3*2") == 4.0  # Additional test case
    assert parse_term("2*2*2*2") == 16  # Additional test case
    assert parse_term("10/2*5") == 25.0  # Additional test case
    try:
        parse_term("3**4")
        assert False, "No error for 3**4"
    except Exception:
        print("got an error for 3**4")

def test_parse_factor():
    print("testing parse_factor()")
    assert parse_factor("3") == 3
    assert parse_factor("-3") == -3
    assert parse_factor("3.14") == 3.14
    assert parse_factor("-3.14") == -3.14
    assert parse_factor("0.5") == 0.5  # Additional test case
    assert parse_factor("-0.5") == -0.5  # Additional test case
    assert parse_factor("2.718") == 2.718  # Additional test case
    try:
        parse_factor("3..14")
        assert False, "No error for 3..14"
    except Exception:
        print("got an error for 3..14")
    try:
        parse_factor("abc")
        assert False, "No error for abc"
    except Exception:
        print("got an error for abc")

def parse_term(expression):
    try:
        return eval(expression.replace('*', ' * ').replace('/', ' / '))
    except Exception:
        raise ValueError("Invalid term")

def parse_factor(expression):
    try:
        return eval(expression)
    except Exception:
        raise ValueError("Invalid factor")

if __name__ == "__main__":
    test_eval()
    test_parse_term()
    test_parse_factor()
    print("done.")
