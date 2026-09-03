from lesson09_sliding_window import (
    longest_sum_at_most,
    longest_unique_substring,
    max_average_of_k,
    max_sum_of_k,
)

# --------------------------------------------------
# 1. Fixed window: maximum sum
# --------------------------------------------------


def test_max_sum_of_k():
    assert max_sum_of_k([2, 1, 5, 1, 3, 2], 3) == 9


def test_max_sum_of_k_at_start():
    assert max_sum_of_k([9, 4, 1, 2, 3], 2) == 13


def test_max_sum_of_k_at_end():
    assert max_sum_of_k([1, 2, 3, 8, 9], 2) == 17


def test_max_sum_of_k_entire_list():
    assert max_sum_of_k([1, 2, 3], 3) == 6


def test_max_sum_of_k_with_negative_numbers():
    assert max_sum_of_k([-4, -2, -7, -1], 2) == -6


# --------------------------------------------------
# 2. Fixed window: maximum average
# --------------------------------------------------


def test_max_average_of_k():
    assert max_average_of_k([1, 12, -5, -6, 50, 3], 4) == 12.75


def test_max_average_of_k_at_start():
    assert max_average_of_k([10, 8, 1, 2, 3], 2) == 9


def test_max_average_of_k_entire_list():
    assert max_average_of_k([2, 4, 6, 8], 4) == 5


# --------------------------------------------------
# 3. Variable window: longest unique substring
# --------------------------------------------------


def test_longest_unique_substring():
    assert longest_unique_substring("abcabcbb") == 3


def test_longest_unique_substring_all_unique():
    assert longest_unique_substring("abcdef") == 6


def test_longest_unique_substring_all_same():
    assert longest_unique_substring("bbbb") == 1


def test_longest_unique_substring_with_repeated_middle_character():
    assert longest_unique_substring("pwwkew") == 3


def test_longest_unique_substring_empty_string():
    assert longest_unique_substring("") == 0


def test_longest_unique_substring_single_character():
    assert longest_unique_substring("a") == 1


# --------------------------------------------------
# 3. Variable window: sum at most
# --------------------------------------------------


def test_longest_sum_at_most():
    assert longest_sum_at_most([2, 3, 1, 2, 4, 3], 10) == 4
