# Module 2 Project

## Project 002 — Employee Information System

### Difficulty Level

🟢 Beginner

### Modules Covered

This project is designed for students who have completed:

* Python Data Types
* Numbers & Arithmetic
* Variables
* Strings
* String Methods
* Input & Output
* Print Formatting
* Type Conversion
* Comments
* Basic Operators



---

# Project Story

## Welcome Back to EduTech Africa Ltd

Congratulations!

You have successfully completed your first project — the Company Welcome Banner.

Your manager was impressed.

Now the HR department has a new request.

Currently, new employee information is recorded manually on paper.

This causes:

* Lost records
* Incorrect information
* Difficult searches
* Poor organization

The HR department wants a simple Python application that captures employee information and displays a professional employee profile.

You have been assigned to build Version 1 of the system.

---

# Business Requirement

The system should collect:

* Employee Name
* Age
* Department
* Position
* Monthly Salary

Then display a professional employee profile.

---

# Functional Requirements

The program must:

✅ Accept user input

✅ Store information in variables

✅ Convert numeric values appropriately

✅ Display a formatted employee profile

✅ Calculate annual salary

✅ Use f-strings for formatting

---

# Expected Skills

Students should demonstrate:

* Variables
* Strings
* Numbers
* Type Conversion
* Arithmetic Operations
* Input/Output
* Print Formatting

---

# Sample Run

### Input

```text
Enter Employee Name: Adewale

Enter Age: 25

Enter Department: Technology

Enter Position: Python Developer

Enter Monthly Salary: 200000
```

### Output

```text
==================================================
             EMPLOYEE PROFILE
==================================================

Name: Adewale

Age: 25

Department: Technology

Position: Python Developer

Monthly Salary: ₦200000.00

Annual Salary: ₦2400000.00

==================================================
```

---

# Student Task

Create a file named:

```text
employee_profile.py
```

Build the application from scratch.

---

# Rules

You must use:

✅ Variables

✅ input()

✅ print()

✅ Arithmetic Operators

✅ f-Strings

✅ Type Conversion

---

# Project Breakdown

### Step 1

Ask for employee name.

Example:

```text
Enter Employee Name:
```

---

### Step 2

Ask for age.

Example:

```text
Enter Age:
```

---

### Step 3

Ask for department.

Example:

```text
Enter Department:
```

---

### Step 4

Ask for position.

Example:

```text
Enter Position:
```

---

### Step 5

Ask for monthly salary.

Example:

```text
Enter Monthly Salary:
```

---

### Step 6

Calculate annual salary.

Formula:

```text
Annual Salary = Monthly Salary × 12
```

---

### Step 7

Display a formatted employee profile.

---

# Helpful Hints

## Hint 1

Use:

```python
name = input("Enter Employee Name: ")
```

---

## Hint 2

Salary must be converted to a number.

Example:

```python
salary = float(input("Enter Salary: "))
```

---

## Hint 3

Calculate annual salary:

```python
annual_salary = salary * 12
```

---

## Hint 4

Use f-strings.

Example:

```python
print(f"Salary: ₦{salary}")
```

---

# Project Checklist

Before viewing the solution, ask yourself:

### Did I?

☐ Use variables?

☐ Use input()?

☐ Use type conversion?

☐ Use arithmetic operators?

☐ Use f-strings?

☐ Calculate annual salary?

☐ Display all employee details?

☐ Format output neatly?

---

# Instructor Solution

```python
print("==================================================")
print("      EDUTECH AFRICA EMPLOYEE SYSTEM")
print("==================================================")

name = input("Enter Employee Name: ")

age = int(input("Enter Age: "))

department = input("Enter Department: ")

position = input("Enter Position: ")

monthly_salary = float(
    input("Enter Monthly Salary: ")
)

annual_salary = monthly_salary * 12

print("\n==================================================")
print("               EMPLOYEE PROFILE")
print("==================================================")

print(f"Name: {name}")

print(f"Age: {age}")

print(f"Department: {department}")

print(f"Position: {position}")

print(f"Monthly Salary: ₦{monthly_salary:.2f}")

print(f"Annual Salary: ₦{annual_salary:.2f}")

print("==================================================")
```

---

# Code Walkthrough

## Why use input()?

To collect information from users.

Example:

```python
name = input("Enter Employee Name: ")
```

---

## Why use int()?

Age should be stored as a number.

```python
age = int(input("Enter Age: "))
```

---

## Why use float()?

Salary may contain decimal values.

```python
monthly_salary = float(
    input("Enter Monthly Salary: ")
)
```

---

## Why multiply by 12?

There are 12 months in a year.

```python
annual_salary = monthly_salary * 12
```

---

## Why use f-strings?

Cleaner formatting.

```python
print(f"Annual Salary: ₦{annual_salary:.2f}")
```

---

# Professional Upgrade Challenge

Add:

### Employee ID

Example:

```text
EMP001
```

---

### Office Location

Example:

```text
Ibadan Office
```

---

### Employment Type

Example:

```text
Full-Time
```

---

### Years of Experience

Example:

```text
3
```

Display all information professionally.

---

# Super Challenge

Calculate:

### Weekly Salary

Formula:

```text
Annual Salary ÷ 52
```

---

### Daily Salary

Formula:

```text
Annual Salary ÷ 365
```

Display:

```text
Weekly Salary: ₦46,153.85

Daily Salary: ₦6,575.34
```

---

# Expert Challenge

Add a company email generator.

If the employee name is:

```text
Adewale Oladiti
```

Generate:

```text
adewale.oladiti@edutechafrica.com
```

(Hint: Use string methods.)

---

# Real-World Connection

This project introduces concepts used in:

* HR Systems
* Payroll Applications
* Employee Management Software
* Staff Databases
* Enterprise ERP Systems

Many professional systems begin by collecting and processing employee information.

---

# Portfolio Section

## Project Name

Employee Information System

---

## What I Built

A Python application that collects employee information, calculates annual salary, and generates a professional employee profile.

---

## Skills Demonstrated

* Variables
* Strings
* Input Handling
* Type Conversion
* Arithmetic Operations
* Output Formatting
* Basic Business Logic

---

## Resume Description

> Developed a Python-based Employee Information System that captures employee records, performs salary calculations, and generates formatted employee profiles using user input, variables, arithmetic operations, and string formatting.

---

## GitHub Repository Name

```text
employee-information-system
```

---

## Suggested README Description

A beginner-friendly HR application built with Python that captures employee details, calculates annual salary, and displays a professional employee profile.

---

# What Students Have Achieved

After completing this project, students have:

✅ Used variables in a real application

✅ Worked with strings and numbers

✅ Practiced type conversion

✅ Performed calculations

✅ Used formatted output

✅ Built their first interactive business application

✅ Added Project #2 to their portfolio

---

