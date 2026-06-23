# Module 4 Project

## Project 004 — Employee Directory System

### Difficulty Level

🟢 Beginner to Intermediate

---

# Project Story

## EduTech Africa Ltd — Employee Directory Upgrade

In Module 2, you built an **Employee Information System**.

In Module 3, you upgraded it into an **Employee Performance Evaluation System**.

Now, EduTech Africa Ltd has more employees, and HR can no longer manage one employee at a time.

The company now wants a system that can store and manage multiple employee records.

Your task is to build an **Employee Directory System** using Python collections.

---

# Business Requirement

The HR department wants a simple program that can:

* Store multiple employees
* Display all employees
* Search for an employee
* Add new employees
* Track departments
* Avoid duplicate department names
* Count how many employees belong to each department

---

# Concepts Used

Students must use:

* Lists
* Dictionaries
* Tuples
* Sets
* Loops
* `if/elif/else`
* `input()`
* f-strings
* Basic collection methods

---

# Data Structure Design

Each employee should be stored as a dictionary.

Example:

```python
employee = {
    "id": "EMP001",
    "name": "Adewale",
    "department": "Technology",
    "role": "Python Developer",
    "score": 92
}
```

Multiple employees should be stored inside a list.

```python
employees = [
    {
        "id": "EMP001",
        "name": "Adewale",
        "department": "Technology",
        "role": "Python Developer",
        "score": 92
    },
    {
        "id": "EMP002",
        "name": "Mary",
        "department": "HR",
        "role": "HR Officer",
        "score": 85
    }
]
```

---

# Functional Requirements

The system should allow users to:

1. Add an employee
2. View all employees
3. Search employee by ID
4. View all departments
5. Count employees by department
6. Exit the program

---

# Sample Menu

```text
========================================
       EDUTECH EMPLOYEE DIRECTORY
========================================

1. Add Employee
2. View All Employees
3. Search Employee by ID
4. View Departments
5. Count Employees by Department
6. Exit

Choose an option:
```

---

# Sample Output: View All Employees

```text
========================================
           ALL EMPLOYEES
========================================

ID: EMP001
Name: Adewale
Department: Technology
Role: Python Developer
Score: 92

ID: EMP002
Name: Mary
Department: HR
Role: HR Officer
Score: 85
```

---

# Sample Output: Search Employee

```text
Enter Employee ID: EMP001

Employee Found!

ID: EMP001
Name: Adewale
Department: Technology
Role: Python Developer
Score: 92
```

---

# Student Task

Create a file named:

```text
employee_directory.py
```

Build the Employee Directory System from scratch.

---

# Project Rules

Your program must:

* Use a list to store employees
* Use dictionaries to represent employees
* Use a set to store unique departments
* Use loops to display records
* Use `if/elif/else` for menu choices
* Use `break` to exit the program

---

# Helpful Hints

## Hint 1: Start with an Empty List

```python
employees = []
```

---

## Hint 2: Store One Employee as a Dictionary

```python
employee = {
    "id": employee_id,
    "name": name,
    "department": department,
    "role": role,
    "score": score
}
```

---

## Hint 3: Add Employee to List

```python
employees.append(employee)
```

---

## Hint 4: Search Employee

```python
for employee in employees:
    if employee["id"] == search_id:
        print("Employee Found")
```

---

## Hint 5: Use a Set for Departments

```python
departments = set()
departments.add(employee["department"])
```

---

# Project Checklist

Before viewing the solution, check:

☐ Did I use a list?

☐ Did I use dictionaries?

☐ Did I use a set?

☐ Did I use loops?

☐ Did I create a menu?

☐ Did I add employees successfully?

☐ Did I search employees successfully?

☐ Did I count employees by department?

☐ Did I exit the program correctly?

---

# Instructor Solution

