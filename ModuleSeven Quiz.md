# Module 7 Assessment

## Object-Oriented Programming (OOP) Fundamentals

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

✓ Explain Object-Oriented Programming

✓ Create classes and objects

✓ Use constructors

✓ Create and access attributes

✓ Create methods

✓ Differentiate instance and class attributes

✓ Apply encapsulation

✓ Use properties, getters and setters

✓ Implement inheritance

✓ Override methods

✓ Use polymorphism

✓ Understand duck typing

✓ Apply composition and aggregation

✓ Build simple OOP applications

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (20 Marks)

### Question 1

What does OOP stand for?

A. Object Organized Programming

B. Object-Oriented Programming

C. Ordered Object Programming

D. Operational Object Programming

**Answer:** B

---

### Question 2

A class is best described as:

A. A variable

B. A function

C. A blueprint for creating objects

D. A loop

**Answer:** C

---

### Question 3

An object is:

A. A blueprint

B. An instance of a class

C. A variable

D. A module

**Answer:** B

---

### Question 4

Which special method acts as a constructor in Python?

A. **main**()

B. **class**()

C. **init**()

D. **self**()

**Answer:** C

---

### Question 5

What is the purpose of `self`?

A. Refers to the current object

B. Refers to the class

C. Refers to Python

D. Refers to a module

**Answer:** A

---

### Question 6

Which attribute belongs to individual objects?

A. Global Attribute

B. Instance Attribute

C. Static Attribute

D. Shared Attribute

**Answer:** B

---

### Question 7

Which attribute is shared among all instances?

A. Instance Attribute

B. Private Attribute

C. Class Attribute

D. Local Attribute

**Answer:** C

---

### Question 8

Which decorator is used to create a property?

A. @staticmethod

B. @property

C. @class

D. @private

**Answer:** B

---

### Question 9

Which keyword is used to call a parent class method?

A. parent

B. base

C. super

D. inherit

**Answer:** C

---

### Question 10

What is method overriding?

A. Creating a new class

B. Replacing a parent method in a child class

C. Creating an object

D. Importing methods

**Answer:** B

---

# SECTION B — MULTIPLE SELECT QUESTIONS (15 Marks)

### Question 11

Select the four pillars of OOP.

☐ Encapsulation

☐ Inheritance

☐ Polymorphism

☐ Abstraction

☐ Compilation

**Answers**

✓ Encapsulation

✓ Inheritance

✓ Polymorphism

✓ Abstraction

---

### Question 12

Which are valid OOP concepts?

☐ Classes

☐ Objects

☐ Methods

☐ Attributes

☐ Variables

**Answers**

✓ Classes

✓ Objects

✓ Methods

✓ Attributes

---

### Question 13

Select valid method types.

☐ Instance Methods

☐ Static Methods

☐ Class Methods

☐ Private Methods

**Answers**

✓ Instance Methods

✓ Static Methods

✓ Class Methods

✓ Private Methods

---

### Question 14

Which statements are true about inheritance?

☐ Child classes inherit parent behavior

☐ Code reuse is possible

☐ Child classes can override methods

☐ Parent classes inherit from child classes

**Answers**

✓ Child classes inherit parent behavior

✓ Code reuse is possible

✓ Child classes can override methods

---

### Question 15

Which are examples of composition?

☐ Car has an Engine

☐ House has Rooms

☐ School has Students

☐ Student is a Person

**Answers**

✓ Car has an Engine

✓ House has Rooms

✓ School has Students

---

# SECTION C — TRUE OR FALSE (10 Marks)

### Question 16

A class is used to create objects.

☐ True

☐ False

**Answer:** True

---

### Question 17

Every object created from a class shares the same instance attributes.

☐ True

☐ False

**Answer:** False

---

### Question 18

Inheritance promotes code reuse.

☐ True

☐ False

**Answer:** True

---

### Question 19

Polymorphism allows different objects to respond differently to the same method call.

☐ True

☐ False

**Answer:** True

---

### Question 20

Duck typing focuses on behavior rather than exact object type.

☐ True

☐ False

**Answer:** True

---

# SECTION D — FILL IN THE GAPS (15 Marks)

### Question 21

A __________ is a blueprint for creating objects.

**Answer:** Class

---

### Question 22

An __________ is an instance of a class.

**Answer:** Object

---

### Question 23

The special constructor method is __________.

**Answer:** **init**

---

### Question 24

The keyword that refers to the current object is __________.

**Answer:** self

---

### Question 25

A variable belonging to an object is called an __________ attribute.

**Answer:** Instance

---

### Question 26

The decorator used to create properties is __________.

**Answer:** @property

---

### Question 27

The keyword used to access parent class functionality is __________.

**Answer:** super

---

### Question 28

The OOP concept that allows one class to inherit from another is __________.

