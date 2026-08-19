import pandas as pd


def make_students():
    return pd.DataFrame(
        {
            "name": ["Alice", "Bob", "Cara", "Dan"],
            "course": ["ML", "NLP", "ML", "NLP"],
            "grade": [82, 71, 93, 64],
            "attendance": [0.91, 0.84, 0.96, 0.72],
        }
    )


def get_grades(students):
    return students["grade"]


def get_names_and_grades(students):
    return students[["name", "grade"]]


def get_high_achievers(students, minimum_grade):
    return students[students["grade"] >= minimum_grade]


def get_ml_students(students):
    return students[students["course"] == "ML"]


def get_engaged_students(students, minimum_grade, minimum_attendance):
    meets_minimum_grades = students["grade"] >= minimum_grade
    meets_minimum_attendance = students["attendance"] >= minimum_attendance

    return students[meets_minimum_grades & meets_minimum_attendance]


def get_ml_or_high_grade(students, minimum_grade):
    meets_minimum_grades = students["grade"] >= minimum_grade
    studies_ml = students["course"] == "ML"

    return students[meets_minimum_grades | studies_ml]


def get_high_achiever_summary(students, minimum_grade):
    meets_minimum_grades = students["grade"] >= minimum_grade

    return students.loc[meets_minimum_grades, ["name", "grade"]]


def get_first_two_students(students):
    return students.iloc[0:2]


def get_top_left(students):
    return students.iloc[0:2, 0:2]


def add_passed_column(students, pass_grade):
    df = students.copy()
    df["passed"] = df["grade"] >= pass_grade

    return df


def add_weighted_score(students):
    df = students.copy()
    df["weighted_score"] = df["grade"] * df["attendance"]

    return df


def rank_students(students):
    return students.sort_values("grade", ascending=False)


def sort_by_course_and_grade(students):
    return students.sort_values(["course", "grade"], ascending=[True, False])


def remove_missing_grades(students):
    df = students.copy()

    return df.dropna(subset=["grade"])


def fill_missing_grades(students):
    df = students.copy()
    mean = df["grade"].mean()

    df["grade"] = df["grade"].fillna(mean)
    return df


def average_grade_by_course(students):
    return students.groupby("course")["grade"].mean()


def highest_grade_by_course(students):
    return students.groupby("course")["grade"].max()


def grade_statistics_by_course(students):
    return students.groupby("course")["grade"].agg(["mean", "max", "min"])


def course_summary(students):
    return students.groupby("course")["grade"].agg(["mean", "max", "min"]).reset_index()


def add_teacher_information(students, courses):
    return students.merge(courses, on="course")


def add_teacher_information_keep_all(students, courses):
    return students.merge(courses, on="course", how="left")
