import numpy as np

from lesson10_numpy import (
    add_arrays,
    add_ten,
    array_shape,
    calculate_errors,
    column_maximums,
    column_means,
    column_sums,
    count_passing,
    element_at,
    failing_grades,
    feature_means,
    first_column,
    first_row,
    first_two_columns,
    first_two_rows,
    grades_between,
    last_column,
    multiply_arrays,
    number_of_dimensions,
    number_of_elements,
    passing_grades,
    replace_failing_with_zero,
    row_means,
    row_minimums,
    row_sums,
    square,
    squared_errors,
    times_two,
    top_left,
    total,
)

MATRIX = np.array(
    [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [90, 100, 110, 120],
    ]
)


def test_array_shape():
    assert array_shape(MATRIX) == (3, 4)


def test_number_of_dimensions():
    assert number_of_dimensions(MATRIX) == 2


def test_number_of_elements():
    assert number_of_elements(MATRIX) == 12


def test_first_row():
    result = first_row(MATRIX)

    np.testing.assert_array_equal(
        result,
        np.array([10, 20, 30, 40]),
    )


def test_first_column():
    result = first_column(MATRIX)

    np.testing.assert_array_equal(
        result,
        np.array([10, 50, 90]),
    )


def test_last_column():
    result = last_column(MATRIX)

    np.testing.assert_array_equal(
        result,
        np.array([40, 80, 120]),
    )


def test_element_at():
    assert element_at(MATRIX, 1, 2) == 70


def test_first_two_rows():
    result = first_two_rows(MATRIX)

    np.testing.assert_array_equal(
        result,
        np.array(
            [
                [10, 20, 30, 40],
                [50, 60, 70, 80],
            ]
        ),
    )


def test_first_two_columns():
    result = first_two_columns(MATRIX)

    np.testing.assert_array_equal(
        result,
        np.array(
            [
                [10, 20],
                [50, 60],
                [90, 100],
            ]
        ),
    )


def test_top_left():
    result = top_left(MATRIX)

    np.testing.assert_array_equal(
        result,
        np.array(
            [
                [10, 20],
                [50, 60],
            ]
        ),
    )


def test_add_ten():
    array = np.array([1, 2, 3])

    result = add_ten(array)

    np.testing.assert_array_equal(
        result,
        np.array([11, 12, 13]),
    )


def test_times_two():
    array = np.array([1, 2, 3])

    result = times_two(array)

    np.testing.assert_array_equal(
        result,
        np.array([2, 4, 6]),
    )


def test_square():
    array = np.array([1, 2, 3, 4])

    result = square(array)

    np.testing.assert_array_equal(
        result,
        np.array([1, 4, 9, 16]),
    )


def test_add_arrays():
    first = np.array([1, 2, 3])
    second = np.array([10, 20, 30])

    result = add_arrays(first, second)

    np.testing.assert_array_equal(
        result,
        np.array([11, 22, 33]),
    )


def test_multiply_arrays():
    first = np.array([1, 2, 3])
    second = np.array([10, 20, 30])

    result = multiply_arrays(first, second)

    np.testing.assert_array_equal(
        result,
        np.array([10, 40, 90]),
    )


def test_calculate_errors():
    predictions = np.array([10, 15, 20])
    actual = np.array([12, 14, 18])

    result = calculate_errors(predictions, actual)

    np.testing.assert_array_equal(
        result,
        np.array([-2, 1, 2]),
    )


def test_squared_errors():
    predictions = np.array([10, 15, 20])
    actual = np.array([12, 14, 18])

    result = squared_errors(predictions, actual)

    np.testing.assert_array_equal(
        result,
        np.array([4, 1, 4]),
    )


def test_passing_grades():
    grades = np.array([45, 72, 81, 39, 65, 90])

    result = passing_grades(grades)

    np.testing.assert_array_equal(
        result,
        np.array([72, 81, 65, 90]),
    )


def test_failing_grades():
    grades = np.array([45, 72, 81, 39, 65, 90])

    result = failing_grades(grades)

    np.testing.assert_array_equal(
        result,
        np.array([45, 39]),
    )


def test_grades_between():
    grades = np.array([45, 72, 81, 39, 65, 90])

    result = grades_between(grades, 50, 80)

    np.testing.assert_array_equal(
        result,
        np.array([72, 65]),
    )


def test_count_passing():
    grades = np.array([45, 72, 81, 39, 65, 90])

    assert count_passing(grades) == 4


def test_replace_failing_with_zero():
    grades = np.array([45, 72, 81, 39, 65, 90])

    result = replace_failing_with_zero(grades)

    np.testing.assert_array_equal(
        result,
        np.array([0, 72, 81, 0, 65, 90]),
    )


def test_total():
    array = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
        ]
    )

    assert total(array) == 210


def test_column_sums():
    array = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
        ]
    )

    result = column_sums(array)

    np.testing.assert_array_equal(
        result,
        np.array([50, 70, 90]),
    )


def test_row_sums():
    array = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
        ]
    )

    result = row_sums(array)

    np.testing.assert_array_equal(
        result,
        np.array([60, 150]),
    )


def test_column_means():
    array = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
        ]
    )

    result = column_means(array)

    np.testing.assert_array_equal(
        result,
        np.array([25, 35, 45]),
    )


def test_row_means():
    array = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
        ]
    )

    result = row_means(array)

    np.testing.assert_array_equal(
        result,
        np.array([20, 50]),
    )


def test_column_maximums():
    array = np.array(
        [
            [10, 80, 30],
            [40, 20, 90],
            [25, 70, 50],
        ]
    )

    result = column_maximums(array)

    np.testing.assert_array_equal(
        result,
        np.array([40, 80, 90]),
    )


def test_row_minimums():
    array = np.array(
        [
            [10, 80, 30],
            [40, 20, 90],
            [25, 70, 50],
        ]
    )

    result = row_minimums(array)

    np.testing.assert_array_equal(
        result,
        np.array([10, 20, 25]),
    )


def test_feature_means():
    features = np.array(
        [
            # age, income, score
            [20, 30000, 70],
            [30, 50000, 80],
            [40, 70000, 90],
            [50, 90000, 100],
        ]
    )

    result = feature_means(features)

    np.testing.assert_array_equal(
        result,
        np.array([35, 60000, 85]),
    )
