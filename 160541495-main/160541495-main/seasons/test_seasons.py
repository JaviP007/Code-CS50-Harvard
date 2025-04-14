from seasons import getminutesxd
import pytest


def test_getminutes1():
    assert getminutesxd("2000-04-11")=="Twelve million, six hundred twelve thousand, nine hundred sixty minutes"


def test_getminutes2():

    with pytest.raises(SystemExit):
        getminutesxd("09:00 17:00")
    with pytest.raises(SystemExit):
        getminutesxd("9dfsM")

if __name__ == "__main__":
    main()
