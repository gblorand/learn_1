import pytest


# Input for tests with list of lists of ints where 5 appear multiple times in a list
@pytest.fixture
def list_of_int_lists():
    test_input = [
        [17, 4, 1, 3, 2],
        [6, 5, 5],
        [7, 9, 7, 8],
        [12, 11, 10, 12, 18],
        [14, 13],
        [16, 15, 15, 10],
        [18, 5, 17, 18, 17, 19, 5]
    ]
    return test_input


@pytest.fixture
def expected_output():
    return {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 2,
    6: 1,
    7: 1,
    8: 1,
    9: 1,
    10: 2,
    11: 1,
    12: 1,
    13: 1,
    14: 1,
    15: 1,
    16: 1,
    17: 2,
    18: 2,
    19: 1
}


def test_count_appearances(list_of_int_lists, expected_output):
    from util.alg import count_appearances
    assert count_appearances(list_of_int_lists) == expected_output
