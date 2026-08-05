def longest_word(words):
    return max(words, key=len)


def shortest_word(words):
    return min(words, key=len)


def sort_words_by_length(words):
    return sorted(words, key=len)


def sort_words_by_last_letter(words):
    return sorted(words, key=lambda w: w[-1])


def highest_grade(grades):
    return max(grades.items(), key=lambda item: item[1])


def lowest_grade(grades):
    return min(grades.items(), key=lambda item: item[1])


def alphabetical_students(students):
    return sorted(students, key=lambda student: student["name"])


def longest_name(students):
    return max(students, key=lambda student: len(student["name"]))


def oldest_person(people):
    return max(people, key=lambda person: person["age"])


def sort_people_by_age(people):
    return sorted(people, key=lambda person: person["age"])
