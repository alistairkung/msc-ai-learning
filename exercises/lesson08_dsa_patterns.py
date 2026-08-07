from collections import defaultdict


def contains_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return True

        seen.add(number)

    return False


def first_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return number

        seen.add(number)

    return None


def two_sum(numbers, target):
    seen = {}

    for index, number in enumerate(numbers):
        lookup = target - number

        if lookup in seen:
            return (seen[lookup], index)

        seen[number] = index

    return None


def are_anagrams(first, second):
    first_counts = defaultdict(int)
    second_counts = defaultdict(int)

    for letter in first.lower():
        first_counts[letter] += 1

    for letter in second.lower():
        second_counts[letter] += 1

    return first_counts == second_counts


def is_palindrome(text):
    processed_text = "".join(text.lower().split())
    left = 0
    right = len(processed_text) - 1

    while left < right:
        if processed_text[left] != processed_text[right]:
            return False

        left += 1
        right -= 1

    return True


def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            return (left, right)

    return None


def reverse_list(items):
    left = 0
    right = len(items) - 1

    while left < right:
        swap_left = items[right]
        swap_right = items[left]
        items[left] = swap_left
        items[right] = swap_right

        left += 1
        right -= 1

    return items
