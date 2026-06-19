
---

# Module 9: Modules, Packages & Virtual Environments

![Modules and Packages](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+9:+Modules+Packages+and+Virtual+Environments)

---

# Learning Objectives

By the end of this module students should be able to:

✓ Create Python modules

✓ Import modules correctly

✓ Create Python packages

✓ Install third-party packages

✓ Use pip effectively

✓ Create virtual environments

✓ Manage project dependencies

✓ Generate requirements.txt files

✓ Build reusable Python packages

✓ Publish packages to TestPyPI

---

# Chapter 1: Introduction to Modules

## What is a Module?

A module is simply a Python file that contains reusable code.

Example:

```text
math_utils.py
```

Inside:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

This file is now a module.

---

# Why Use Modules?

Imagine building a calculator application.

Without modules:

```python
# main.py

def add():
    pass

def subtract():
    pass

def multiply():
    pass

def divide():
    pass

# Hundreds of lines...
```

Everything becomes messy.

---

With modules:

```text
project/
│
├── main.py
├── math_utils.py
├── string_utils.py
└── file_utils.py
```

Cleaner.

Organized.

Professional.

---

# Importing Modules

Suppose:

```text
math_utils.py
```

Contains:

```python
def add(a, b):
    return a + b
```

---

Import entire module:

```python
import math_utils

print(
    math_utils.add(2, 3)
)
```

Output:

```text
5
```

---

# Import Specific Functions

```python
from math_utils import add

print(add(2, 3))
```

---

# Import Multiple Functions

```python
from math_utils import (
    add,
    subtract
)
```

---

# Import Alias

```python
import math_utils as mu

print(mu.add(2, 3))
```

---

# Module Search Path

Python searches:

```text
1. Current Folder
2. Installed Packages
3. Python System Libraries
```

You can inspect:

```python
import sys

print(sys.path)
```

---

# Chapter 2: Packages

## What is a Package?

A package is a collection of modules.

Example:

```text
calculator/
│
├── __init__.py
├── basic.py
├── advanced.py
└── statistics.py
```

---

# Why Packages?

Modules solve small organization problems.

Packages solve large organization problems.

Example:

```text
ecommerce/
│
├── products/
├── orders/
├── payments/
├── users/
└── inventory/
```

---

# The **init**.py File

Marks a folder as a package.

Example:

```text
calculator/
│
├── __init__.py
├── basic.py
```

---

# Importing from Packages

```python
from calculator.basic import add
```

---

Usage:

```python
print(add(10, 5))
```

Output:

```text
15
```

---

# Package Structure Example

```text
school_system/
│
├── students/
│   ├── __init__.py
│   └── student.py
│
├── teachers/
│   ├── __init__.py
│   └── teacher.py
│
└── main.py
```

---

# Chapter 3: Installing Packages with pip

## What is pip?

pip is Python's package manager.

Think of it as:

```text
Play Store for Python
```

or

```text
App Store for Python
```

---

# Installing Packages

Syntax:

```bash
pip install package_name
```

Example:

```bash
pip install requests
```

---

# What Happens?

pip downloads:

```text
requests
```

from:

Python Package Index (PyPI)

and installs it.

---

# Checking Installed Packages

```bash
pip list
```

---

# Package Information

```bash
pip show requests
```

---

# Updating Packages

```bash
pip install --upgrade requests
```

---

# Removing Packages

```bash
pip uninstall requests
```

---

# Popular Packages

| Package    | Purpose             |
| ---------- | ------------------- |
| requests   | HTTP Requests       |
| pandas     | Data Analysis       |
| numpy      | Numerical Computing |
| flask      | Web Development     |
| django     | Web Development     |
| matplotlib | Data Visualization  |

---

# Chapter 4: Virtual Environments

## The Problem

Suppose:

Project A requires:

```text
Django 4.2
```

Project B requires:

```text
Django 5.2
```

Installing both globally causes conflicts.

---

# Solution: Virtual Environments

A virtual environment creates an isolated Python environment.

```text
Project A
   |
 Virtual Environment A

Project B
   |
 Virtual Environment B
```

Each project has its own packages.

---

# Creating a Virtual Environment

Using venv:

```bash
python -m venv venv
```

---

Folder Created:

```text
project/
│
├── venv/
├── main.py
```

---

# Activating Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

### Mac/Linux

