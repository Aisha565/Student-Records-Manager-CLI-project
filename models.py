import re


def validate_name(name):

    name = name.strip()

    if not name:
        return False

    if len(name) < 3 or len(name) > 30:
        return False

    if not name.replace(" ", "").isalpha():
        return False

    return True


def validate_email(email):

    email = email.strip()

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not re.match(pattern, email):
        return False

    return True


def validate_duplicate_email(email, students):

    email = email.strip().lower()

    for student in students:

        if student["email"].lower() == email:
            return False

    return True


def validate_age(age):

    if age < 18 or age > 60:
        return False

    return True


def validate_subject(subject):

    subject = subject.strip()

    if not subject:
        return False

    if len(subject) < 2 or len(subject) > 20:
        return False

    if not subject.replace(" ", "").isalpha():
        return False

    return True


def validate_grade(grade):

    if grade < 0 or grade > 100:
        return False

    return True