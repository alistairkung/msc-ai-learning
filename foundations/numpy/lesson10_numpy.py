def array_shape(array):
    return array.shape


def number_of_dimensions(array):
    return array.ndim


def number_of_elements(array):
    return array.size


def first_row(array):
    return array[0]


def first_column(array):
    return array[:, 0]


def last_column(array):
    return array[:, -1]


def element_at(array, row, column):
    return array[row, column]


def first_two_rows(array):
    return array[:2]


def first_two_columns(array):
    return array[:, :2]


def top_left(array):
    return array[:2, :2]


def add_ten(array):
    return array + 10


def times_two(array):
    return array * 2


def square(array):
    return array**2


def add_arrays(first, second):
    return first + second


def multiply_arrays(first, second):
    return first * second


def calculate_errors(predictions, actual):
    return predictions - actual


def squared_errors(predictions, actual):
    return (predictions - actual) ** 2


def passing_grades(grades):
    return grades[grades >= 50]


def failing_grades(grades):
    return grades[grades < 50]


def grades_between(grades, minimum, maximum):
    condition = (grades >= minimum) & (grades < maximum)
    return grades[condition]


def count_passing(grades):
    return grades[grades >= 50].size


def replace_failing_with_zero(grades):
    result = grades.copy()

    result[result < 50] = 0

    return result


def total(array):
    return array.sum()


def column_sums(array):
    return array.sum(axis=0)


def row_sums(array):
    return array.sum(axis=1)


def column_means(array):
    return array.mean(axis=0)


def row_means(array):
    return array.mean(axis=1)


def column_maximums(array):
    return array.max(axis=0)


def row_minimums(array):
    return array.min(axis=1)


def feature_means(features):
    return features.mean(axis=0)
