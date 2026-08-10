def max_sum_of_k(numbers, k):
    window_sum = sum(numbers[0:k])
    max_sum = window_sum

    for index in range(k, len(numbers)):
        window_sum = window_sum - numbers[index - k] + numbers[index]
        max_sum = max(window_sum, max_sum)

    return max_sum


def max_average_of_k(numbers, k):
    window_sum = sum(numbers[0:k])
    max_sum = window_sum

    for index in range(k, len(numbers)):
        window_sum = window_sum - numbers[index - k] + numbers[index]
        max_sum = max(window_sum, max_sum)

    return max_sum / k


def longest_unique_substring(text):
    seen = set()
    longest = 0
    left = 0

    for right, char in enumerate(text):
        while char in seen:
            seen.discard(text[left])
            left += 1

        seen.add(char)

        current_length = right - left + 1
        longest = max(longest, current_length)

    return longest
