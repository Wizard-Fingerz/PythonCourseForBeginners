# Module 8 Assessment

## Advanced Object-Oriented Programming (Advanced OOP)

### Instructions

* Answer all questions.
* Read each question carefully.
* Some questions may have more than one correct answer.
* Attempt all practical questions.
* Total Marks: 100
* Duration: 120 Minutes

---

# Learning Objectives Assessment

By the end of this assessment, students should be able to:

✓ Explain advanced inheritance concepts

✓ Differentiate inheritance types

✓ Apply polymorphism

✓ Explain duck typing

✓ Create abstract classes using the ABC module

✓ Design interface-like structures

✓ Implement magic (dunder) methods

✓ Overload operators

✓ Design enterprise-level OOP solutions

✓ Build a banking system using advanced OOP principles

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (20 Marks)

### Question 1

Which inheritance type involves one child class inheriting from multiple parent classes?

A. Single Inheritance

B. Hierarchical Inheritance

C. Multiple Inheritance

D. Multilevel Inheritance

**Answer:** C

---

### Question 2

What does MRO stand for?

A. Method Runtime Operation

B. Method Resolution Order

C. Multiple Reference Object

D. Main Runtime Order

**Answer:** B

---

### Question 3

Which module is used for Abstract Base Classes?

A. oop

B. abstract

C. abc

D. classes

**Answer:** C

---

### Question 4

Which decorator is used to define abstract methods?

A. @property

B. @staticmethod

C. @abstractmethod

D. @override

**Answer:** C

---

### Question 5

Which OOP concept means "one interface, many forms"?

A. Encapsulation

B. Inheritance

C. Composition

D. Polymorphism

**Answer:** D

---

### Question 6

Which dunder method controls object printing?

A. **init**

B. **add**

C. **str**

D. **len**

**Answer:** C

---

### Question 7

Which dunder method enables the use of the `+` operator?

A. **sum**

B. **plus**

C. **add**

D. **append**

**Answer:** C

---

### Question 8

What is Duck Typing based on?

A. Class hierarchy

B. Data type

C. Behavior

D. Modules

**Answer:** C

---

### Question 9

Which relationship best describes Composition?

A. IS-A

B. HAS-A

C. INHERITS-A

D. OVERRIDES-A

**Answer:** B

---

### Question 10

Which of the following is an abstract class?

```python
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
```

A. Concrete Class

B. Utility Class

C. Abstract Class

D. Static Class

**Answer:** C

---

# SECTION B — MULTIPLE SELECT QUESTIONS (15 Marks)

### Question 11

Select valid inheritance types.

☐ Single Inheritance

☐ Multiple Inheritance

☐ Multilevel Inheritance

☐ Hierarchical Inheritance

☐ Circular Inheritance

**Answers**

✓ Single Inheritance

✓ Multiple Inheritance

✓ Multilevel Inheritance

✓ Hierarchical Inheritance

---

### Question 12

Select valid dunder methods.

☐ **init**

☐ **str**

☐ **len**

☐ **add**

☐ **money**

**Answers**

✓ **init**

✓ **str**

✓ **len**

✓ **add**

---

### Question 13

Select valid benefits of polymorphism.

☐ Flexibility

☐ Code Reuse

☐ Extensibility

☐ Cleaner Design

**Answers**

✓ Flexibility

✓ Code Reuse

✓ Extensibility

✓ Cleaner Design

---

### Question 14

Which concepts are commonly used in enterprise software?

☐ Abstract Classes

☐ Interfaces

☐ Inheritance

☐ Composition

**Answers**

✓ Abstract Classes

✓ Interfaces

✓ Inheritance

✓ Composition

---

### Question 15

Select examples of Composition.

☐ Car has an Engine

☐ House has Rooms

☐ Computer has CPU

☐ School has Departments

**Answers**

✓ Car has an Engine

✓ House has Rooms

✓ Computer has CPU

✓ School has Departments

---

# SECTION C — TRUE OR FALSE (10 Marks)

### Question 16

Multiple inheritance allows a class to inherit from more than one parent class.

☐ True

☐ False

**Answer:** True

---

### Question 17

Duck Typing depends on exact object type.

☐ True

☐ False

**Answer:** False

---

### Question 18

Abstract classes can contain abstract methods.

☐ True

☐ False

**Answer:** True

---

### Question 19

Operator overloading allows operators to work with custom objects.

☐ True

☐ False

**Answer:** True

---

### Question 20

The `__str__()` method should return a string.

☐ True

☐ False

**Answer:** True

---

# SECTION D — FILL IN THE GAPS (15 Marks)

### Question 21

The inheritance type where one child inherits from two or more parent classes is __________.

**Answer:** Multiple Inheritance

---

### Question 22

The Python module used for abstract classes is __________.

**Answer:** abc

---

### Question 23

The decorator used for abstract methods is __________.

**Answer:** @abstractmethod

---

### Question 24

The OOP principle that allows different objects to respond differently to the same method call is __________.

**Answer:** Polymorphism

---

### Question 25

The method used to customize printing of an object is __________.

