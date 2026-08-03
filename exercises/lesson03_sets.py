def create_cities():
    return {"London", "Hong Kong", "Singapore"}


def add_city(cities, city):
    cities.add(city)


def contains_city(cities, city):
    return city in cities


def unique_cities(cities):
    return set(cities)


def common_cities(first, second):
    return first & second


def cities_only_in_first(first, second):
    return first - second


def cities_only_in_second(first, second):
    return second - first


def has_duplicates(items):
    return len(set(items)) != len(items)


def remove_city(cities, city):
    cities.discard(city)


def merge_city_sets(first, second):
    return first | second


def count_unique_cities(cities):
    return len(set(cities))


def is_subset(first, second):
    return first.issubset(second)


def invert_membership(students):
    return {student: True for student in students}
