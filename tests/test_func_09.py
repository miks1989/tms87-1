from functions.functions_09 import counter_numbers_in_list


def test_counter_numbers_in_list():
    result = counter_numbers_in_list([1, 1, 1, 2, 2, 3, 5, 5, 5, 5, 5])
    assert result == {1: 3, 2: 2, 5: 5, 3: 1}
