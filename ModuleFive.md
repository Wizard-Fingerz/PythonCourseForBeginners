
---

# Module 5: Functions & Functional Programming

![Functions](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+5:+Functions+and+Functional+Programming)

---

# Learning Objectives

By the end of this module students should be able to:

✓ Create functions

✓ Use parameters and return values

✓ Understand variable scope

✓ Use global and nonlocal

✓ Import Python modules

✓ Create custom modules

✓ Use lambda functions

✓ Use map, filter and reduce

✓ Write docstrings

✓ Apply type hints

✓ Understand decorators

✓ Build reusable Python utilities

---

# 1. Introduction to Functions

## What is a Function?

A function is a reusable block of code that performs a specific task.

Think of a function like a blender.

```text
Ingredients
    ↓
 Blender
    ↓
 Smoothie
```

Input goes in.

Output comes out.

Functions work exactly the same way.

---

## Why Functions Matter

Without functions:

```python
name = input("Name: ")

print(f"Hello {name}")

name = input("Name: ")

print(f"Hello {name}")

name = input("Name: ")

print(f"Hello {name}")
```

Lots of repetition.

With functions:

```python
def greet():
    name = input("Name: ")
    print(f"Hello {name}")
```

Now:

```python
greet()
greet()
greet()
```

Cleaner.

Reusable.

Professional.

---

# 2. Defining Functions

Syntax:

```python
def function_name():
    code
```

Example:

```python
def say_hello():
    print("Hello World")
```

---

## Calling a Function

Creating a function does not execute it.

You must call it.

```python
say_hello()
```

Output:

```text
Hello World
```

---

# Function Flow Diagram

```text
Define Function
       ↓
Function Stored
       ↓
Function Called
       ↓
Code Executes
```

---

# Functions with Parameters

Parameters allow functions to receive data.

```python
def greet(name):
    print(f"Hello {name}")
```

Usage:

```python
greet("Adewale")
```

Output:

```text
Hello Adewale
```

---

# Multiple Parameters

```python
def student(name, age):

    print(
        f"{name} is {age}"
    )
```

Usage:

```python
student(
    "Mary",
    20
)
```

---

# Return Values

Many beginners confuse print() and return.

Example:

```python
def add(a, b):
    return a + b
```

Usage:

```python
result = add(5, 3)

print(result)
```

Output:

```text
8
```

---

# print vs return

Bad:

```python
def add(a, b):
    print(a + b)
```

Better:

```python
def add(a, b):
    return a + b
```

Why?

Because returned values can be reused.

---

# 3. Default Arguments

Sometimes we want default values.

```python
def greet(name="Student"):
    print(
        f"Hello {name}"
    )
```

Usage:

```python
greet()
```

Output:

```text
Hello Student
```

---

Usage:

```python
greet("Adewale")
```

Output:

```text
Hello Adewale
```

---

# Keyword Arguments

```python
def student(name, age):
    print(name, age)
```

Instead of:

```python
student(
    "Mary",
    20
)
```

We can write:

```python
student(
    age=20,
    name="Mary"
)
```

Order no longer matters.

---

# 4. Scope & Namespaces

