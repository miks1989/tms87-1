from functions.functions_11 import is_power_n

def test_is_power_n_true():
    result = is_power_n(9, 3)
    assert result == True

def test_is_power_n_false():
    result = is_power_n(7, 3)
    assert result == False