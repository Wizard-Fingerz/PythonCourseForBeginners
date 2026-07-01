# Module 8 Project

## Project 008 — Enterprise Payroll System

### Difficulty Level

🟠 Intermediate to Advanced

---

# Project Story

## EduTech Africa Ltd — Enterprise Payroll Upgrade

In Module 7, you rebuilt the HR system using Object-Oriented Programming.

The system now has:

* Employee objects
* Manager objects
* Intern objects
* Basic salary calculations
* Inheritance
* Encapsulation
* Polymorphism

Now EduTech Africa Ltd wants to upgrade the system into a more professional payroll engine.

The company now has different employee types, and each employee type is paid differently.

Your task is to build an:

```text
Enterprise Payroll System
```

using Advanced Object-Oriented Programming.

---

# Business Requirement

The HR and Finance departments want a payroll system that can:

* Calculate salary for different employee types
* Enforce a standard salary calculation structure
* Display employee payroll reports
* Compare employees
* Add payroll amounts together
* Support flexible employee types

---

# Learning Objectives

Students should learn how to apply:

* Advanced inheritance
* Abstract classes
* Polymorphism
* Interfaces
* Magic methods
* Operator overloading
* Professional OOP design

---

# System Design

The system should have a parent abstract class:

```text
Employee
```

and child classes:

```text
Manager
Developer
Intern
ContractStaff
```

Each employee type should calculate salary differently.

---

# Class Structure

```text
Employee (Abstract Class)
│
├── Manager
├── Developer
├── Intern
└── ContractStaff
```

---

# Payroll Rules

| Employee Type  | Salary Rule                           |
| -------------- | ------------------------------------- |
| Manager        | Base salary + ₦100,000 allowance      |
| Developer      | Base salary + ₦50,000 technical bonus |
| Intern         | Fixed monthly stipend                 |
| Contract Staff | Hourly rate × hours worked            |

---

# Functional Requirements

The system should:

1. Create different employee types.
2. Calculate payroll for each employee.
3. Use abstract classes to enforce `calculate_salary()`.
4. Use polymorphism to process all employees together.
5. Use `__str__()` to display employee details neatly.
6. Use `__add__()` to combine payroll amounts.
7. Use `__len__()` to count employees in a payroll batch.
8. Generate a payroll summary.

---

# Concepts Used

Students must use:

* `ABC`
* `abstractmethod`
* Inheritance
* Method overriding
* Polymorphism
* Dunder methods
* Operator overloading
* Lists of objects

---

# Student Task

Create a file named:

```text
enterprise_payroll_system.py
```

Build the payroll system using advanced OOP concepts.

---

# Project Rules

Your program must:

* Use an abstract class
* Create at least 4 subclasses
* Override `calculate_salary()`
* Use polymorphism
* Use at least 2 dunder methods
* Use operator overloading

---

# Helpful Hints

## Hint 1 — Abstract Class

```python
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass
```

---

## Hint 2 — Method Overriding

```python
class Manager(Employee):

    def calculate_salary(self):
        return self.base_salary + 100000
```

---

## Hint 3 — Polymorphism

```python
for employee in employees:
    print(employee.calculate_salary())
```

---

## Hint 4 — `__str__()`

```python
def __str__(self):
    return f"{self.name} - {self.role}"
```

---

## Hint 5 — Operator Overloading

```python
def __add__(self, other):
    return self.calculate_salary() + other.calculate_salary()
```

---

# Project Checklist

Before viewing the solution:

☐ Did I create an abstract class?

☐ Did I use `@abstractmethod`?

☐ Did I create subclasses?

☐ Did I override methods?

☐ Did I use polymorphism?

☐ Did I use `__str__()`?

☐ Did I use `__add__()`?

☐ Did I generate a payroll report?

---

# Instructor Solution

```python
from abc import ABC, abstractmethod


class Employee(ABC):

    company = "EduTech Africa Ltd"

    def __init__(self, employee_id, name, department):
        self.employee_id = employee_id
        self.name = name
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return f"{self.employee_id} - {self.name} ({self.department})"

    def __add__(self, other):
        return self.calculate_salary() + other.calculate_salary()


class Manager(Employee):

    def __init__(self, employee_id, name, department, base_salary):
        super().__init__(employee_id, name, department)
        self.base_salary = base_salary
        self.allowance = 100000

    def calculate_salary(self):
        return self.base_salary + self.allowance


class Developer(Employee):

    def __init__(self, employee_id, name, department, base_salary):
        super().__init__(employee_id, name, department)
        self.base_salary = base_salary
        self.technical_bonus = 50000

    def calculate_salary(self):
        return self.base_salary + self.technical_bonus


class Intern(Employee):

    def __init__(self, employee_id, name, department, stipend):
        super().__init__(employee_id, name, department)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


class ContractStaff(Employee):

    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        super().__init__(employee_id, name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class PayrollBatch:

    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def __len__(self):
        return len(self.employees)

    def generate_report(self):
        print("\n======================================")
        print("        PAYROLL SUMMARY REPORT")
        print("======================================")

        total_payroll = 0

        for employee in self.employees:
            salary = employee.calculate_salary()
            total_payroll += salary

            print(f"\nEmployee: {employee}")
            print(f"Salary: ₦{salary:,.2f}")

        print("\n======================================")
        print(f"Total Employees: {len(self)}")
        print(f"Total Payroll: ₦{total_payroll:,.2f}")
        print("======================================")


manager = Manager(
    "EMP001",
    "Adewale Oladiti",
    "Technology",
    500000
)

developer = Developer(
    "EMP002",
    "Mary Johnson",
    "Engineering",
    350000
)

intern = Intern(
    "EMP003",
    "Tolu Adebayo",
    "Technology",
    80000
)

contract_staff = ContractStaff(
    "EMP004",
    "Grace Bello",
    "Operations",
    5000,
    40
)

payroll = PayrollBatch()

payroll.add_employee(manager)
payroll.add_employee(developer)
payroll.add_employee(intern)
payroll.add_employee(contract_staff)

payroll.generate_report()

combined_salary = manager + developer

print(f"\nCombined Manager + Developer Salary: ₦{combined_salary:,.2f}")
```

