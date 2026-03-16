from problems_3 import count_char_freq, is_anagram

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


    