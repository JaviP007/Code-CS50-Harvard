from fuel import convert
from fuel import gauge
import pytest


def test_valid1():

    assert convert("1/4")== 25
    assert convert("0/5")== 0
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("99/1")

def test_valid2():

    assert gauge(25)=="25%"
    assert gauge(1)=="E"
    assert gauge(99)=="F"



if __name__ == "__main__":
    main()
