from lesson03_sets import (
    add_city,
    cities_only_in_first,
    cities_only_in_second,
    common_cities,
    contains_city,
    count_unique_cities,
    create_cities,
    has_duplicates,
    invert_membership,
    is_subset,
    merge_city_sets,
    remove_city,
    unique_cities,
)


def test_create_cities():
    assert create_cities() == {
        "London",
        "Hong Kong",
        "Singapore",
    }


def test_add_city():
    cities = {
        "London",
        "Hong Kong",
    }

    add_city(cities, "Singapore")

    assert cities == {
        "London",
        "Hong Kong",
        "Singapore",
    }


def test_adding_duplicate_city_has_no_effect():
    cities = {
        "London",
        "Hong Kong",
    }

    add_city(cities, "London")

    assert cities == {
        "London",
        "Hong Kong",
    }


def test_contains_city():
    cities = {
        "London",
        "Hong Kong",
    }

    assert contains_city(cities, "London") is True
    assert contains_city(cities, "Singapore") is False


def test_unique_cities():
    cities = [
        "London",
        "Hong Kong",
        "London",
        "Singapore",
        "Singapore",
    ]

    assert unique_cities(cities) == {
        "London",
        "Hong Kong",
        "Singapore",
    }


def test_common_cities():
    first = {
        "London",
        "Hong Kong",
        "Singapore",
    }

    second = {
        "Hong Kong",
        "Tokyo",
    }

    assert common_cities(first, second) == {
        "Hong Kong",
    }


def test_cities_only_in_first():
    first = {
        "London",
        "Hong Kong",
        "Singapore",
    }

    second = {
        "Hong Kong",
        "Tokyo",
    }

    assert cities_only_in_first(first, second) == {
        "London",
        "Singapore",
    }


def test_cities_only_in_second():
    first = {
        "London",
        "Hong Kong",
    }

    second = {
        "Hong Kong",
        "Tokyo",
    }

    assert cities_only_in_second(first, second) == {
        "Tokyo",
    }


def test_has_duplicates():
    assert has_duplicates(["a", "b", "c"]) is False
    assert has_duplicates(["a", "b", "a"]) is True
    assert has_duplicates([]) is False


def test_remove_city():
    cities = {
        "London",
        "Hong Kong",
        "Singapore",
    }

    remove_city(cities, "Hong Kong")

    assert cities == {
        "London",
        "Singapore",
    }


def test_remove_missing_city_does_not_raise():
    cities = {
        "London",
        "Hong Kong",
    }

    remove_city(cities, "Tokyo")

    assert cities == {
        "London",
        "Hong Kong",
    }


def test_merge_city_sets():
    first = {
        "London",
        "Hong Kong",
    }

    second = {
        "Hong Kong",
        "Singapore",
    }

    assert merge_city_sets(first, second) == {
        "London",
        "Hong Kong",
        "Singapore",
    }


def test_merge_does_not_mutate_inputs():
    first = {
        "London",
    }

    second = {
        "Singapore",
    }

    merge_city_sets(first, second)

    assert first == {"London"}
    assert second == {"Singapore"}


def test_count_unique_cities():
    cities = [
        "London",
        "London",
        "Singapore",
        "Hong Kong",
    ]

    assert count_unique_cities(cities) == 3


def test_is_subset():
    first = {
        "London",
        "Hong Kong",
    }

    second = {
        "London",
        "Hong Kong",
        "Singapore",
    }

    assert is_subset(first, second) is True
    assert is_subset(second, first) is False


def test_invert_membership():
    students = {
        "Alice",
        "Bob",
        "Charlie",
    }

    assert invert_membership(students) == {
        "Alice": True,
        "Bob": True,
        "Charlie": True,
    }