---

# Expected Output

```text
======================================
        PAYROLL SUMMARY REPORT
======================================

Employee: EMP001 - Adewale Oladiti (Technology)
Salary: ₦600,000.00

Employee: EMP002 - Mary Johnson (Engineering)
Salary: ₦400,000.00

Employee: EMP003 - Tolu Adebayo (Technology)
Salary: ₦80,000.00

Employee: EMP004 - Grace Bello (Operations)
Salary: ₦200,000.00

======================================
Total Employees: 4
Total Payroll: ₦1,280,000.00
======================================

Combined Manager + Developer Salary: ₦1,000,000.00
```

---

# Code Walkthrough

## Step 1 — Abstract Employee Class

```python
class Employee(ABC):
```

This class defines the common structure for all employees.

---

## Step 2 — Abstract Method

```python
@abstractmethod
def calculate_salary(self):
    pass
```

This forces every employee type to implement its own salary calculation.

---

## Step 3 — Subclasses

```python
class Manager(Employee):
```

Each subclass inherits from Employee.

---

## Step 4 — Method Overriding

```python
def calculate_salary(self):
```

Each subclass defines its own version of salary calculation.

---

## Step 5 — Polymorphism

```python
for employee in self.employees:
    salary = employee.calculate_salary()
```

Different employee types use the same method name but produce different results.

---

## Step 6 — `__str__()`

```python
def __str__(self):
```

This controls how employee objects are displayed.

---

## Step 7 — `__add__()`

```python
def __add__(self, other):
```

This allows two employee payroll values to be added using `+`.

---

## Step 8 — `__len__()`

```python
def __len__(self):
```

This allows the payroll batch to be counted using `len()`.

---

# Professional Upgrade Challenge

Add tax calculation.

Rules:

| Salary Range       | Tax Rate |
| ------------------ | -------- |
| Below ₦100,000     | 0%       |
| ₦100,000–₦299,999  | 5%       |
| ₦300,000–₦599,999  | 10%      |
| ₦600,000 and above | 15%      |

Display:

```text
Gross Salary
Tax
Net Salary
```

---

# Super Challenge

Add a new employee type:

```python
class SalesRepresentative(Employee):
```

Salary rule:

```text
Base Salary + Commission
```

---

# Expert Challenge

Create an interface-like abstract class:

```python
class Payable(ABC):
```

Required method:

```python
process_payment()
```

Make all employee types implement it.

---

# Real-World Connection

This project is similar to payroll engines used in:

* HR software
* Accounting platforms
* ERP systems
* Banking systems
* Government salary systems
* Business management software

Different workers are paid differently, so payroll systems need polymorphism, inheritance, and clean object-oriented design.

---

# Portfolio Section

## Project Name

Enterprise Payroll System

---

## What I Built

A Python-based enterprise payroll system that uses abstract classes, inheritance, polymorphism, magic methods, and operator overloading to calculate salaries for different employee types and generate payroll reports.

---

## Skills Demonstrated

* Advanced OOP
* Abstract Classes
* Interfaces
* Inheritance
* Polymorphism
* Method Overriding
* Magic Methods
* Operator Overloading
* Payroll Logic
* Enterprise Software Design

---

## Resume Description

Developed an advanced object-oriented Enterprise Payroll System in Python using abstract classes, inheritance, polymorphism, and operator overloading to model multiple employee types, process payroll, and generate salary reports.

---

## GitHub Repository Name

```text
enterprise-payroll-system
```

---

# What Students Have Achieved

After completing this project, students have:

* Built an advanced OOP business system
* Used abstract classes and method overriding
* Applied polymorphism in a realistic payroll scenario
* Implemented magic methods and operator overloading
* Added Project #8 to their HR Management System journey

---

# Next Project

In Module 9, students will convert the HR and payroll logic into a reusable Python package using:

* Modules
* Packages
* Virtual environments
* Requirements files

This will make their project look like a professional software library.
