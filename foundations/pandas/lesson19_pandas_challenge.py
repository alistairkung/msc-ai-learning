def clean_students(students):
    df = students.copy()
    mean = students["grade"].mean()
    df["grade"] = df["grade"].fillna(mean)
    df["weighted_score"] = df["grade"] * df["attendance"]

    return df


def top_students(students, minimum_grade, minimum_attendance):
    meets_minimum_grade_mask = students["grade"] >= minimum_grade
    meets_minimum_attendance_mask = students["attendance"] >= minimum_attendance

    return students[
        meets_minimum_grade_mask & meets_minimum_attendance_mask
    ].sort_values("grade", ascending=False)


def course_performance(students):
    result = students.groupby("course")["grade"].agg(["mean", "max"]).reset_index()
    return result.rename(columns={"mean": "mean_grade", "max": "highest_grade"})
