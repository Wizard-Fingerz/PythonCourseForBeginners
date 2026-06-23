# Module 6 Project

## Project 006 — Employee Records Database

### Difficulty Level

🟡 Intermediate

---

# Project Story

## EduTech Africa Ltd — Data Persistence Upgrade

Congratulations!

The HR department has been using your:

```text id="q7sk2f"
HR Utility Toolkit
```

to manage employees.

Unfortunately, there is a major problem.

Whenever the application closes:

```text id="tm9n6u"
All Employee Records Are Lost
```

The HR department is frustrated because they have to enter employee information every time they reopen the program.

Management has requested a permanent solution.

Your task is to build:

```text id="jhlhsl"
Employee Records Database
```

using JSON files.

---

# Business Requirement

The HR department wants a system that can:

✓ Save employee records

✓ Load employee records automatically

✓ Search employee records

✓ Update employee records

✓ Delete employee records

✓ Persist data even after the application closes

---

# Learning Objectives

Students should learn:

* Reading files
* Writing files
* JSON storage
* Exception handling
* Data persistence
* CRUD operations

---

# What Is Data Persistence?

Without persistence:

```text id="9m9nv0"
Program Closes
       ↓
Data Lost
```

With persistence:

```text id="22m54t"
Program Closes
       ↓
Data Saved
       ↓
Program Opens Again
       ↓
Data Restored
```

---

# Project Goal

Build a JSON-powered employee database.

---

# Employee Structure

Each employee record should look like:

```python id="5wtrzz"
{
    "id": "EMP001",
    "name": "Adewale",
    "department": "Technology",
    "position": "Python Developer",
    "salary": 200000
}
```

---

# Storage File

Create:

```text id="yjk2gs"
employees.json
```

Example:

```json id="zw73j0"
[
    {
        "id": "EMP001",
        "name": "Adewale",
        "department": "Technology",
        "position": "Python Developer",
        "salary": 200000
    }
]
```

---

# Functional Requirements

The system should allow users to:

### 1. Add Employee

Store a new employee.

---

### 2. View Employees

Display all employees.

---

### 3. Search Employee

Search using employee ID.

---

### 4. Update Employee

Modify employee information.

---

### 5. Delete Employee

Remove employee records.

---

### 6. Save Data

Store all records inside JSON.

---

### 7. Load Data

Automatically load data when application starts.

---

# Sample Menu

```text id="lshtlc"
====================================
EMPLOYEE RECORDS DATABASE
====================================

1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit

Choose an option:
```

---

# Student Task

Create:

```text id="hrs5x4"
employee_database.py
```

Build the Employee Records Database.

---

# Project Rules

You must:

✅ Use JSON

✅ Use file handling

✅ Use try/except

✅ Save data automatically

✅ Load data automatically

---

# Helpful Hints

## Hint 1

Import JSON.

```python id="08e7yv"
import json
```

---

## Hint 2

Save data.

```python id="4w6ccn"
with open(
    "employees.json",
    "w"
) as file:

    json.dump(
        employees,
        file,
        indent=4
    )
```

---

## Hint 3

Load data.

```python id="vfe8gr"
with open(
    "employees.json"
) as file:

    employees = json.load(file)
```

---

## Hint 4

Handle missing files.

```python id="h4wr9c"
try:

    with open(
        "employees.json"
    ) as file:

        employees = json.load(file)

except FileNotFoundError:

    employees = []
```

---

# Project Checklist

Before viewing the solution:

☐ Did I use JSON?

☐ Did I use file handling?

☐ Did I use try/except?

☐ Did I save records?

☐ Did I load records?

☐ Did I implement CRUD operations?

☐ Did I test application restart?

---

# Instructor Solution

## Save Function

```python id="2g6ntp"
import json

def save_data(employees):

    with open(
        "employees.json",
        "w"
    ) as file:

        json.dump(
            employees,
            file,
            indent=4
        )
```

---

## Load Function

```python id="awicvj"
def load_data():

    try:

        with open(
            "employees.json"
        ) as file:

            return json.load(file)

    except FileNotFoundError:

        return []
```

---

## Application Startup

```python id="0z5n94"
employees = load_data()
```

---

## Add Employee

```python id="66b8yi"
employee = {
    "id": employee_id,
    "name": name,
    "department": department,
    "position": position,
    "salary": salary
}

employees.append(employee)

save_data(employees)
```

---

# Exception Handling Example

Without exception handling:

```python id="4c4lxy"
salary = int(input())
```

User enters:

```text id="6h3g1s"
abc
```

Program crashes.

---

With exception handling:

```python id="oqyb7o"
try:

    salary = int(input())

except ValueError:

    print(
        "Invalid salary entered."
    )
```

Program continues safely.

---

# Professional Upgrade Challenge

Add:

```python id="94hn5f"
update_employee()
```

Function.

Allow HR to:

* Update Name
* Update Department
* Update Salary

Save changes automatically.

---

# Super Challenge

Create:

```python id="y2n38t"
delete_employee()
```

Function.

Requirements:

* Search by Employee ID
* Confirm deletion
* Save changes

Example:

```text id="4c3r64"
Are you sure? (yes/no)
```

---

# Expert Challenge

Create:

```python id="r5h18s"
backup_database()
```

Function.

Requirements:

Save:

```text id="uqdjl6"
employees_backup.json
```

before every update.

This protects HR records from accidental loss.

---

# CSV Export Challenge

Create:

```python id="uyz6lv"
export_to_csv()
```

Function.

Output:

```text id="nlzhd8"
employees.csv
```

Example:

```csv id="jk5r42"
ID,Name,Department,Salary

EMP001,Adewale,Technology,200000
```

---

# Real-World Connection

This project mirrors systems used in:

* Human Resource Systems
* Hospital Staff Records
* Student Management Systems
* Banking Customer Databases
* Inventory Applications

Every professional application stores information permanently.

This is the first time students are building a system that remembers data.

---

# Portfolio Section

## Project Name

Employee Records Database

---

## What I Built

A JSON-powered employee management database capable of storing, retrieving, updating, deleting, and persisting employee records between application sessions.

---

## Skills Demonstrated

* JSON
* File Handling
* Data Persistence
* CRUD Operations
* Exception Handling
* Python Dictionaries
* Python Lists

---

## Resume Description

Developed a Python-based Employee Records Database using JSON file storage, implementing CRUD operations, automatic data persistence, exception handling, and record management functionality.

---

## GitHub Repository Name

```text id="71fmxs"
employee-records-database
```

---

# What Students Have Achieved

After completing this project, students have:

✅ Built their first persistent application

✅ Created a JSON database

✅ Implemented CRUD operations

✅ Applied exception handling

✅ Used file storage professionally

✅ Built Project #6 in the HR Management System journey

---

