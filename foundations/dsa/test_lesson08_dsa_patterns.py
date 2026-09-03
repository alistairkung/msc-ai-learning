from lesson08_dsa_patterns import (
    are_anagrams,
    contains_duplicate,
    first_duplicate,
    is_palindrome,
    reverse_list,
    two_sum,
    two_sum_sorted,
)


def test_contains_duplicate_when_duplicate_exists():
    assert contains_duplicate([4, 2, 7, 1, 2]) is True


def test_contains_duplicate_when_all_unique():
    assert contains_duplicate([4, 2, 7, 1]) is False


def test_contains_duplicate_with_empty_list():
    assert contains_duplicate([]) is False


def test_first_duplicate():
    assert first_duplicate([4, 2, 7, 1, 2, 7]) == 2


def test_first_duplicate_returns_none_when_unique():
    assert first_duplicate([4, 2, 7, 1]) is None


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)


def test_two_sum_with_later_match():
    assert two_sum([3, 2, 4], 6) == (1, 2)


def test_two_sum_with_duplicate_values():
    assert two_sum([3, 3], 6) == (0, 1)


def test_two_sum_returns_none_when_no_pair_exists():
    assert two_sum([1, 2, 3], 20) is None


def test_are_anagrams():
    assert are_anagrams("listen", "silent") is True


def test_are_anagrams_when_not_anagrams():
    assert are_anagrams("hello", "world") is False


def test_are_anagrams_ignores_case():
    assert are_anagrams("Listen", "Silent") is True


def test_are_anagrams_with_repeated_letters():
    assert are_anagrams("aabbcc", "abcabc") is True


def test_are_anagrams_with_different_counts():
    assert are_anagrams("aabb", "abbb") is False


def test_is_palindrome():
    assert is_palindrome("racecar") is True


def test_is_palindrome_when_not_palindrome():
    assert is_palindrome("python") is False


def test_is_palindrome_ignores_case():
    assert is_palindrome("RaceCar") is True


def test_is_palindrome_ignores_spaces():
    assert is_palindrome("never odd or even") is True


def test_two_sum_sorted():
    assert two_sum_sorted([1, 2, 4, 7, 11, 15], 15) == (2, 4)


def test_two_sum_sorted_with_first_and_last():
    assert two_sum_sorted([1, 2, 3, 8], 9) == (0, 3)


def test_two_sum_sorted_returns_none():
    assert two_sum_sorted([1, 2, 4, 8], 20) is None


def test_reverse_list():
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]


def test_reverse_list_with_odd_number_of_items():
    assert reverse_list([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]


def test_reverse_list_with_empty_list():
    assert reverse_list([]) == []
