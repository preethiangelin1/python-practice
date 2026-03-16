from problems_3 import count_char_freq, is_anagram, invert_dict, merge_dict

def test_count_char_freq():
    assert count_char_freq("abc") == {"a":1, "b":1, "c":1} 
    assert count_char_freq("") == {} 
    assert count_char_freq("123") == {"1": 1, "2": 1, "3": 1} 

def test_is_anagram():
    assert is_anagram("abc", "abc") == True
    assert is_anagram("abc", "abcd") == False
    assert is_anagram("", "abc") == False
    assert is_anagram("123", "abc") == False
    assert is_anagram("", "") == True

def test_invert_dict():
    assert invert_dict({"a":1, "b":2, "c":3}) == {1:'a', 2:'b', 3:'c'}
    assert invert_dict({"a":1, "b":1, "c":"ab"}) == {1:'a', 1:'b', "ab":'c'}
    assert invert_dict({}) == {}

def test_merge_dict():
    assert merge_dict({"a":1,"b":2}, {"c":3,"d":4}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert merge_dict({}, {}) == {}
    assert merge_dict({1:1, 3:2}, {"c":3,"d":4}) == {1: 1, 3: 2, 'c': 3, 'd': 4}

    