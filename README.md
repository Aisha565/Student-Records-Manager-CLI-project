# 📚 Student Records Manager (CLI)

## 📌 Project Description

Student Records Manager is a Python-based Command Line Interface (CLI) application developed to efficiently manage student records. The application allows users to add, search, update, delete, and list student information. It also generates class statistics and exports reports while storing all student records permanently in a JSON file.

The project follows a modular programming approach by separating the application into different modules for validation, storage, and statistics.

---

# 🎯 Objectives

- Manage student records through a CLI application.
- Store student data permanently using JSON.
- Validate user input before saving data.
- Generate student statistics.
- Export reports to a text file.
- Practice modular programming in Python.
- Improve code readability and maintainability.

---

# ✨ Features

- Add Student
- List Students (Sorted Alphabetically)
- Search Student by Name or Email
- Update Student Information
- Delete Student by Name
- Display All Matching Student Records
- Select the Required Student from the Matching List
- Confirmation Before Deletion
- Generate Student Statistics
- Export Report to Text File
- Automatic Student ID Generation
- Input Validation
- Duplicate Email Prevention
- JSON Data Storage
- Modular Programming

---

# 🛠 Technologies Used

- Python 3
- JSON
- Regular Expressions (`re`)
- Datetime Module

---

# 📂 Project Structure

```text
student-records-cli/
│
├── main.py
├── models.py
├── storage.py
├── stats.py
├── README.md
├── report.txt
│
└── data/
    └── students.json
```

---

# 📁 Module Description

## main.py

This is the main entry point of the application.

Responsibilities:

- Display the menu
- Handle user interaction
- Manage program flow
- Call functions from other modules

The application starts using:

```python
if __name__ == "__main__":
    main()
```

This ensures that the program runs only when `main.py` is executed directly.

---

## models.py

This module contains all input validation functions.

### Validation Functions

- Name Validation
- Email Validation
- Duplicate Email Validation
- Age Validation
- Subject Validation
- Grade Validation

---

## storage.py

This module is responsible for loading and saving student records using JSON.

Functions:

- `load_students()`
- `save_students()`

Student records are stored in:

```text
data/students.json
```

---

## stats.py

This module generates statistics and exports reports.

Functions:

- `show_statistics()`
- `export_report()`

---

# 👨‍🎓 Student Information

Each student record contains:

- Student ID
- Name
- Email
- Age
- Subjects
- Grades

Example:

```json
{
    "id": 1,
    "name": "Ayesha",
    "email": "ayesha@gmail.com",
    "age": 22,
    "grades": {
        "Math": 90,
        "English": 85
    }
}
```

---

# ✅ Validation Rules

## Name

- Cannot be empty
- Leading and trailing spaces are removed
- Minimum 3 characters
- Maximum 30 characters
- Only alphabets and spaces are allowed

---

## Email

- Must follow a valid email format
- Duplicate emails are not allowed
- Each student must have a unique email address

---

## Age

- Must be between 18 and 60

---

## Subject

- Cannot be empty
- Only alphabets and spaces are allowed

---

## Grade

- Must be between 0 and 100

---

# 🗑 Delete Student Process

The delete operation works as follows:

1. The user enters the student's name.
2. The system searches for all students with the same name.
3. All matching student records are displayed.
4. The user selects the desired student by entering the Student ID from the displayed list.
5. The system asks for confirmation before deletion.
6. The selected student is permanently deleted.

This approach ensures that the correct student is deleted even when multiple students have the same name.

---

# 📊 Statistics

The application provides:

- Total Students
- Class Average Per Subject
- Highest Scoring Student
- Lowest Scoring Student
- Grade Distribution (A, B, C, F)

---

# 📄 Report Generation

The application exports a report named:

```text
report.txt
```

The report includes:

- Current Date & Time
- Total Students
- Subject-wise Average
- Highest Scoring Student
- Lowest Scoring Student
- Grade Distribution

---

# 💾 Data Storage

Student records are stored permanently in:

```text
data/students.json
```

The data is automatically:

- Loaded when the application starts.
- Saved after adding a student.
- Saved after updating a student.
- Saved after deleting a student.

---

# ▶️ How to Run

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run the following command:

```bash
python main.py
```

The application starts through:

```python
if __name__ == "__main__":
    main()
```

---

# 📋 Sample Menu

```text
===== Student Records Manager =====

1. Add Student
2. List Students
3. Search Student
4. Update Student
5. Delete Student
6. Statistics
7. Export Report
8. Exit
```

---

# 🚀 Project Highlights

- Modular Python Project
- Uses Functions, Lists, and Dictionaries
- JSON-Based Data Storage
- Automatic Student ID Generation
- Input Validation
- Duplicate Email Prevention
- Student Statistics
- Report Export Feature
- Smart Student Deletion Using Name with Matching Record Selection
- Uses `if __name__ == "__main__"` as the application entry point

---

# 🔮 Future Improvements

- Search Student by ID
- Update Multiple Student Fields at Once
- GPA Calculation
- CSV Export Support
- User Authentication
- Graphical User Interface (GUI)
- Advanced Filtering and Sorting

---

# 👩‍💻 Author

**Ayesha**

BS Computer Science

Python Student Records Manager (CLI)