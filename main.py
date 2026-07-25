from stats import show_statistics, export_report
from storage import save_students, load_students
from models import validate_name, validate_email, validate_duplicate_email, validate_age, validate_subject, validate_grade

students = load_students()


# =========================
# Menu
# =========================
def show_menu():
    print("\n===== Student Records Manager =====")
    print("1. Add Student")
    print("2. List Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Statistics")
    print("7. Export Report")
    print("8. Exit")


# =========================
# Helper Functions
# =========================
def generate_id():

    if len(students) == 0:
        return 1

    last_id = 0

    for student in students:
        if student["id"] > last_id:
            last_id = student["id"]

    return last_id + 1


# =========================
# Student Functions
# =========================
def add_student():

    print("\n=== Add Student ===")

    student_id = generate_id()

    # Name Validation
    while True:

        name = input("Enter Name: ")

        if validate_name(name):
            break

        print("Invalid Name! Please enter a valid name.")

    # Email Validation
    while True:

        email = input("Enter Email: ")

        if not validate_email(email):
            print("Invalid Email Format!")
            continue

        if not validate_duplicate_email(email, students):
            print("Email Already Exists!")
            continue

        break

    # Age Validation
    while True:

        try:
            age = int(input("Enter Age: "))

            if validate_age(age):
                break

            print("Age must be between 18 and 60.")

        except ValueError:
            print("Please enter numbers only.")

    grades = {}

    while True:

        # Subject Validation
        while True:

            subject = input("Enter Subject Name: ").lower()

            if validate_subject(subject):
                break

            print("Invalid Subject Name!")

        # Grade Validation
        while True:

            try:
                grade = float(input("Enter Grade: "))

                if validate_grade(grade):
                    break

                print("Grade must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

        grades[subject] = grade

        another = input("Add another subject? (y/n): ").lower()

        if another != "y":
            break

    student = {
        "id": student_id,
        "name": name,
        "email": email,
        "age": age,
        "grades": grades,
    }

    students.append(student)
    save_students(students)

    print("Student Added Successfully!")


def list_students():

    print("\n===== Student List =====")

    if len(students) == 0:
        print("No students found.")
        return

    sorted_students = sorted(students, key=lambda student: student["name"])

    print("-" * 80)
    print(f"{'ID':<5}{'Name':<15}{'Email':<30}{'Age':<5}")
    print("-" * 80)

    for student in sorted_students:
        print(
            f"{student['id']:<5}{student['name']:<15}{student['email']:<30}{student['age']:<5}"
        )


def search_student():

    print("\n===== Search Student =====")

    search = input("Enter student name or email: ").lower()

    found = False

    for student in students:

        if search in student["name"].lower() or search == student["email"].lower():

            print("-" * 40)
            print("ID   :", student["id"])
            print("Name :", student["name"])
            print("Email:", student["email"])
            print("Age  :", student["age"])
            print("Grades:", student["grades"])

            found = True

    if not found:
        print("Student not found.")


def update_student():

    print("\n===== Update Student =====")

    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")

            print("1. Update Email")
            print("2. Update Age")
            print("3. Update Subject Grade")

            choice = input("Enter Choice: ")

            if choice == "1":
                student["email"] = input("Enter New Email: ")

            elif choice == "2":
                student["age"] = int(input("Enter New Age: "))

            elif choice == "3":

                subject = input("Enter Subject Name: ").lower()

                if subject in student["grades"]:

                    new_grade = float(input("Enter New Grade: "))

                    student["grades"][subject] = new_grade

                    print("Grade Updated Successfully!")

                else:
                    print("Subject Not Found!")
                    return

            else:
                print("Invalid Choice!")
                return

            save_students(students)
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


def delete_student():

    print("\n===== Delete Student =====")

    # Name Validation
    while True:

        name = input("Enter Student Name: ")

        if validate_name(name):
            break

        print("Invalid Name!")

    matched_students = []

    # Find all students with the same name
    for student in students:

        if student["name"].lower() == name.lower():
            matched_students.append(student)

    # If no student found
    if len(matched_students) == 0:
        print("Student Not Found!")
        return

    # Display matching students
    print("\nMatching Students")
    print("-" * 80)
    print(f"{'ID':<5}{'Name':<15}{'Email':<30}{'Age':<5}")
    print("-" * 80)

    for student in matched_students:
        print(
            f"{student['id']:<5}"
            f"{student['name']:<15}"
            f"{student['email']:<30}"
            f"{student['age']:<5}"
        )

    # Take ID from user
    while True:

        try:
            student_id = int(input("\nEnter Student ID to Delete: "))
            break

        except ValueError:
            print("Please enter a valid ID.")

    # Delete selected student
    for student in matched_students:

        if student["id"] == student_id:

            confirm = input("Are you sure you want to delete this student? (y/n): ").lower()

            if confirm == "y":

                students.remove(student)
                save_students(students)

                print("Student Deleted Successfully!")

            else:
                print("Delete Cancelled!")

            return

    print("Invalid Student ID!")
# =========================
# Main Function
# =========================
def main():

    while True:

        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            list_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_statistics(students)

        elif choice == "7":
            export_report(students)

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid Choice!")


# =========================
# Program Entry Point
# =========================
if __name__ == "__main__":
    main()