from plates import is_valid


def test_valid1():

    assert is_valid("AAAA")== True
    assert is_valid("AA05")==False
    assert is_valid("543")==False

def test_valid2():

    assert is_valid("CS50")==True

def test_valid3():

    assert is_valid("AAA5A")==False
    assert is_valid("54HAA")==False

def test_valid4():
    assert is_valid("HOL.,A")==False
    assert is_valid("HOLAAAAAA")==False
    assert is_valid("54HAA")==False





if __name__ == "__main__":
    main()
