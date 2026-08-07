def greet(name, language="English"):
    return f"Hello {name} ({language})"


def power(number, exponent=2):
    return number**exponent


def describe_person(*, name, age):
    return f"{name} is {age} years old."


def total(*numbers):
    return sum(numbers)


def build_profile(**kwargs):
    return kwargs
