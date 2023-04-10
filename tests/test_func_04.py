from functions.functions_04 import create_matrix

result_test_data = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def test_create_matrix():
    result = create_matrix(3)
    assert len(result) == len(result_test_data)
    assert len(result[0]) == 3
    # assert len(result[0]) == len(result_test_data[0])
