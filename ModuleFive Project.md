# Module 5 Project

## Project 005 — HR Utility Toolkit

### Difficulty Level

🟡 Beginner to Intermediate

---

# Project Story

## EduTech Africa Ltd — Refactoring the HR System

Congratulations!

Your Employee Directory System is now being used by the HR department.

However, there is a problem.

As more features were added, the program became:

* Long
* Difficult to maintain
* Hard to read
* Difficult to upgrade

Your manager has asked you to improve the code quality.

Instead of writing everything in one file, you will now create reusable functions.

This new version will be called:

```text
HR Utility Toolkit
```

---

# Business Requirement

The HR department wants reusable tools for:

* Adding employees
* Viewing employees
* Searching employees
* Counting employees by department
* Generating performance grades

Each task should be handled by its own function.

---

# Learning Objective

Students should understand:

> Functions allow us to write code once and reuse it many times.

---

# Concepts Covered

Students must use:

* Functions
* Parameters
* Return values
* Scope
* Default arguments
* Docstrings
* Type hints (optional)
* Lists
* Dictionaries

---

# Functional Requirements

The system should provide:

### Function 1

Add Employee

```python
add_employee()
```

---

### Function 2

View Employees

```python
view_employees()
```

---

### Function 3

Search Employee

```python
search_employee()
```

---

### Function 4

Generate Grade

```python
generate_grade()
```

---

### Function 5

Count Departments

```python
count_departments()
```

---

# Sample Output

```text
====================================
HR UTILITY TOOLKIT
====================================

1. Add Employee
2. View Employees
3. Search Employee
4. Department Summary
5. Exit
```

---

# Student Task

Create:

```text
hr_toolkit.py
```

Refactor the Employee Directory System using functions.

---

# Project Rules

You must:

✅ Create at least 5 functions

✅ Use parameters

✅ Use return statements

✅ Add docstrings

✅ Avoid repeating code

---

# Helpful Hints

## Hint 1

Functions start with:

```python
def function_name():
    pass
```

---

## Hint 2

Functions can receive information.

Example:

```python
def greet(name):
    print(f"Hello {name}")
```

---

## Hint 3

Functions can return values.

```python
def square(number):
    return number * number
```

---

# Project Checklist

Before viewing the solution:

☐ Did I create functions?

☐ Did I use parameters?

☐ Did I use return values?

☐ Did I add docstrings?

☐ Did I reduce code repetition?

☐ Did I separate responsibilities properly?

---

# Instructor Solution

```python
employees = []


def generate_grade(score):
    """
    Generates employee performance grade.
    """

    if score >= 90:
        return "Excellent"

    elif score >= 70:
        return "Very Good"

    elif score >= 50:
        return "Good"

    elif score >= 40:
        return "Fair"

    return "Poor"


def add_employee():
    """
    Add a new employee.
    """

    employee_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    score = int(input("Performance Score: "))

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "score": score,
        "grade": generate_grade(score)
    }

    employees.append(employee)

    print("Employee added successfully.")


def view_employees():
    """
    Display all employees.
    """

    if len(employees) == 0:
        print("No employee records found.")
        return

    for employee in employees:
        print("\n----------------")
        print(f"ID: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Grade: {employee['grade']}")


def search_employee(employee_id):
    """
    Search employee by ID.
    """

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    return None


def count_departments():
    """
    Count employees per department.
    """

    result = {}

    for employee in employees:
        department = employee["department"]

        result[department] = (
            result.get(department, 0) + 1
        )

    return result
```

---

# Code Walkthrough

## Function 1 — generate_grade()

```python
def generate_grade(score):
```

This function receives a score and returns a grade.

---

## Function 2 — add_employee()

```python
def add_employee():
```

Handles all employee creation.

---

## Function 3 — view_employees()

```python
def view_employees():
```

Displays employee records.

---

## Function 4 — search_employee()

```python
def search_employee(employee_id):
```

Accepts an ID and returns an employee record.

---

## Function 5 — count_departments()

```python
def count_departments():
```

Creates a department summary.

---

# Professional Upgrade Challenge

Create:

```python
update_employee()
```

Function.

Allow HR to:

* Update employee name
* Update department
* Update score

---

# Super Challenge

Create:

```python
generate_employee_email()
```

Example:

```text
Adewale Oladiti
```

becomes:

```text
adewale.oladiti@edutechafrica.com
```

---

# Expert Challenge

Create:

```python
calculate_bonus()
```

Rules:

| Grade     | Bonus   |
| --------- | ------- |
| Excellent | ₦50,000 |
| Very Good | ₦25,000 |
| Good      | ₦10,000 |
| Fair      | ₦0      |
| Poor      | ₦0      |

---

# Real-World Connection

This project mirrors how real software engineers work.

When applications grow:

```text
Bad:
500 lines in one file

Good:
Small reusable functions
```

Functions are one of the foundations of:

* Web Development
* APIs
* Automation
* Data Science
* Enterprise Applications

---

# Portfolio Section

## Project Name

HR Utility Toolkit

---

## What I Built

A Python-based HR utility system that uses reusable functions to manage employee records, generate performance grades, search employee information, and summarize departmental data.

---

## Skills Demonstrated

* Function Design
* Parameters
* Return Values
* Scope
* Code Reusability
* Business Logic
* Refactoring

---

## Resume Description

Developed a modular HR Utility Toolkit using Python functions to manage employee records, automate performance grading, and generate department summaries while applying software engineering best practices for code reusability and maintainability.

---

## GitHub Repository Name

```text
hr-utility-toolkit
```

---

# What Students Have Achieved

After completing this project, students have:

✅ Written reusable functions

✅ Reduced code duplication

✅ Applied software engineering principles

✅ Organized business logic into modules

✅ Built Project #5 in the HR Management System journey

---
