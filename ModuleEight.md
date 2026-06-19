
---

# Module 8: Advanced Object-Oriented Programming

![Advanced OOP](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+8:+Advanced+Object+Oriented+Programming)

---

# Learning Objectives

By the end of this module students should be able to:

✓ Understand advanced inheritance

✓ Apply polymorphism effectively

✓ Create abstract classes

✓ Design interfaces

✓ Use magic methods

✓ Overload operators

✓ Build enterprise-grade OOP applications

✓ Design banking systems using OOP

✓ Answer advanced OOP examination questions

---

# Chapter 1: Revisiting Inheritance

Before learning advanced inheritance, let's recap.

Inheritance allows one class to acquire features from another class.

Example:

```python
class Animal:

    def speak(self):
        print("Animal Sound")
```

```python
class Dog(Animal):
    pass
```

Dog automatically gets:

```python
speak()
```

---

# Why Inheritance Matters

Without inheritance:

```python
class Dog:
    ...
```

```python
class Cat:
    ...
```

```python
class Horse:
    ...
```

All classes repeat code.

Inheritance promotes:

✓ Reuse

✓ Maintainability

✓ Cleaner Design

---

# Types of Inheritance

Python supports several inheritance types.

---

# 1. Single Inheritance

One parent.

```text
Animal
   |
  Dog
```

Example:

```python
class Animal:

    def eat(self):
        print("Eating")
```

```python
class Dog(Animal):
    pass
```

---

# 2. Multilevel Inheritance

```text
Animal
   |
 Mammal
   |
  Dog
```

Example:

```python
class Animal:
    pass
```

```python
class Mammal(Animal):
    pass
```

```python
class Dog(Mammal):
    pass
```

---

# 3. Hierarchical Inheritance

One parent.

Many children.

```text
        Animal
       /      \
     Dog      Cat
```

---

# 4. Multiple Inheritance

One child.

Multiple parents.

```text
Flyer     Swimmer
    \       /
     Duck
```

Example:

```python
class Flyer:

    def fly(self):
        print("Flying")
```

```python
class Swimmer:

    def swim(self):
        print("Swimming")
```

```python
class Duck(
    Flyer,
    Swimmer
):
    pass
```

Usage:

```python
duck = Duck()

duck.fly()

duck.swim()
```

---

# Method Resolution Order (MRO)

Multiple inheritance introduces ambiguity.

Example:

```python
class A:

    def speak(self):
        print("A")
```

```python
class B:

    def speak(self):
        print("B")
```

```python
class C(A, B):
    pass
```

Usage:

```python
c = C()

c.speak()
```

Output:

```text
A
```

Python follows:

```python
C.mro()
```

to determine search order.

---

# Chapter 2: Advanced Polymorphism

## What is Polymorphism?

Polymorphism means:

```text
One Interface
Many Behaviors
```

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

# Real World Example

Payment System

```python
class CardPayment:
    def pay(self):
        print("Card Payment")
```

```python
class BankTransfer:
    def pay(self):
        print("Bank Transfer")
```

```python
class CryptoPayment:
    def pay(self):
        print("Crypto Payment")
```

Same method.

Different behavior.

---

# Duck Typing

Python uses:

```text
Behavior > Type
```

If it behaves correctly, Python accepts it.

---

Example:

```python
class Bird:

    def fly(self):
        print("Flying")
```

```python
class Airplane:

    def fly(self):
        print("Flying")
```

Both work.

Python doesn't care what they are.

Only that they have:

```python
fly()
```

---

# Chapter 3: Abstract Classes

## The Problem

Suppose every payment method must have:

```python
pay()
```

We want to force subclasses to implement it.

---

# ABC Module

ABC means:

```text
Abstract Base Class
```

---

Import:

```python
from abc import ABC
```

---

Abstract Class Example

```python
from abc import ABC
from abc import abstractmethod
```

```python
class Payment(ABC):

    @abstractmethod

    def pay(self):
        pass
```

---

Subclass:

```python
class CardPayment(
    Payment
):

    def pay(self):

        print(
            "Card Payment"
        )
```

---

Usage:

```python
payment = CardPayment()

payment.pay()
```

Output:

```text
Card Payment
```

---

# Why Abstract Classes?

They enforce structure.

Every subclass MUST implement:

```python
pay()
```

---

# Chapter 4: Interfaces

Python doesn't have traditional interfaces like Java.

Instead we use:

* Abstract Classes
* Duck Typing
* Protocols (Advanced)

---

Interface Concept

```text
All Vehicles Must:
   Start
   Stop
```

Example:

```python
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
```

---

# Chapter 5: Magic (Dunder) Methods

## What Are Dunder Methods?

