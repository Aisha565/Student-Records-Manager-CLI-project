from datetime import datetime
from stats_helper import calculate_statistics


def show_statistics(students):

    print("\n===== Statistics =====")

    if len(students) == 0:
        print("No students found.")
        return

    result = calculate_statistics(students)

    if result is None:
        print("No grades available to calculate statistics.")
        return

    subject_totals, subject_counts, highest_student, lowest_student, grade_bands = result

    # Total Students
    print("Total Students:", len(students))

    # Subject Averages
    print("\nClass Average Per Subject:")

    for subject in subject_totals:
        average = subject_totals[subject] / subject_counts[subject]
        print(f"{subject.capitalize():<12}: {average:.2f}")

    # Highest Student
    print("\nHighest Scoring Student:")
    print(f"{highest_student['name']} ({highest_student['average']:.2f})")

    # Lowest Student
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

    result = calculate_statistics(students)

    if result is None:
        print("No grades available to export report.")
        return

    subject_totals, subject_counts, highest_student, lowest_student, grade_bands = result

    with open("report.txt", "w", encoding="utf-8") as file:

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