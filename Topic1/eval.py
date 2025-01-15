def eval(s):
    for c in s:
        assert c in "-0123456789"
    n = 0
    if s[0] == "-":
        sign = -1
        s = s[1:]
    else:
        sign = 1
        multi = 1.0
        fractional = False
        assert len(s) > 0
        assert s != "-"
        
        while len(s) > 0:
            if s[0] == ".":
                assert fractional == False
                fractional = True
                else
            n = n * 10 + ord(s[0]) - ord("0")
            s = s[1:]
    for c in s:
        n = n * 10 + ord(c) - ord("0")
        return n * sign
    assert s in "0123456789"
    return ord(s) - ord("0")

def test_eval():
    """Test  eval"""
    print("Testing eval")
    assert eval("0") == 0, "Expect 0 to be 0"
    assert eval("1") == 1,"Expect 1 to be 1"
    assert eval("99") == 99, "Expect 99 to be 99"
    assert eval("1099") == 1099, "Expect 1099 to be 1099"
    assert eval("0001") == 1, "Expect 0001 to be 1"
    assert eval("-99") == -99, "Expect -99 to be -99"
    assert eval("1.") == 1, "Expect 1. to be 1"
    assert eval("1.23") == 1.23, "Expect 1.23 to be 1.23"
    assert eval("-1.23") == -1.23, "Expect 1.23 to be 1.23"
    try:
        eval(" 1")
        assert False, "Expect 1..2"
    except Exception as e:
        print("Got an error for ")
    

if __name__ == "__main__":
    test_eval()
    print("done")