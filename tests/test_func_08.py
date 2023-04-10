from functions.functions_08 import avg_arifm, avg_geom, result_avg


def test_avg_arifm():
    result = avg_arifm(3, 3, 3)
    assert result == 3


def test_avg_geom():
    result = avg_geom(2, 2, 2)
    assert result == 2


def test_result_avg_geom():
    result = result_avg(2, 2, 2, mean_type=1)
    assert result == 2


def test_result_avg_arifm():
    result = result_avg(3, 3, 3, 3, mean_type=0)
    assert result == 3
