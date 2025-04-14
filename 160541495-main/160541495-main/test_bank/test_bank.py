from bank import value


def test_bank():
    assert value("Que honda")== 100
    assert value("Hola amigo")==20
    assert value("Hello")==0
def test_bank2():
    assert value("1")==100
def test_bank3():
    assert value("hello 5")==0




if __name__ == "__main__":
    main()
