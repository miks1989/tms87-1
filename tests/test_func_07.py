from functions.functions_07 import print_from_dict


def test_func_07():
    result = print_from_dict(a=1, bb=2, ccc=3, dddd=4)
    assert result == {'bb': 2, 'dddd': 4}


def test_func_07_without_data_in_dict():
    result = print_from_dict(a=1, ccc=3)
    assert result == {}
