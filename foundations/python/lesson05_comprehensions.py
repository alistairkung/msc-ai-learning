from collections import defaultdict


def square_numbers(numbers):
    return [number**2 for number in numbers]


def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]


def long_words(words, minimum_length):
    return [word for word in words if len(word) > minimum_length]


def word_lengths(words):
    return {word: len(word) for word in words}


def lowercase_unique_words(words):
    return {word.lower() for word in words}


def course_names(students):
    return [student["course"] for student in students]


def passing_student_names(students, pass_mark):
    return [student["name"] for student in students if student["grade"] >= pass_mark]


def grade_lookup(students):
    return {student["name"]: student["grade"] for student in students}


def student_summaries(students):
    return [f"{student['name']} studies {student['course']}" for student in students]


def names_by_course(students):
    course_dictionary = defaultdict(list)

    for student in students:
        course_dictionary[student["course"]].append(student["name"])

    return course_dictionary
