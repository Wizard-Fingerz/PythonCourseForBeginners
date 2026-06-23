# Module 9 Project

## Project 009 — HR Management Package

### Difficulty Level

🟡 Intermediate

---

# Project Story

## EduTech Africa Ltd — Software Product Initiative

Over the past modules, you have built:

* Employee Information System
* Employee Performance System
* Employee Directory System
* HR Utility Toolkit
* Employee Records Database
* Employee Management System
* Enterprise Payroll System

The company is impressed.

However, there is a new problem.

Different departments need to use the HR system.

Instead of copying and pasting files between projects, management wants the HR system converted into a reusable Python package.

Your task is to package the entire HR system into a professional Python package.

---

# Business Requirement

The HR department wants:

✅ Employee Management Tools

✅ Payroll Functions

✅ Database Functions

✅ Report Functions

All accessible through a single package.

---

# Learning Objectives

Students should learn:

* Modules
* Packages
* Imports
* Project Structure
* Virtual Environments
* Requirements Files
* Professional Code Organization

---

# Final Package Name

```text
hr_tools
```

---

# Package Structure

```text
hr_tools/

│
├── hr_tools/
│   │
│   ├── __init__.py
│   ├── employees.py
│   ├── payroll.py
│   ├── database.py
│   ├── reports.py
│
├── README.md
├── requirements.txt
└── main.py
```

---

# Functional Requirements

The package should provide:

### Employee Functions

```python
add_employee()

search_employee()

view_employees()
```

---

### Payroll Functions

```python
calculate_salary()

calculate_bonus()

calculate_annual_salary()
```

---

### Database Functions

```python
save_data()

load_data()
```

---

### Reporting Functions

```python
generate_employee_report()

department_summary()
```

---

# Sample Usage

A developer should be able to write:

```python
from hr_tools.payroll import calculate_bonus

bonus = calculate_bonus("Excellent")

print(bonus)
```

Output:

```text
50000
```

---

# Student Task

Create:

```text
hr_tools
```

as a Python package.

Move all related functionality into separate modules.

---

# Project Rules

You must:

✅ Create a package folder

✅ Create **init**.py

✅ Create multiple modules

✅ Import functions between modules

✅ Use a virtual environment

✅ Create requirements.txt

---

# Step 1 — Create Package Structure

Create:

```text
hr_tools/
```

Inside:

```text
employees.py
payroll.py
database.py
reports.py
```

---

# Step 2 — Employee Module

Create:

```python
# employees.py

employees = []

def add_employee(employee):
    employees.append(employee)

def view_employees():
    return employees
```

---

# Step 3 — Payroll Module

Create:

```python
# payroll.py

def calculate_bonus(grade):

    if grade == "Excellent":
        return 50000

    elif grade == "Very Good":
        return 25000

    return 0
```

---

# Step 4 — Database Module

Create:

```python
# database.py

import json

def save_data(data):

    with open(
        "employees.json",
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )
```

---

# Step 5 — Reports Module

Create:

```python
# reports.py

def department_summary(employees):

    result = {}

    for employee in employees:

        department = employee["department"]

        result[department] = (
            result.get(
                department,
                0
            ) + 1
        )

    return result
```

---

# Step 6 — Main Application

Create:

```python
# main.py

from hr_tools.payroll import (
    calculate_bonus
)

print(
    calculate_bonus(
        "Excellent"
    )
)
```

---

# Expected Output

```text
50000
```

---

# Project Checklist

Before viewing the solution:

☐ Did I create a package?

☐ Did I create **init**.py?

☐ Did I create modules?

☐ Did I import functions correctly?

☐ Did I separate concerns?

☐ Did I use a virtual environment?

☐ Did I create requirements.txt?

---

# Virtual Environment Task

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

# Requirements File

Generate:

```bash
pip freeze > requirements.txt
```

Example:

```text
Django==5.2.1
requests==2.32.0
```

---

# Instructor Solution

## **init**.py

```python
from .employees import *
from .payroll import *
from .database import *
from .reports import *
```

---

# Professional Upgrade Challenge

Create:

```python
generate_employee_email()
```

inside:

```text
employees.py
```

Example:

```python
generate_employee_email(
    "Adewale Oladiti"
)
```

Output:

```text
adewale.oladiti@edutechafrica.com
```

---

# Super Challenge

Convert:

```text
employees.json
```

into:

```text
employees.csv
```

and create:

```python
export_to_csv()
```

inside:

```text
reports.py
```

---

# Expert Challenge

Create:

```python
backup_database()
```

Function.

Requirements:

* Create timestamp backup
* Save JSON copy
* Prevent data loss

Example:

```text
backup_2026_06_23.json
```

---

# Real-World Connection

This project mirrors how professional software is organized.

Instead of:

```text
one_file.py
```

real applications use:

```text
modules
packages
components
```

Large companies separate functionality into packages to make software:

* Maintainable
* Reusable
* Scalable

---

# Portfolio Section

## Project Name

HR Management Package

---

## What I Built

A modular Python package that organizes employee management, payroll processing, reporting, and database functionality into reusable modules.

---

## Skills Demonstrated

* Python Packages
* Modules
* Imports
* Virtual Environments
* Requirements Files
* Code Organization
* Software Architecture

---

## Resume Description

Developed a reusable HR Management Python package that modularizes employee management, payroll processing, reporting, and data persistence functionality using industry-standard package structures and dependency management practices.

---

## GitHub Repository Name

```text
hr-management-package
```

---

# What Students Have Achieved

After completing this project, students have:

✅ Built a professional Python package

✅ Organized code into modules

✅ Learned dependency management

✅ Used virtual environments

✅ Applied software architecture principles

✅ Built Project #9 in the HR Management System journey

---

