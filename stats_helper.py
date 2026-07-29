def calculate_statistics(students):

    subject_totals = {}
    subject_counts = {}

    highest_student = None
    lowest_student = None

    grade_bands = {
        "A": 0,
        "B": 0,
        "C": 0,
        "F": 0
    }

    for student in students:

        grades = student["grades"]

        # Edge Case:
        # Skip students who have no grades
        if len(grades) == 0:
            continue

        total = 0

        # Subject Totals
        for subject, grade in grades.items():

            total += grade

            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0

            subject_totals[subject] += grade
            subject_counts[subject] += 1

        average = total / len(grades)

        # Highest Student
        if highest_student is None or average > highest_student["average"]:
            highest_student = {
                "name": student["name"],
                "average": average
            }

        # Lowest Student
        if lowest_student is None or average < lowest_student["average"]:
            lowest_student = {
                "name": student["name"],
                "average": average
            }

        # Grade Bands
        if average >= 85:
            grade_bands["A"] += 1

        elif average >= 70:
            grade_bands["B"] += 1

        elif average >= 55:
            grade_bands["C"] += 1

        else:
            grade_bands["F"] += 1

    # Edge Case:
    # If no student has grades
    if highest_student is None:
        return None

    return (
        subject_totals,
        subject_counts,
        highest_student,
        lowest_student,
        grade_bands
    )