from isEven.is_even import is_even

def test_even_numbers():
    assert is_even(2)
    assert is_even(0)
    assert is_even(-4)
    assert is_even(104)

def test_odd_numbers():
    assert not is_even(1)
    assert not is_even(-3)
    assert not is_even(5)
    assert not is_even(103)
