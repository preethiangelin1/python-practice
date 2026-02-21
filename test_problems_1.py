from problems_1 import sum_of_elements,count_even_numbers,find_maximum_number

def test_sum_of_elements():
    assert sum_of_elements([2,4,7]) == 13
    assert sum_of_elements([]) == 0
    assert sum_of_elements([9]) == 9
    assert sum_of_elements([20,-43,-30]) == -53
    assert sum_of_elements("123") == 0

def test_count_even_numbers():
    assert count_even_numbers([2,4,9]) == 2
    assert count_even_numbers([]) == 0
    assert count_even_numbers([3]) == 0
    assert count_even_numbers([2]) == 1
    assert count_even_numbers([-2,-4,7]) == 2

def test_find_maximum_number():
    assert find_maximum_number([8,4,2]) == 8
    assert find_maximum_number([2]) == 2
    assert find_maximum_number([]) == None
    assert find_maximum_number([-9,2,-4]) == 2
    assert find_maximum_number("123") == None

