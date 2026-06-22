# Module 3 Project

## Project 003 — Employee Performance Evaluation System

### Difficulty Level

🟢 Beginner

---

# Project Story

## EduTech Africa Ltd — HR Performance Review

In Module 2, you built an **Employee Information System** that collects employee details and calculates salary.

Now, EduTech Africa Ltd wants to improve its HR system.

The HR department wants a program that can evaluate employee performance based on a performance score.

Your task is to build a Python program that:

* Accepts employee information
* Accepts performance score
* Determines performance grade
* Gives a recommendation
* Allows multiple employee evaluations

---

# Business Requirement

The HR department wants a system that evaluates employees using this grading structure:

| Score    | Grade     | Remark                    |
| -------- | --------- | ------------------------- |
| 90–100   | Excellent | Eligible for promotion    |
| 70–89    | Very Good | Eligible for bonus        |
| 50–69    | Good      | Needs improvement plan    |
| 40–49    | Fair      | Requires training         |
| Below 40 | Poor      | Performance review needed |

---

# Functional Requirements

The program should:

1. Ask for employee name.
2. Ask for department.
3. Ask for performance score.
4. Determine the employee’s grade.
5. Display the employee’s result.
6. Allow the user to evaluate more than one employee.
7. Stop when the user types `quit`.

---

# Concepts Used

Students must use:

* `input()`
* Variables
* Type conversion
* `if`
* `elif`
* `else`
* Logical operators
* `while` loop
* `break`
* f-strings

---

# Sample Run

```text
Enter employee name or type quit to stop: Adewale
Enter department: Technology
Enter performance score: 92

====================================
EMPLOYEE PERFORMANCE REPORT
====================================
Name: Adewale
Department: Technology
Score: 92
Grade: Excellent
Remark: Eligible for promotion
====================================

Enter employee name or type quit to stop: Mary
Enter department: HR
Enter performance score: 75

====================================
EMPLOYEE PERFORMANCE REPORT
====================================
Name: Mary
Department: HR
Score: 75
Grade: Very Good
Remark: Eligible for bonus
====================================

Enter employee name or type quit to stop: quit
Program ended.
```

---

# Student Task

Create a file named:

```text
employee_performance_evaluator.py
```

Build the program from scratch.

---

# Project Rules

Your program must:

* Use a `while` loop
* Use `if-elif-else`
* Use `break` to stop the program
* Use score ranges correctly
* Display a clean report

---

# Helpful Hints

## Hint 1

Use a loop to keep the program running.

```python
while True:
    # code goes here
```

---

## Hint 2

Use `break` to stop the loop.

```python
if employee_name == "quit":
    break
```

---

## Hint 3

Convert score to integer.

```python
score = int(input("Enter performance score: "))
```

---

## Hint 4

Use conditions to determine grade.

```python
if score >= 90:
    grade = "Excellent"
```

---

# Project Checklist

Before viewing the solution, check:

☐ Did I use a while loop?

☐ Did I allow multiple employee evaluations?

☐ Did I use if-elif-else?

☐ Did I use score ranges correctly?

☐ Did I use break to stop the program?

☐ Did I display a professional report?

☐ Did I test different scores?

---

# Instructor Solution

```python
print("====================================")
print("EDUTECH AFRICA PERFORMANCE SYSTEM")
print("====================================")

while True:
    employee_name = input("\nEnter employee name or type quit to stop: ")

    if employee_name.lower() == "quit":
        print("Program ended.")
        break

    department = input("Enter department: ")

    score = int(input("Enter performance score: "))

    if score >= 90 and score <= 100:
        grade = "Excellent"
        remark = "Eligible for promotion"

    elif score >= 70 and score <= 89:
        grade = "Very Good"
        remark = "Eligible for bonus"

    elif score >= 50 and score <= 69:
        grade = "Good"
        remark = "Needs improvement plan"

    elif score >= 40 and score <= 49:
        grade = "Fair"
        remark = "Requires training"

    elif score >= 0 and score < 40:
        grade = "Poor"
        remark = "Performance review needed"

    else:
        grade = "Invalid Score"
        remark = "Score must be between 0 and 100"

    print("\n====================================")
    print("EMPLOYEE PERFORMANCE REPORT")
    print("====================================")
    print(f"Name: {employee_name}")
    print(f"Department: {department}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")
    print(f"Remark: {remark}")
    print("====================================")
```

---

# Code Walkthrough

## Step 1: Display Program Title

```python
print("EDUTECH AFRICA PERFORMANCE SYSTEM")
```

This tells the user what the program does.

---

## Step 2: Keep Program Running

```python
while True:
```

This keeps the program running until we manually stop it.

---

## Step 3: Stop the Program

```python
if employee_name.lower() == "quit":
    break
```

This allows the user to exit the program by typing `quit`.

`.lower()` helps because the user may type:

```text
QUIT
Quit
quit
```

All will still work.

---

## Step 4: Convert Score

```python
score = int(input("Enter performance score: "))
```

`input()` returns text, so we use `int()` to convert the score to a number.

---

## Step 5: Make Decisions

```python
if score >= 90 and score <= 100:
```

This checks whether the score is between 90 and 100.

---

# Professional Upgrade Challenge

Improve the system by adding:

* Employee ID
* Years of experience
* Attendance percentage
* Punctuality score

Then decide promotion eligibility using multiple conditions.

Example:

```text
Promotion Eligibility:
Employee must have:
- Performance score 90 or above
- Attendance 80% or above
- At least 2 years experience
```

---

# Super Challenge

Add this rule:

If the employee has a score below 0 or above 100, display:

```text
Invalid score. Please enter a score between 0 and 100.
```

Then use `continue` to skip the rest of that evaluation.

---

# Super Challenge Solution Idea

```python
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
    continue
```

---

# Real-World Connection

This project is similar to systems used in:

* HR departments
* Employee appraisal systems
* School grading systems
* Staff promotion systems
* Performance management platforms

The same logic can be reused for students, workers, sales agents, or loan applicants.

---

# Portfolio Section

## Project Name

Employee Performance Evaluation System

---

## What I Built

A Python console application that evaluates employee performance scores, assigns grades, gives HR recommendations, and supports multiple employee evaluations using loops.

---

## Skills Demonstrated

* Conditional statements
* Logical operators
* Loops
* Break statement
* Type conversion
* User input
* f-string formatting
* Basic business logic

---

## Resume Description

Developed a Python-based Employee Performance Evaluation System that uses conditional logic and loops to evaluate staff performance, assign grades, generate HR recommendations, and process multiple employee records interactively.

---

## GitHub Repository Name

```text
employee-performance-evaluation-system
```

---

# What Students Have Achieved

After completing this project, students have:

* Built a decision-making Python application
* Used conditions to solve a business problem
* Used loops to process multiple records
* Built Project #3 in their HR Management System journey

---