Dunder means:

```text
Double Underscore
```

Examples:

```python
__init__

__str__

__len__

__add__
```

---

# Why They Matter

They define object behavior.

---

# **init**

Constructor.

```python
def __init__(self):
    pass
```

Already familiar.

---

# **str**

Controls printing.

Without:

```python
print(student)
```

Output:

```text
<__main__.Student object at 0x001>
```

---

With:

```python
class Student:

    def __str__(self):

        return "Student Object"
```

Output:

```text
Student Object
```

---

# **len**

Defines length.

```python
class Playlist:

    def __len__(self):

        return 10
```

Usage:

```python
playlist = Playlist()

print(
    len(playlist)
)
```

Output:

```text
10
```

---

# **repr**

Developer representation.

```python
def __repr__(self):
    return "Student('John')"
```

---

# Chapter 6: Operator Overloading

## What is Operator Overloading?

Giving operators new meaning.

---

Example:

Normal:

```python
5 + 3
```

Output:

```text
8
```

---

Custom Objects

```python
class Money:

    def __init__(
        self,
        amount
    ):
        self.amount = amount
```

---

Without overloading:

```python
m1 + m2
```

Error.

---

Using **add**

```python
class Money:

    def __init__(
        self,
        amount
    ):
        self.amount = amount

    def __add__(
        self,
        other
    ):

        return Money(
            self.amount +
            other.amount
        )
```

---

Usage:

```python
m1 = Money(100)

m2 = Money(50)

result = m1 + m2

print(result.amount)
```

Output:

```text
150
```

---

# Common Operator Methods

| Operator | Method      |
| -------- | ----------- |
| +        | **add**     |
| -        | **sub**     |
| *        | **mul**     |
| /        | **truediv** |
| ==       | **eq**      |
| <        | **lt**      |
| >        | **gt**      |
| len()    | **len**     |
| print()  | **str**     |

---

# Practical Project 1

## Banking System

Create:

```text
Account
```

Parent Class.

---

Attributes:

```python
account_number
owner
balance
```

Methods:

```python
deposit()

withdraw()

check_balance()
```

---

Subclass:

```text
SavingsAccount
```

Additional:

```python
interest_rate
```

---

Subclass:

```text
CurrentAccount
```

Additional:

```python
overdraft_limit
```

---

Transfer Feature

```python
transfer(
    target_account,
    amount
)
```

---

# Practical Project 2

## Advanced Banking System

Use:

✓ Inheritance

✓ Abstract Classes

✓ Polymorphism

✓ Dunder Methods

---

Example:

```python
class Account(
    ABC
):
```

```python
class SavingsAccount(
    Account
):
```

```python
class CurrentAccount(
    Account
):
```

---

# Practical Project 3

## Employee Payroll System 2.0

Parent:

```python
Employee
```

Children:

```python
Manager

Developer

Intern
```

Each overrides:

```python
calculate_salary()
```

Polymorphism:

```python
employees = [
    Manager(),
    Developer(),
    Intern()
]

for emp in employees:

    print(
        emp.calculate_salary()
    )
```

---

# Advanced OOP Examination Questions

### Theory

1. Differentiate between abstraction and encapsulation.
2. Explain polymorphism with examples.
3. Explain duck typing.
4. Explain operator overloading.
5. Explain MRO.
6. Differentiate composition and inheritance.
7. Explain abstract classes.
8. Explain interfaces in Python.

---

### Coding

1. Build a Shape hierarchy using abstract classes.
2. Build a banking system.
3. Create a custom Vector class using operator overloading.
4. Implement multiple inheritance.
5. Create custom objects supporting len().

---

# Common Beginner Mistakes

### Forgetting abstract methods

Wrong:

```python
class Dog(
    Animal
):
    pass
```

when Animal has required abstract methods.

---

### Misusing Multiple Inheritance

Use only when necessary.

Prefer composition when possible.

---

### Forgetting to return values in dunder methods

Wrong:

```python
def __str__(self):
    print("Hello")
```

Correct:

```python
def __str__(self):
    return "Hello"
```

---

# Module Summary

In this module we learned:

✓ Advanced Inheritance

✓ Multiple Inheritance

✓ MRO

✓ Polymorphism

✓ Duck Typing

✓ Abstract Classes

✓ Interfaces

✓ Magic Methods

✓ Dunder Methods

✓ Operator Overloading

✓ Banking Systems

✓ Enterprise OOP Design

✓ Advanced OOP Exam Preparation

This module prepares students for professional software architecture and is the bridge between beginner Python programming and real-world framework development such as Django, FastAPI, ERP systems, fintech applications, and enterprise software.

---

## Recommended Duration

