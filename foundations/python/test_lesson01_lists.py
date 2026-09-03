from exercises.lesson01_lists import (
    add_city,
    alphabetical_cities,
    contains_city,
    count_cities,
    create_cities,
    last_city,
)


def test_cities_exist():
    expected_cities = ["London", "Hong Kong", "Singapore"]

    assert create_cities() == expected_cities


def test_add_city():
    cities = create_cities()

    add_city(cities, "New York")

    assert cities == ["London", "Hong Kong", "Singapore", "New York"]


def test_last_city():
    cities = create_cities()

    assert last_city(cities) == "Singapore"


def test_contains_city():
    cities = create_cities()

    assert contains_city(cities, "Hong Kong") is True


def test_cities_count():
    cities = create_cities()

    assert count_cities(cities) == 3


def test_alphabetical_cities():
    cities = create_cities()

    assert alphabetical_cities(cities) == ["HONG KONG", "LONDON", "SINGAPORE"]
