from functions.functions_06 import summ_and_max


def test_summ_and_max():
    result = summ_and_max(1, 2, 3, 4)
    assert result == (10, 4)