**Answer:** **str**

---

### Question 26

The method used for operator overloading with the `+` operator is __________.

**Answer:** **add**

---

### Question 27

The relationship represented by "HAS-A" is called __________.

**Answer:** Composition

---

### Question 28

Python determines which method to call using __________.

**Answer:** MRO (Method Resolution Order)

---

# SECTION E — MATCH THE FOLLOWING (10 Marks)

| Column A             | Column B                     |
| -------------------- | ---------------------------- |
| Multiple Inheritance | Many Parents                 |
| MRO                  | Method Search Order          |
| Polymorphism         | Many Forms                   |
| Duck Typing          | Behavior-Based               |
| ABC                  | Abstract Base Class          |
| @abstractmethod      | Required Method              |
| **str**              | Object String Representation |
| **len**              | Custom Length                |
| **add**              | Addition Operator            |
| Composition          | HAS-A Relationship           |

---

# SECTION F — SHORT ANSWER QUESTIONS (10 Marks)

### Question 29

Explain Multiple Inheritance.

---

### Question 30

What problem does MRO solve?

---

### Question 31

Differentiate between Abstract Classes and Regular Classes.

---

### Question 32

Explain Duck Typing with an example.

---

### Question 33

What is Operator Overloading?

---

# SECTION G — CODE READING (10 Marks)

### Question 34

Predict the output.

```python
class Dog:

    def speak(self):
        print("Woof")

dog = Dog()

dog.speak()
```

**Answer**

```text
Woof
```

---

### Question 35

Predict the output.

```python
class Student:

    def __str__(self):
        return "Student Object"

student = Student()

print(student)
```

**Answer**

```text
Student Object
```

---

### Question 36

Predict the output.

```python
class Number:

    def __len__(self):
        return 5

n = Number()

print(len(n))
```

**Answer**

```text
5
```

---

### Question 37

Predict the output.

```python
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(
            self.amount + other.amount
        )

m1 = Money(100)
m2 = Money(50)

result = m1 + m2

print(result.amount)
```

**Answer**

```text
150
```

---

# SECTION H — DEBUGGING QUESTIONS (5 Marks)

### Question 38

Find the error.

```python
from abc import ABC

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```

**Answer**

Missing import.

Correct:

```python
from abc import ABC
from abc import abstractmethod
```

---

### Question 39

Find the error.

```python
class Student:

    def __str__(self):
        print("Student")
```

**Answer**

`__str__()` must return a string.

Correct:

```python
class Student:

    def __str__(self):
        return "Student"
```

---

# SECTION I — PRACTICAL PROGRAMMING (15 Marks)

### Question 40

Create a Shape Abstract Class.

Requirements:

```python
class Shape(ABC):
```

Abstract Method:

```python
area()
```

Create subclasses:

* Rectangle
* Circle

Implement the area calculation.

---

### Question 41

Create a Vehicle class.

Create subclasses:

* Car
* Bike
* Truck

Override:

```python
start()
```

for each subclass.

---

### Question 42

Create a custom Vector class that supports:

```python
vector1 + vector2
```

using operator overloading.

---

### Question 43

Create a custom Book class.

Implement:

```python
__str__()
```

to display book details.

---

# SECTION J — BANKING SYSTEM PROJECT (Bonus 10 Marks)

## Banking System

Create:

### Abstract Class

```python
Account
```

Methods:

```python
deposit()
withdraw()
check_balance()
```

---

### Subclasses

#### SavingsAccount

Additional:

```python
interest_rate
```

---

#### CurrentAccount

Additional:

```python
overdraft_limit
```

---

### Features

* Deposit
* Withdraw
* Transfer Funds
* Display Balance

---

# SECTION K — ADVANCED POLYMORPHISM PROJECT

Create a Payroll System.

Parent:

```python
Employee
```

Subclasses:

```python
Manager
Developer
Intern
```

Each class must override:

```python
calculate_salary()
```

Display salaries using:

```python
for employee in employees:
    print(employee.calculate_salary())
```

---

# SECTION L — ADVANCED OOP EXAM QUESTIONS

### Question 44

Differentiate between:

* Encapsulation
* Abstraction

---

### Question 45

Differentiate between:

* Inheritance
* Composition

---

### Question 46

Explain how Duck Typing differs from traditional polymorphism.

---

### Question 47

Explain the role of Abstract Classes in large software systems.

---

### Question 48

Discuss three advantages and two disadvantages of Multiple Inheritance.

---

# END-OF-MODULE CHALLENGE

## Fintech Banking Platform

Design a mini banking application that demonstrates:

### OOP Concepts

✓ Abstract Classes

✓ Inheritance

✓ Polymorphism

✓ Composition

✓ Operator Overloading

✓ Magic Methods

---

### Entities

* Customer
* Account
* Savings Account
* Current Account
* Transaction

---

### Features

* Open Account
* Deposit
* Withdraw
* Transfer Funds
* Transaction History
* Account Summary

---

### Bonus

Implement:

```python
account1 + account2
```

to combine balances using operator overloading.

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

# End of Module 8 Assessment