```python
employees = []

print("========================================")
print("       EDUTECH EMPLOYEE DIRECTORY")
print("========================================")

while True:
    print("\n1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee by ID")
    print("4. View Departments")
    print("5. Count Employees by Department")
    print("6. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        role = input("Enter Role: ")
        score = int(input("Enter Performance Score: "))

        employee = {
            "id": employee_id,
            "name": name,
            "department": department,
            "role": role,
            "score": score
        }

        employees.append(employee)

        print("\nEmployee added successfully!")

    elif choice == "2":
        print("\n========================================")
        print("           ALL EMPLOYEES")
        print("========================================")

        if len(employees) == 0:
            print("No employee records available.")
        else:
            for employee in employees:
                print(f"\nID: {employee['id']}")
                print(f"Name: {employee['name']}")
                print(f"Department: {employee['department']}")
                print(f"Role: {employee['role']}")
                print(f"Score: {employee['score']}")

    elif choice == "3":
        search_id = input("Enter Employee ID: ")

        found = False

        for employee in employees:
            if employee["id"] == search_id:
                print("\nEmployee Found!")
                print(f"ID: {employee['id']}")
                print(f"Name: {employee['name']}")
                print(f"Department: {employee['department']}")
                print(f"Role: {employee['role']}")
                print(f"Score: {employee['score']}")

                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == "4":
        departments = set()

        for employee in employees:
            departments.add(employee["department"])

        print("\nDepartments:")

        if len(departments) == 0:
            print("No departments available.")
        else:
            for department in departments:
                print(f"- {department}")

    elif choice == "5":
        department_count = {}

        for employee in employees:
            department = employee["department"]

            department_count[department] = department_count.get(department, 0) + 1

        print("\nEmployee Count by Department:")

        if len(department_count) == 0:
            print("No employee records available.")
        else:
            for department, count in department_count.items():
                print(f"{department}: {count}")

    elif choice == "6":
        print("Exiting Employee Directory System.")
        break

    else:
        print("Invalid option. Please choose between 1 and 6.")
```

---

# Code Walkthrough

## Step 1: Create an Empty List

```python
employees = []
```

This list will store all employee records.

---

## Step 2: Use a Menu

```python
while True:
```

The menu keeps showing until the user chooses to exit.

---

## Step 3: Store Employee as Dictionary

```python
employee = {
    "id": employee_id,
    "name": name,
    "department": department,
    "role": role,
    "score": score
}
```

Each employee is represented as a dictionary because employee data has labels.

---

## Step 4: Add Employee to List

```python
employees.append(employee)
```

This saves the employee record inside the employee list.

---

## Step 5: Search with a Loop

```python
for employee in employees:
    if employee["id"] == search_id:
```

The program checks each employee until it finds a matching ID.

---

## Step 6: Use a Set for Departments

```python
departments = set()
```

A set prevents duplicate department names.

---

## Step 7: Count Employees by Department

```python
department_count[department] = department_count.get(department, 0) + 1
```

This creates a frequency counter using dictionaries.

---

# Professional Upgrade Challenge

Improve the system by adding:

* Delete employee
* Update employee role
* Update employee performance score
* Show best-performing employee
* Show employees with score above 80
* Prevent duplicate employee IDs

---

# Super Challenge

Add a performance grade to each employee.

Rules:

| Score    | Grade     |
| -------- | --------- |
| 90–100   | Excellent |
| 70–89    | Very Good |
| 50–69    | Good      |
| 40–49    | Fair      |
| Below 40 | Poor      |

Display the grade when viewing employees.

---

# Super Challenge Hint

```python
if score >= 90:
    grade = "Excellent"
elif score >= 70:
    grade = "Very Good"
elif score >= 50:
    grade = "Good"
elif score >= 40:
    grade = "Fair"
else:
    grade = "Poor"
```

Add the grade to the employee dictionary.

---

# Real-World Connection

This project is similar to systems used in:

* HR departments
* Staff management systems
* School management systems
* Hospital staff directories
* Company admin dashboards
* ERP systems

The main difference is that professional systems store data in databases.

For now, students are using lists and dictionaries as an in-memory database.

---

# Portfolio Section

## Project Name

Employee Directory System

---

## What I Built

A Python console-based employee directory system that stores multiple employee records using lists and dictionaries, supports searching, displays unique departments using sets, and counts employees by department.

---

## Skills Demonstrated

* Lists
* Dictionaries
* Sets
* Loops
* Conditional statements
* Menu-driven programs
* Searching records
* Frequency counting
* Basic data modeling

---

## Resume Description

Developed a Python-based Employee Directory System that manages multiple employee records using lists, dictionaries, and sets. The system supports adding employees, viewing records, searching by ID, listing departments, and counting employees by department.

---

## GitHub Repository Name

```text
employee-directory-system
```

---

# What Students Have Achieved

After completing this project, students have:

* Built a collection-based business application
* Used lists to store multiple records
* Used dictionaries to represent real-world objects
* Used sets to prevent duplicate departments
* Built a searchable employee directory
* Added Project #4 to their HR Management System journey

---

