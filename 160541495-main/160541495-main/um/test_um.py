from um import count


def test_convert():
    assert count("Um?")==1
    assert count("9 AM to 5 PM")==0
    assert count("um")==1
    assert count("holaumdf")==0
