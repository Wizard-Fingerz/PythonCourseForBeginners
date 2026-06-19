# Module 9 Assessment

## Modules, Packages & Virtual Environments

### Instructions

* Answer all questions.
* Read all questions carefully.
* Some questions may have more than one correct answer.
* Attempt all practical questions.
* Total Marks: 100
* Duration: 90 Minutes

---

# Learning Objectives Assessment

By the end of this assessment, students should be able to:

✓ Create and use Python modules

✓ Import modules and functions correctly

✓ Create Python packages

✓ Install packages using pip

✓ Understand package management

✓ Create and manage virtual environments

✓ Generate and use requirements files

✓ Build reusable Python packages

✓ Understand package publishing concepts

✓ Apply professional project organization practices

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (20 Marks)

### Question 1

What is a Python module?

A. A folder containing files

B. A Python file containing reusable code

C. A virtual environment

D. A package manager

**Answer:** B

---

### Question 2

Which keyword is used to import a module?

A. include

B. require

C. import

D. using

**Answer:** C

---

### Question 3

Which statement imports the entire math module?

A.

```python
from math import *
```

B.

```python
import math
```

C.

```python
using math
```

D.

```python
include math
```

**Answer:** B

---

### Question 4

Which command installs a package?

A.

```bash
python install requests
```

B.

```bash
pip install requests
```

C.

```bash
package install requests
```

D.

```bash
install requests
```

**Answer:** B

---

### Question 5

What is pip?

A. Python editor

B. Package manager

C. Database

D. Framework

**Answer:** B

---

### Question 6

What file identifies a Python package?

A. package.py

B. config.py

C. **init**.py

D. main.py

**Answer:** C

---

### Question 7

What is the purpose of a virtual environment?

A. Improve internet speed

B. Store databases

C. Isolate project dependencies

D. Create packages

**Answer:** C

---

### Question 8

Which command creates a virtual environment using venv?

A.

```bash
python create venv
```

B.

```bash
python -m venv venv
```

C.

```bash
pip create venv
```

D.

```bash
venv install
```

**Answer:** B

---

### Question 9

Which file stores project dependencies?

A. packages.txt

B. dependencies.txt

C. requirements.txt

D. install.txt

**Answer:** C

---

### Question 10

What is TestPyPI used for?

A. Testing Python syntax

B. Testing package uploads before publishing publicly

C. Testing databases

D. Testing virtual environments

**Answer:** B

---

# SECTION B — MULTIPLE SELECT QUESTIONS (15 Marks)

### Question 11

Select valid import statements.

☐ import math

☐ from math import sqrt

☐ import math as m

☐ include math

**Answers**

✓ import math

✓ from math import sqrt

✓ import math as m

---

### Question 12

Which are benefits of modules?

☐ Reusability

☐ Organization

☐ Easier Maintenance

☐ Code Duplication

**Answers**

✓ Reusability

✓ Organization

✓ Easier Maintenance

---

### Question 13

Select valid package management commands.

☐ pip install

☐ pip uninstall

☐ pip list

☐ pip show

**Answers**

✓ pip install

✓ pip uninstall

✓ pip list

✓ pip show

---

### Question 14

Which are benefits of virtual environments?

☐ Dependency Isolation

☐ Version Control

☐ Avoid Package Conflicts

☐ Project Independence

**Answers**

✓ Dependency Isolation

✓ Avoid Package Conflicts

✓ Project Independence

---

### Question 15

Which files are commonly found in Python packages?

☐ **init**.py

☐ README.md

☐ pyproject.toml

☐ requirements.txt

**Answers**

✓ **init**.py

✓ README.md

✓ pyproject.toml

✓ requirements.txt

---

# SECTION C — TRUE OR FALSE (10 Marks)

### Question 16

A package can contain multiple modules.

☐ True

☐ False

**Answer:** True

---

### Question 17

pip is included with most modern Python installations.

☐ True

☐ False

**Answer:** True

---

### Question 18

Virtual environments isolate project dependencies.

☐ True

☐ False

**Answer:** True

---

### Question 19

requirements.txt helps other developers install required packages.

☐ True

☐ False

**Answer:** True

---

### Question 20

TestPyPI is the same as the production PyPI repository.

☐ True

☐ False

**Answer:** False

---

# SECTION D — FILL IN THE GAPS (15 Marks)

### Question 21

A Python file containing reusable code is called a __________.

**Answer:** Module

---

### Question 22

The keyword used to load a module is __________.

**Answer:** import

---

### Question 23

A collection of related modules is called a __________.

**Answer:** Package

---

### Question 24

The package manager for Python is __________.

**Answer:** pip

---

### Question 25

The file used to identify a package is __________.

**Answer:** **init**.py

---

### Question 26

The command used to create a virtual environment is __________.

**Answer:** python -m venv venv

---

### Question 27

Project dependencies are stored in __________.

**Answer:** requirements.txt

---

### Question 28

The testing repository for Python packages is called __________.

