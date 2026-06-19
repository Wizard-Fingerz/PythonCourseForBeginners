
---

# Module 7: Object-Oriented Programming (OOP) Fundamentals

![OOP](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+7:+Object+Oriented+Programming)

---

# Learning Objectives

By the end of this module students should be able to:

✓ Explain Object-Oriented Programming

✓ Create classes and objects

✓ Use constructors

✓ Create attributes and methods

✓ Use encapsulation

✓ Use properties

✓ Apply inheritance

✓ Override methods

✓ Use polymorphism

✓ Understand duck typing

✓ Apply composition and aggregation

✓ Build real-world OOP applications

---

# Chapter 1: What is OOP?

## Procedural Programming

Everything we've done so far:

```python
name = "John"

score = 80

print(name)
```

This is called Procedural Programming.

---

## The Problem

Imagine a school with:

```text
1000 Students
100 Teachers
50 Courses
```

Creating variables for everything becomes impossible.

---

## OOP Solution

Represent real-world objects as software objects.

```text
Real Student
      ↓
Python Object
```

Example:

```python
student = Student(
    "John",
    80
)
```

---

# What is a Class?

A class is a blueprint.

Example:

Blueprint:

```text
House Design
```

Actual House:

```text
House #1
House #2
House #3
```

---

In Python:

```python
class Student:
    pass
```

Student is the blueprint.

---

# What is an Object?

An object is an instance of a class.

```python
student1 = Student()

student2 = Student()
```

Two different objects.

---

# Class vs Object

| Class      | Object         |
| ---------- | -------------- |
| Blueprint  | Real Instance  |
| Student    | John           |
| Car        | Toyota Corolla |
| House Plan | Actual House   |

---

# Chapter 2: Constructors

## What is a Constructor?

A constructor runs automatically when an object is created.

Python constructor:

```python
__init__()
```

---

Example:

```python
class Student:

    def __init__(self):

        print(
            "Student Created"
        )
```

Usage:

```python
student = Student()
```

Output:

```text
Student Created
```

---

# The self Parameter

Every instance method receives:

```python
self
```

Example:

```python
class Student:

    def __init__(self):

        self.name = "John"
```

---

Think of:

```python
self
```

as:

```text
This Object
```

---

# Instance Attributes

```python
class Student:

    def __init__(
        self,
        name,
        age
    ):

        self.name = name

        self.age = age
```

Usage:

```python
student = Student(
    "John",
    20
)
```

---

Access:

```python
print(student.name)
```

Output:

```text
John
```

---

# Chapter 3: Methods

Methods are functions inside classes.

---

Example:

```python
class Student:

    def greet(self):

        print(
            "Hello"
        )
```

Usage:

```python
student = Student()

student.greet()
```

---

# Bank Account Example

```python
class BankAccount:

    def __init__(
        self,
        balance
    ):

        self.balance = balance

    def deposit(
        self,
        amount
    ):

        self.balance += amount
```

---

Usage:

```python
account = BankAccount(
    1000
)

account.deposit(500)
```

---

# Class Attributes

Shared by all objects.

```python
class Student:

    school = "ABC College"
```

Every student shares:

```text
ABC College
```

---

# Static Methods

Methods that don't use self.

```python
class MathTools:

    @staticmethod

    def add(a, b):

        return a + b
```

Usage:

```python
MathTools.add(2, 3)
```

---

# Chapter 4: Encapsulation

Encapsulation means hiding internal details.

---

# Public Attribute

```python
student.name
```

Accessible everywhere.

---

# Protected Attribute

Convention:

```python
self._name
```

Means:

```text
Use Carefully
```

---

# Private Attribute

```python
self.__password
```

Python performs:

```text
Name Mangling
```

---

Example:

```python
class User:

    def __init__(self):

        self.__password = "1234"
```

Access:

```python
user.__password
```

Produces error.

---

# Name Mangling

Python secretly changes:

```text
__password
```

to:

```text
_User__password
```

---

# Chapter 5: Properties

Properties allow controlled access.

---

Without Properties

```python
student.age = -10
```

Problem.

Invalid age.

---

# Getter Example

