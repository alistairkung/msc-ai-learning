def create_cities():
    return ["London", "Hong Kong", "Singapore"]


def add_city(cities, city):
    cities.append(city)


def last_city(cities):
    return cities[-1]


def contains_city(cities, city):
    return city in cities


def count_cities(cities):
    return len(cities)


def alphabetical_cities(cities):
    upcased_cities = []
    for city in cities:
        upcased_cities.append(city.upper())

    return sorted(upcased_cities)