**Answer:** Inheritance

---

# SECTION E — MATCH THE FOLLOWING (10 Marks)

| Column A     | Column B                    |
| ------------ | --------------------------- |
| Class        | Blueprint                   |
| Object       | Instance                    |
| **init**     | Constructor                 |
| self         | Current Object              |
| Method       | Function Inside Class       |
| Property     | Controlled Attribute Access |
| Inheritance  | Code Reuse                  |
| Polymorphism | Many Forms                  |
| Composition  | HAS-A Relationship          |
| Aggregation  | Weak HAS-A Relationship     |

---

# SECTION F — SHORT ANSWER QUESTIONS (10 Marks)

### Question 29

What is Object-Oriented Programming?

---

### Question 30

Differentiate between a class and an object.

---

### Question 31

Explain the purpose of the constructor (`__init__`).

---

### Question 32

What is encapsulation?

---

### Question 33

Differentiate between composition and inheritance.

---

# SECTION G — CODE READING (10 Marks)

### Question 34

Predict the output.

```python
class Student:

    def __init__(self):
        self.name = "John"

student = Student()

print(student.name)
```

**Answer**

```text
John
```

---

### Question 35

Predict the output.

```python
class Calculator:

    def add(self, a, b):
        return a + b

calc = Calculator()

print(calc.add(2, 3))
```

**Answer**

```text
5
```

---

### Question 36

Predict the output.

```python
class Animal:

    def speak(self):
        print("Animal Sound")

class Dog(Animal):
    pass

dog = Dog()

dog.speak()
```

**Answer**

```text
Animal Sound
```

---

### Question 37

Predict the output.

```python
class Dog:

    def speak(self):
        print("Woof")

class Cat:

    def speak(self):
        print("Meow")

animals = [
    Dog(),
    Cat()
]

for animal in animals:
    animal.speak()
```

**Answer**

```text
Woof
Meow
```

---

# SECTION H — DEBUGGING QUESTIONS (5 Marks)

### Question 38

Identify the error.

```python
class Student

    def __init__(self):
        self.name = "John"
```

**Answer**

Missing colon after class declaration.

Correct:

```python
class Student:

    def __init__(self):
        self.name = "John"
```

---

### Question 39

Identify the error.

```python
class Student:

    def greet():
        print("Hello")
```

**Answer**

Missing self parameter.

Correct:

```python
class Student:

    def greet(self):
        print("Hello")
```

---

# SECTION I — PRACTICAL PROGRAMMING (15 Marks)

### Question 40

Create a Student class with:

* name
* age

Add a method:

```python
display_info()
```

that displays student information.

---

### Question 41

Create a BankAccount class with:

* balance

Methods:

```python
deposit()
withdraw()
```

Update the balance appropriately.

---

### Question 42

Create an Employee class containing:

* name
* monthly_salary

Create a method:

```python
annual_salary()
```

that calculates annual salary.

---

### Question 43

Create a Vehicle class and a Car subclass.

Add a method:

```python
start()
```

Override the method in the Car class.

---

# SECTION J — STUDENT MANAGEMENT PROJECT (Bonus 10 Marks)

## Student Class System

Create a Student class that stores:

```python
name
score
```

Methods:

```python
calculate_grade()
display_student()
```

Grade Rules:

| Score    | Grade |
| -------- | ----- |
| 70+      | A     |
| 60-69    | B     |
| 50-59    | C     |
| Below 50 | F     |

---

# SECTION K — EMPLOYEE PAYROLL PROJECT

Create an Employee Payroll System.

Requirements:

### Employee Class

Attributes:

```python
name
salary
```

Methods:

```python
annual_salary()
tax()
net_salary()
```

Assume:

```text
Tax = 10% of Annual Salary
```

Display employee details and payroll summary.

---

# SECTION L — CAMBRIDGE A-LEVEL STYLE QUESTIONS

### Question 44

Explain the difference between instance attributes and class attributes.

---

### Question 45

Describe how inheritance improves software development.

---

### Question 46

Explain the purpose of getters and setters.

---

### Question 47

Describe polymorphism using a real-world example.

---

### Question 48

Compare composition and aggregation with examples.

---

# END-OF-MODULE CHALLENGE

## School Management System

Build a simple OOP-based school management system.

### Requirements

#### Student Class

```python
name
age
score
```

#### Teacher Class

```python
name
subject
```

#### School Class

Stores:

```python
students
teachers
```

Features:

* Add Student
* Add Teacher
* Display Students
* Display Teachers
* Calculate Student Grades

### Concepts to Demonstrate

✓ Classes

✓ Objects

✓ Constructors

✓ Methods

✓ Encapsulation

✓ Inheritance (optional)

✓ Composition

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

# End of Module 7 Assessment