```bash
source venv/bin/activate
```

---

After activation:

```text
(venv)
```

appears in terminal.

---

# Installing Packages Inside venv

```bash
pip install requests
```

Only this project gets the package.

---

# Deactivating Environment

```bash
deactivate
```

---

# Chapter 5: Conda Environments

## What is Conda?

Conda is both:

* Package Manager
* Environment Manager

Popular in:

* Data Science
* Machine Learning
* AI

---

# Create Environment

```bash
conda create -n myenv python=3.12
```

---

# Activate

```bash
conda activate myenv
```

---

# Deactivate

```bash
conda deactivate
```

---

# venv vs Conda

| venv                  | Conda                  |
| --------------------- | ---------------------- |
| Built into Python     | External Tool          |
| Lightweight           | Larger                 |
| Great for Development | Great for Data Science |

---

# Chapter 6: Requirements Files

## The Problem

You build a project using:

```text
Flask
Requests
Pandas
```

Someone else downloads your code.

How do they know what packages are required?

---

# Solution

requirements.txt

---

# Generate Requirements File

```bash
pip freeze > requirements.txt
```

Example:

```text
flask==3.1.0
requests==2.32.0
pandas==2.3.0
```

---

# Install from Requirements File

```bash
pip install -r requirements.txt
```

---

# Why Requirements Matter

Without:

```text
Works on my computer
```

With requirements:

```text
Works on every computer
```

---

# Chapter 7: Building Your Own Package

Project Structure:

```text
mycalculator/
│
├── mycalculator/
│   ├── __init__.py
│   └── calculator.py
│
├── README.md
├── pyproject.toml
└── LICENSE
```

---

# calculator.py

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

---

# **init**.py

```python
from .calculator import (
    add,
    subtract
)
```

---

# Usage

```python
from mycalculator import add

print(add(5, 3))
```

Output:

```text
8
```

---

# Chapter 8: Publishing to TestPyPI

## What is TestPyPI?

TestPyPI

A testing version of PyPI.

Used before publishing publicly.

---

# Build Package

```bash
python -m build
```

---

# Upload Package

```bash
twine upload \
--repository testpypi \
dist/*
```

---

# Install from TestPyPI

```bash
pip install \
--index-url \
https://test.pypi.org/simple/ \
mycalculator
```

---

# Practical 1: Create Your Own Module

Create:

```text
math_tools.py
```

Functions:

```python
add()
subtract()
multiply()
divide()
```

Import and use them.

---

# Practical 2: Build a Package

Create:

```text
student_utils/
```

Modules:

```text
student.py
grade.py
report.py
```

Package them together.

---

# Practical 3: Requirements Generator

Create a project.

Install:

```bash
pip install requests
pip install pandas
```

Generate:

```text
requirements.txt
```

Install it in a fresh virtual environment.

---

# Practical 4 (Advanced Track)

Publish your package to:

TestPyPI

Requirements:

✓ Build package

✓ Create account

✓ Upload package

✓ Install package

✓ Verify functionality

---

# Common Beginner Mistakes

### Forgetting to Activate Virtual Environment

Wrong:

```bash
pip install requests
```

Installs globally.

Always activate first.

---

### Not Using requirements.txt

Makes collaboration difficult.

---

### Using import *

Wrong:

```python
from math import *
```

Can cause conflicts.

Prefer:

```python
from math import sqrt
```

---

### Forgetting **init**.py

Without it:

```text
Package may not be recognized
```

---

# Real-World Project

## Student Management Package

Structure:

```text
student_manager/
│
├── student_manager/
│   ├── __init__.py
│   ├── students.py
│   ├── grades.py
│   └── reports.py
│
├── requirements.txt
├── README.md
└── pyproject.toml
```

Features:

* Add Student
* Calculate Grade
* Generate Report
* Install as Package

---

# Module Summary

In this module we learned:

✓ Modules

✓ Imports

✓ Packages

✓ **init**.py

✓ pip

✓ Package Installation

✓ Virtual Environments

✓ venv

✓ Conda

✓ requirements.txt

✓ Building Packages

✓ Publishing Packages

✓ TestPyPI

✓ Professional Python Project Structure

This module teaches students how real-world Python projects are organized and distributed. These skills are essential for software engineering, open-source development, team collaboration, package management, and professional Python development.

---

## Recommended Duration