```python
class Student:

    @property

    def age(self):

        return self._age
```

---

# Setter Example

```python
@age.setter

def age(
    self,
    value
):

    if value >= 0:

        self._age = value
```

---

Usage:

```python
student.age = 20
```

---

# Chapter 6: Inheritance

Inheritance allows classes to reuse existing classes.

---

Example:

```python
class Animal:

    def speak(self):

        print("Sound")
```

---

Child Class

```python
class Dog(Animal):

    pass
```

---

Usage:

```python
dog = Dog()

dog.speak()
```

Output:

```text
Sound
```

---

# Extending Parent Classes

```python
class Dog(Animal):

    def bark(self):

        print("Woof")
```

---

# super()

Calls parent functionality.

```python
class Dog(Animal):

    def __init__(self):

        super().__init__()
```

---

# Method Overriding

Change inherited behavior.

Parent:

```python
class Animal:

    def speak(self):

        print("Animal Sound")
```

Child:

```python
class Dog(Animal):

    def speak(self):

        print("Woof")
```

---

Output:

```text
Woof
```

---

# Chapter 7: Polymorphism

One interface.

Many forms.

---

Example:

```python
class Dog:

    def speak(self):

        print("Woof")
```

```python
class Cat:

    def speak(self):

        print("Meow")
```

---

Usage:

```python
animals = [
    Dog(),
    Cat()
]

for animal in animals:

    animal.speak()
```

Output:

```text
Woof
Meow
```

---

# Duck Typing

Python doesn't care about type.

It cares about behavior.

---

Example:

```python
class Duck:

    def fly(self):

        print("Flying")
```

```python
class Airplane:

    def fly(self):

        print("Flying")
```

---

Both work:

```python
obj.fly()
```

---

# Chapter 8: Composition

Inheritance:

```text
IS-A
```

Composition:

```text
HAS-A
```

---

Example:

```python
class Engine:
    pass
```

```python
class Car:

    def __init__(self):

        self.engine = Engine()
```

---

Relationship:

```text
Car HAS-A Engine
```

---

# Aggregation

Weaker version of composition.

---

Example:

```python
class Department:
    pass
```

```python
class Teacher:

    def __init__(
        self,
        department
    ):

        self.department = department
```

Department can exist without Teacher.

---

# Chapter 9: Practical Project 1

## Student Class System

```python
class Student:

    def __init__(
        self,
        name,
        score
    ):

        self.name = name

        self.score = score

    def grade(self):

        if self.score >= 70:
            return "A"

        return "F"
```

---

Usage:

```python
student = Student(
    "John",
    80
)

print(
    student.grade()
)
```

Output:

```text
A
```

---

# Practical Project 2

## Employee Payroll System

```python
class Employee:

    def __init__(
        self,
        name,
        salary
    ):

        self.name = name

        self.salary = salary

    def annual_salary(
        self
    ):

        return (
            self.salary * 12
        )
```

---

Usage:

```python
employee = Employee(
    "Mary",
    200000
)

print(
    employee.annual_salary()
)
```

Output:

```text
2400000
```

---

# Common Beginner Mistakes

### Forgetting self

Wrong:

```python
class Student:

    def greet():

        print("Hello")
```

Correct:

```python
class Student:

    def greet(self):

        print("Hello")
```

---

### Not Calling Constructor Properly

Wrong:

```python
student = Student
```

Correct:

```python
student = Student()
```

---

### Accessing Private Variables Directly

Wrong:

```python
user.__password
```

Use getters/properties instead.

---

# OOP Summary

In this module we learned:

✓ Classes

✓ Objects

✓ Constructors

✓ self

✓ Instance Attributes

✓ Class Attributes

✓ Methods

✓ Static Methods

✓ Encapsulation

✓ Properties

✓ Inheritance

✓ Method Overriding

✓ super()

✓ Polymorphism

✓ Duck Typing

✓ Composition

✓ Aggregation

✓ Student Management Systems

✓ Employee Payroll Systems

OOP is the foundation of professional Python development and is heavily used in frameworks such as Django, Flask, FastAPI, desktop applications, game development, enterprise systems, and AI projects.

---

## Recommended Duration

