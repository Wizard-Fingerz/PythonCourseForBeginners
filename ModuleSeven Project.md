# Module 7 Project

## Project 007 — Employee Management System

### Difficulty Level

🟡 Intermediate

---

# Project Story

## EduTech Africa Ltd — OOP Refactor

Congratulations!

Your Employee Records Database is now working.

Employees can be:

* Added
* Viewed
* Updated
* Deleted

Data is stored permanently using JSON.

However, the software engineering team has identified a problem.

Currently, employee records look like this:

```python
employee = {
    "id": "EMP001",
    "name": "Adewale",
    "department": "Technology",
    "salary": 200000
}
```

As the company grows, managing employees as dictionaries becomes difficult.

The engineering team wants the system rebuilt using Object-Oriented Programming.

Your task is to create a professional Employee Management System using Classes and Objects.

---

# Business Requirement

The company wants:

✓ Employee objects

✓ Manager objects

✓ Intern objects

✓ Salary calculations

✓ Performance tracking

✓ Encapsulation of sensitive data

✓ Reusable OOP design

---

# Learning Objectives

Students should learn:

* Classes
* Objects
* Constructors
* Methods
* Attributes
* Encapsulation
* Properties
* Inheritance
* Polymorphism

---

# System Design

Instead of:

```python
employee = {
    "name": "John"
}
```

We now create:

```python
employee = Employee(
    "EMP001",
    "John",
    "Technology",
    200000
)
```

---

# Class Structure

## Employee

```text
Employee
│
├── ID
├── Name
├── Department
├── Salary
└── Methods
```

---

## Manager

```text
Manager
│
└── Employee
```

Manager inherits from Employee.

---

## Intern

```text
Intern
│
└── Employee
```

Intern inherits from Employee.

---

# Functional Requirements

The system should:

### Create Employee

```python
employee = Employee(...)
```

---

### View Employee Information

```python
employee.display_info()
```

---

### Calculate Annual Salary

```python
employee.annual_salary()
```

---

### Create Managers

```python
manager = Manager(...)
```

---

### Create Interns

```python
intern = Intern(...)
```

---

### Demonstrate Inheritance

Managers and Interns should inherit Employee features.

---

# Student Task

Create:

```text
employee_management_system.py
```

Build the entire system using classes.

---

# Project Rules

You must:

✅ Create at least 3 classes

✅ Use constructors

✅ Use instance attributes

✅ Use methods

✅ Use inheritance

✅ Use encapsulation

---

# Class Diagram

```text
Employee
│
├── Manager
│
└── Intern
```

---

# Helpful Hints

## Hint 1

Create a class.

```python
class Employee:
    pass
```

---

## Hint 2

Use a constructor.

```python
def __init__(
    self,
    name
):
    self.name = name
```

---

## Hint 3

Create methods.

```python
def display_info(self):
    pass
```

---

# Project Checklist

Before viewing the solution:

☐ Did I create classes?

☑ Did I create objects?

☑ Did I use constructors?

☑ Did I use methods?

☑ Did I use inheritance?

☑ Did I demonstrate OOP concepts?

---

# Instructor Solution

## Employee Class

```python
class Employee:

    company = "EduTech Africa Ltd"

    def __init__(
        self,
        employee_id,
        name,
        department,
        salary
    ):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self._salary = salary

    def display_info(self):

        print("\nEmployee Information")
        print("--------------------")
        print(f"ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: ₦{self._salary}")

    def annual_salary(self):

        return self._salary * 12
```

---

# Manager Class

```python
class Manager(Employee):

    def __init__(
        self,
        employee_id,
        name,
        department,
        salary,
        team_size
    ):

        super().__init__(
            employee_id,
            name,
            department,
            salary
        )

        self.team_size = team_size

    def display_info(self):

        super().display_info()

        print(
            f"Team Size: {self.team_size}"
        )
```

---

# Intern Class

```python
class Intern(Employee):

    def __init__(
        self,
        employee_id,
        name,
        department,
        salary,
        duration
    ):

        super().__init__(
            employee_id,
            name,
            department,
            salary
        )

        self.duration = duration

    def display_info(self):

        super().display_info()

        print(
            f"Duration: {self.duration} Months"
        )
```

---

# Creating Objects

```python
manager = Manager(
    "EMP001",
    "Adewale",
    "Technology",
    500000,
    10
)

intern = Intern(
    "EMP002",
    "Mary",
    "Technology",
    50000,
    6
)
```

---

# Using Objects

```python
manager.display_info()

intern.display_info()
```

---

# Expected Output

```text
Employee Information
--------------------
ID: EMP001
Name: Adewale
Department: Technology
Salary: ₦500000
Team Size: 10

Employee Information
--------------------
ID: EMP002
Name: Mary
Department: Technology
Salary: ₦50000
Duration: 6 Months
```

---

# Encapsulation Challenge

Protect salary using a property.

```python
@property
def salary(self):
    return self._salary
```

---

# Setter Challenge

Prevent negative salaries.

```python
@salary.setter
def salary(
    self,
    value
):

    if value >= 0:
        self._salary = value
```

---

# Professional Upgrade Challenge

Create:

```python
class Department:
```

Requirements:

* Department Name
* List of Employees
* Add Employee Method

This demonstrates Composition.

---

# Example

```python
technology = Department(
    "Technology"
)

technology.add_employee(
    manager
)
```

---

# Super Challenge

Create:

```python
class PayrollSystem:
```

Methods:

```python
calculate_bonus()

calculate_payroll()

generate_report()
```

This prepares students for Module 8.

---

# Polymorphism Challenge

Create:

```python
employees = [
    manager,
    intern
]
```

Loop through:

```python
for employee in employees:
    employee.display_info()
```

Each object behaves differently.

This demonstrates Polymorphism.

---

# Real-World Connection

This project mirrors how professional applications are built.

Examples:

* HR Systems
* Banking Applications
* Hospital Systems
* School Management Systems
* ERP Platforms

Most enterprise applications are object-oriented.

Django itself is built around classes and objects.

---

# Portfolio Section

## Project Name

Employee Management System

---

## What I Built

A Python-based Employee Management System that models employees, managers, and interns using Object-Oriented Programming principles including inheritance, encapsulation, methods, properties, and polymorphism.

---

## Skills Demonstrated

* OOP
* Classes
* Objects
* Constructors
* Methods
* Encapsulation
* Properties
* Inheritance
* Polymorphism
* Composition

---

## Resume Description

Developed an Object-Oriented Employee Management System using Python classes, inheritance, encapsulation, and polymorphism to model real-world employee relationships and payroll functionality.

---

## GitHub Repository Name

```text
employee-management-system
```

---

# What Students Have Achieved

After completing this project, students have:

✅ Built their first fully object-oriented application

✅ Created reusable classes

✅ Used inheritance professionally

✅ Applied encapsulation

✅ Implemented polymorphism

✅ Built Project #7 in the HR Management System journey

---
