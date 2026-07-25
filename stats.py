from datetime import datetime

def show_statistics(students):

    print("\n===== Statistics =====")

    if len(students) == 0:
        print("No students found.")
        return

    # Total Students
    print("Total Students:", len(students))

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

    # Loop through all students
    for student in students:

        grades = student["grades"]

        total = 0

        # Subject totals
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

    # Subject Averages
    print("\nClass Average Per Subject:")

    for subject in subject_totals:
        average = subject_totals[subject] / subject_counts[subject]
        print(f"{subject.capitalize():<12}: {average:.2f}")

    # Highest & Lowest
    print("\nHighest Scoring Student:")
    print(f"{highest_student['name']} ({highest_student['average']:.2f})")

    print("\nLowest Scoring Student:")
    print(f"{lowest_student['name']} ({lowest_student['average']:.2f})")

    # Grade Bands
    print("\nGrade Bands:")
    print("A:", grade_bands["A"])
    print("B:", grade_bands["B"])
    print("C:", grade_bands["C"])
    print("F:", grade_bands["F"])



def export_report(students):

    if len(students) == 0:
        print("No students found.")
        return

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

        total = 0

        for subject, grade in grades.items():

            total += grade

            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0

            subject_totals[subject] += grade
            subject_counts[subject] += 1

        average = total / len(grades)

        if highest_student is None or average > highest_student["average"]:
            highest_student = {
                "name": student["name"],
                "average": average
            }

        if lowest_student is None or average < lowest_student["average"]:
            lowest_student = {
                "name": student["name"],
                "average": average
            }

        if average >= 85:
            grade_bands["A"] += 1
        elif average >= 70:
            grade_bands["B"] += 1
        elif average >= 55:
            grade_bands["C"] += 1
        else:
            grade_bands["F"] += 1

    with open("report.txt", "w") as file:

        file.write("===== Student Report =====\n\n")

        file.write("Date: " + str(datetime.now()) + "\n\n")

        file.write(f"Total Students: {len(students)}\n\n")

        file.write("Class Average Per Subject\n")

        for subject in subject_totals:
            average = subject_totals[subject] / subject_counts[subject]
            file.write(f"{subject.capitalize()}: {average:.2f}\n")

        file.write("\nHighest Student:\n")
        file.write(f"{highest_student['name']} ({highest_student['average']:.2f})\n")

        file.write("\nLowest Student:\n")
        file.write(f"{lowest_student['name']} ({lowest_student['average']:.2f})\n")

        file.write("\nGrade Bands\n")
        file.write(f"A: {grade_bands['A']}\n")
        file.write(f"B: {grade_bands['B']}\n")
        file.write(f"C: {grade_bands['C']}\n")
        file.write(f"F: {grade_bands['F']}\n")

    print("Report exported successfully!")