![Scope](https://placehold.co/1000x400/1f2937/ffffff.png?text=Global+Scope+vs+Local+Scope)

Scope determines where variables are visible.

---

# Local Scope

```python
def test():

    age = 25

    print(age)
```

Works:

```python
test()
```

Fails:

```python
print(age)
```

Because age exists only inside the function.

---

# Global Scope

```python
age = 25

def test():
    print(age)
```

Works because age is global.

---

# LEGB Rule

Python searches variables in this order:

```text
Local
 ↓
Enclosing
 ↓
Global
 ↓
Built-in
```

---

# Built-in Namespace

Python automatically provides:

```python
print()
len()
max()
min()
sum()
```

These belong to Python's built-in namespace.

---

# Nested Functions

```python
def outer():

    def inner():
        print("Hello")

    inner()
```

---

# Enclosing Scope

```python
def outer():

    message = "Hello"

    def inner():
        print(message)

    inner()
```

Inner function accesses outer variable.

---

# nonlocal Keyword

```python
def outer():

    count = 0

    def inner():

        nonlocal count

        count += 1

    inner()
```

Allows modification of enclosing variables.

---

# global Keyword

```python
count = 0

def increase():

    global count

    count += 1
```

Modifies global variables.

---

# 5. Python Modules

## What is a Module?

A module is a Python file containing reusable code.

Example:

```text
math_utils.py
```

Inside:

```python
def add(a, b):
    return a + b
```

---

# Importing Modules

```python
import math
```

Usage:

```python
print(math.sqrt(25))
```

Output:

```text
5
```

---

# Import Specific Functions

```python
from math import sqrt
```

Usage:

```python
print(sqrt(25))
```

---

# Import Alias

```python
import numpy as np
```

---

# import *

```python
from math import *
```

Not recommended.

Can cause name conflicts.

---

# **name** == "**main**"

Professional Python pattern.

```python
def main():
    print("Running")

if __name__ == "__main__":
    main()
```

Ensures code runs only when file is executed directly.

---

# Turtle Graphics

Python includes a turtle module.

Example:

```python
import turtle

t = turtle.Turtle()

t.forward(100)
```

Students love this.

Good visual introduction.

---

# Web Browser Module

```python
import webbrowser

webbrowser.open(
    "https://www.python.org"
)
```

Launches browser automatically.

---

# 6. Lambda Expressions

## What is a Lambda?

A lambda is an anonymous function.

Traditional:

```python
def square(x):
    return x * x
```

Lambda:

```python
lambda x: x * x
```

---

Usage:

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

---

# 7. map()

Applies a function to every item.

Example:

```python
numbers = [1,2,3]

result = map(
    lambda x: x*2,
    numbers
)
```

---

Convert:

```python
print(list(result))
```

Output:

```text
[2,4,6]
```

---

# 8. filter()

Filters data.

```python
numbers = [1,2,3,4]

result = filter(
    lambda x: x%2==0,
    numbers
)
```

Output:

```text
[2,4]
```

---

# 9. reduce()

Requires:

```python
from functools import reduce
```

Example:

```python
reduce(
    lambda x,y:x+y,
    [1,2,3,4]
)
```

Output:

```text
10
```

---

# 10. Decorators (Introduction)

Decorator:

```python
@something
```

Modifies function behavior.

Simple example:

```python
def decorator(func):

    def wrapper():

        print("Before")

        func()

        print("After")

    return wrapper
```

---

Usage:

```python
@decorator
def hello():
    print("Hello")
```

Output:

```text
Before
Hello
After
```

---

# 11. Docstrings

Good documentation:

```python
def add(a, b):
    """
    Add two numbers.

    Returns:
        Sum of a and b.
    """

    return a + b
```

---

# Why Docstrings Matter

Professional developers use:

* VS Code
* PyCharm
* Sphinx
* Documentation generators

Docstrings power those tools.

---

# Type Hints

```python
def add(
    a: int,
    b: int
) -> int:

    return a + b
```

Improves readability.

---

# Combining Defaults + Type Hints

```python
def greet(
    name: str = "Student"
) -> str:

    return f"Hello {name}"
```

---

# Practical 1: Build Your Own Math Module

Create:

```text
my_math.py
```

Functions:

```python
add()
subtract()
multiply()
divide()
```

Import into another file.

---

# Practical 2: Custom String Functions

Create:

```python
reverse_text()

capitalize_words()

count_vowels()
```

---

# Practical 3: Palindrome Checker

Example:

```text
madam
```

Forward:

```text
madam
```

Backward:

```text
madam
```

Palindrome.

---

## Function

```python
def is_palindrome(word):

    return (
        word ==
        word[::-1]
    )
```

---

# Enhanced Palindrome Checker

Case insensitive:

```python
word = word.lower()
```

---

Ignore spaces:

```python
word = word.replace(
    " ",
    ""
)
```

---

Ignore punctuation:

Use:

```python
import string
```

---

# Fibonacci Numbers

Sequence:

```text
0
1
1
2
3
5
8
13
21
```

---

# Fibonacci Function

```python
def fibonacci(n):

    a = 0
    b = 1

    for _ in range(n):

        print(a)

        a, b = (
            b,
            a+b
        )
```

---

# Practical 4: Fibonacci Generator

```python
fibonacci(10)
```

Output:

```text
0
1
1
2
3
5
8
13
21
34
```

---

# Module Summary

In this module we learned:

✓ Functions

✓ Parameters

✓ Return Values

✓ Default Arguments

✓ Keyword Arguments

✓ Local Scope

✓ Global Scope

✓ Enclosing Scope

✓ Built-in Namespace

✓ Modules

✓ Imports

✓ Lambda Functions

✓ map()

✓ filter()

✓ reduce()

✓ Decorators

✓ Docstrings

✓ Type Hints

✓ Palindrome Checker

✓ Fibonacci Generator

Functions are the backbone of modern Python programming. Everything from Django views to AI models, APIs, automation scripts, and data science pipelines relies heavily on well-designed functions.

```

