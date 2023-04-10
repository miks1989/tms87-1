from functions.functions_05 import sum_args


def test_sum_args():
    result = sum_args(4, 3, 2, 1)
    assert result == 10
