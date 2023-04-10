from functions.functions_15 import palindrom


def test_palindrom_return_true():
    result = palindrom('assa')
    assert result == True


def test_palindrom_return_false():
    result = palindrom('assd')
    assert result == False
