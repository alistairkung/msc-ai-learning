from exercises.lesson07_functions import (
    build_profile,
    describe_person,
    greet,
    power,
    total,
)


def test_greet_default_language():
    assert greet("Alice") == "Hello Alice (English)"


def test_greet_custom_language():
    assert greet("Alice", "French") == "Hello Alice (French)"


def test_power_default():
    assert power(3) == 9


def test_power_custom():
    assert power(2, 5) == 32


def test_describe_person():
    assert (
        describe_person(
            name="Alice",
            age=30,
        )
        == "Alice is 30 years old."
    )


def test_total():
    assert total(1, 2, 3, 4) == 10


def test_build_profile():
    assert build_profile(
        name="Alice",
        age=30,
    ) == {
        "name": "Alice",
        "age": 30,
    }
