def create_student(name, age, course):
    return {"name": name, "age": age, "course": course}


def add_grade(student, grade):
    student["grade"] = grade


def get_grade(student):
    return student.get("grade")


def student_names(students):
    return [student["name"] for student in students.values()]


def remove_student(students, student_id):
    return students.pop(student_id, None)


def count_words(words):
    counts = {}

    for word in words:
        counts[word] = counts.get(word, 0) + 1

    return counts


def increment_inventory(inventory, item, amount):
    inventory[item] = inventory.get(item, 0) + amount


def average_grade(grades):
    if not grades:
        return None

    sum_of_grades = sum(grades.values())
    total_students = len(grades)

    return sum_of_grades / total_students


def find_top_student(grades):
    if not grades:
        return None

    return max(grades.items(), key=lambda item: item[1])


def merge_settings(defaults, overrides):
    return defaults | overrides


def invert_dictionary(dictionary):
    new_dict = {}

    for key, value in dictionary:
        new_dict[dictionary.get(key)] = key

    return new_dict


def group_students_by_course(students):
    courses = {}

    for student in students:
        student_name = student["name"]
        course = student["course"]

        courses.setdefault(course, []).append(student_name)

    return courses
