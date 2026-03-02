import pytest
from problems_1 import sum_of_elements,count_even_numbers,find_maximum_number

@pytest.mark.parametrize("nums, expected", [
    ([2,4,7], 13),
    ([], 0),
    ([9], 9),
    ([20,-43,-30], -53),
    ("123", 0)
])
def test_sum_of_elements(nums, expected):
    assert sum_of_elements(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([2,4,9], 2),
    ([], 0),
    ([3], 0),
    ([2], 1),
    ([-2,-4,7], 2)
])
def test_count_even_numbers(nums, expected):
    assert count_even_numbers(nums) == expected

@pytest.mark.parametrize("nums, expected", [
    ([8,4,2], 8),
    ([2], 2),
    ([], None),
    ([-9,2,-4], 2),
    ("123", None)
])
def test_find_maximum_number(nums, expected):
    assert find_maximum_number(nums) == expected
    