**Answer:** TestPyPI

---

# SECTION E — MATCH THE FOLLOWING (10 Marks)

| Column A         | Column B                   |
| ---------------- | -------------------------- |
| Module           | Python File                |
| Package          | Collection of Modules      |
| import           | Load Module                |
| pip              | Package Manager            |
| venv             | Virtual Environment        |
| requirements.txt | Dependency List            |
| **init**.py      | Package Identifier         |
| pip install      | Install Package            |
| pip freeze       | Generate Dependency List   |
| TestPyPI         | Package Testing Repository |

---

# SECTION F — SHORT ANSWER QUESTIONS (10 Marks)

### Question 29

What is the difference between a module and a package?

---

### Question 30

Why should developers use virtual environments?

---

### Question 31

Explain the purpose of requirements.txt.

---

### Question 32

What is the role of pip in Python development?

---

### Question 33

Why is publishing to TestPyPI recommended before publishing to PyPI?

---

# SECTION G — CODE READING (10 Marks)

### Question 34

Given:

```python
# math_utils.py

def add(a, b):
    return a + b
```

```python
import math_utils

print(math_utils.add(2, 3))
```

What is the output?

**Answer**

```text
5
```

---

### Question 35

Predict the output.

```python
from math import sqrt

print(sqrt(25))
```

**Answer**

```text
5.0
```

---

### Question 36

Predict the output.

```python
import math as m

print(m.pow(2, 3))
```

**Answer**

```text
8.0
```

---

### Question 37

What does the following command do?

```bash
pip freeze > requirements.txt
```

**Answer:**

Generates a list of installed packages and saves them into a requirements.txt file.

---

# SECTION H — DEBUGGING QUESTIONS (5 Marks)

### Question 38

Find the error.

```python
from math import sqrtt

print(sqrtt(25))
```

**Answer**

The function name is incorrect.

Correct:

```python
from math import sqrt

print(sqrt(25))
```

---

### Question 39

Find the error.

```python
import math

print(sqrt(25))
```

**Answer**

sqrt belongs to the math module.

Correct:

```python
import math

print(math.sqrt(25))
```

---

# SECTION I — PRACTICAL PROGRAMMING (15 Marks)

### Question 40

Create a module named:

```text
calculator.py
```

Containing:

```python
add()
subtract()
multiply()
divide()
```

Import and use all functions in another file.

---

### Question 41

Create a package named:

```text
student_utils
```

Containing:

```text
student.py
grade.py
report.py
```

Include an **init**.py file.

---

### Question 42

Create a virtual environment and document the commands used to:

* Create
* Activate
* Deactivate

the environment.

---

### Question 43

Install the requests package and verify installation using pip commands.

---

# SECTION J — PACKAGE DEVELOPMENT PROJECT (Bonus 10 Marks)

## Build Your Own Python Package

Create:

```text
mytools/
│
├── mytools/
│   ├── __init__.py
│   ├── math_tools.py
│   ├── string_tools.py
│
├── README.md
├── pyproject.toml
└── requirements.txt
```

Features:

### Math Tools

```python
add()
subtract()
multiply()
divide()
```

### String Tools

```python
reverse_text()
count_vowels()
```

Demonstrate package usage.

---

# SECTION K — VIRTUAL ENVIRONMENT PROJECT

Create a new project.

Requirements:

1. Create a virtual environment.
2. Activate it.
3. Install:

   * requests
   * pandas
4. Generate requirements.txt.
5. Create a new virtual environment.
6. Install all dependencies using requirements.txt.

Document every command used.

---

# SECTION L — CAMBRIDGE A-LEVEL STYLE QUESTIONS

### Question 44

Explain three advantages of using modules.

---

### Question 45

Differentiate between:

* Module
* Package

with examples.

---

### Question 46

Describe how virtual environments prevent dependency conflicts.

---

### Question 47

Explain the purpose of **init**.py.

---

### Question 48

Discuss the importance of requirements.txt in team software development.

---

# ADVANCED TRACK (OPTIONAL)

## Upload Package to TestPyPI

### Tasks

1. Create a package.
2. Build the package.
3. Create a TestPyPI account.
4. Upload package using Twine.
5. Install package from TestPyPI.
6. Verify functionality.

Provide screenshots and documentation.

---

# END-OF-MODULE CHALLENGE

## Student Management Package

Build a reusable package called:

```text
student_manager
```

Modules:

```text
students.py
grades.py
reports.py
```

Features:

* Add Student
* Calculate Grade
* Generate Reports
* Save Reports

Requirements:

✓ Package Structure

✓ Virtual Environment

✓ requirements.txt

✓ Proper Imports

✓ Documentation

---

# Grading Guide

| Score    | Grade             |
| -------- | ----------------- |
| 90 – 100 | Excellent         |
| 80 – 89  | Very Good         |
| 70 – 79  | Good              |
| 60 – 69  | Fair              |
| Below 60 | Needs Improvement |

---

# End of Module 9 Assessment
