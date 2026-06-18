# Module 3: Control Flow

![Control Flow](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+3:+Control+Flow)

## Introduction

So far, our programs have followed a straight path.

Example:

```python
name = input("Enter your name: ")

print(name)

print("Welcome")
```

Python executes this line by line.

But real-world applications need to make decisions.

For example:

* If the password is correct → Login
* If the student passes → Display "Pass"
* If the account balance is enough → Allow withdrawal

This ability to make decisions is called **Control Flow**.

Control Flow determines:

* Which code should run
* When it should run
* How many times it should run

---

# Learning Objectives

By the end of this module, students should be able to:

✓ Use if statements

✓ Use if-else statements

✓ Use if-elif-else structures

✓ Create nested conditions

✓ Use logical operators

✓ Write for loops

✓ Write while loops

✓ Use break

✓ Use continue

✓ Use pass

✓ Build practical Python programs

---

# 1. Understanding Control Flow

![Flowchart](https://placehold.co/1000x400/1f2937/ffffff.png?text=Decision+Making+Flowchart)

Imagine a traffic light.

```text
IF Light is Green
    Move
ELSE
    Stop
```

The action depends on a condition.

Python works exactly the same way.

---

# 2. If Statements

## What is an If Statement?

An if statement allows Python to execute code only when a condition is true.

Syntax:

```python
if condition:
    code
```

Example:

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

Output:

```text
You are an adult.
```

Because:

```text
20 >= 18
```

is True.

---

## Example 2

```python
score = 80

if score >= 50:
    print("You passed.")
```

Output:

```text
You passed.
```

---

## Important Rule

Indentation matters.

Correct:

```python
if score >= 50:
    print("Passed")
```

Wrong:

```python
if score >= 50:
print("Passed")
```

Python will raise:

```text
IndentationError
```

---

# 3. If-Else Statements

Sometimes we want Python to perform one action if a condition is true and another action if it is false.

Syntax:

```python
if condition:
    code
else:
    code
```

Example:

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

---

## Real Life Example

ATM Withdrawal

```python
balance = 5000
withdrawal = 8000

if balance >= withdrawal:
    print("Withdrawal Successful")
else:
    print("Insufficient Funds")
```

Output:

```text
Insufficient Funds
```

---

# 4. If-Elif-Else Statements

What if we have multiple conditions?

Syntax:

```python
if condition:
    code

elif condition:
    code

else:
    code
```

---

## Example

```python
score = 75

if score >= 70:
    print("A")

elif score >= 60:
    print("B")

elif score >= 50:
    print("C")

else:
    print("Fail")
```

Output:

```text
A
```

---

# Flow Illustration

```text
Score = 75

Is score >= 70?
       |
      Yes
       |
       A
```

Python stops checking after the first True condition.

---

# 5. Nested Conditions

Nested means placing one condition inside another.

Example:

```python
age = 25
citizen = True

if age >= 18:

    if citizen:
        print("Eligible to Vote")
```

Output:

```text
Eligible to Vote
```

---

## Real-Life Example

University Admission

```python
score = 250
has_credits = True

if score >= 200:

    if has_credits:
        print("Admission Possible")
```

---

## Visual Illustration

```text
Score >= 200?
      |
     Yes
      |
Credits Available?
      |
     Yes
      |
Admission Possible
```

---

# 6. Logical Operators

Logical operators combine multiple conditions.

There are three main logical operators:

| Operator | Meaning           |
| -------- | ----------------- |
| and      | Both must be True |
| or       | One must be True  |
| not      | Reverse result    |

---

# AND Operator

Example:

```python
age = 25
citizen = True

if age >= 18 and citizen:
    print("Can Vote")
```

Output:

```text
Can Vote
```

---

## AND Truth Table

| Condition A | Condition B | Result |
| ----------- | ----------- | ------ |
| True        | True        | True   |
| True        | False       | False  |
| False       | True        | False  |
| False       | False       | False  |

---

# OR Operator

Example:

```python
role = "Admin"

if role == "Admin" or role == "Manager":
    print("Access Granted")
```

Output:

```text
Access Granted
```

---

# NOT Operator

Example:

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

Output:

```text
Please Login"
```

---

# 7. For Loops

## What is a Loop?

A loop repeats code.

Example:

Instead of:

```python
print("Python")
print("Python")
print("Python")
```

We can write:

```python
for i in range(3):
    print("Python")
```

Output:

```text
Python
Python
Python
```

---

# Understanding range()

```python
range(5)
```

Generates:

```text
0 1 2 3 4
```

---

## Example

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

---

# Range with Start and End

```python
for number in range(1, 6):
    print(number)
```

Output:

```text
1
2
3
4
5
```

---

# Range with Step

```python
for number in range(0, 11, 2):
    print(number)
```

Output:

```text
0
2
4
6
8
10
```

---

# Looping Through Strings

```python
name = "Python"

for letter in name:
    print(letter)
```

Output:

```text
P
y
t
h
o
n
```

---

# 8. While Loops

A while loop continues running while a condition remains True.

Syntax:

```python
while condition:
    code
```

---

## Example

```python
count = 1

while count <= 5:
    print(count)

    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# Infinite Loop Warning

This is dangerous:

```python
while True:
    print("Hello")
```

The loop never stops.

Always make sure the condition can eventually become False.

---

# 9. Break Statement

Break immediately stops a loop.

Example:

```python
for number in range(10):

    if number == 5:
        break

    print(number)
```

Output:

```text
0
1
2
3
4
```

Loop stops at 5.

---

# 10. Continue Statement

Continue skips the current iteration.

Example:

```python
for number in range(5):

    if number == 2:
        continue

    print(number)
```

Output:

```text
0
1
3
4
```

2 is skipped.

---

# 11. Pass Statement

Pass does nothing.

Example:

```python
for number in range(5):

    if number == 3:
        pass

    print(number)
```

Used when planning future code.

---

# Practical 1: Student Grade Checker

```python
score = int(input("Enter score: "))

if score >= 70:
    print("Grade A")

elif score >= 60:
    print("Grade B")

elif score >= 50:
    print("Grade C")

else:
    print("Fail")
```

---

# Practical 2: Multiplication Table Generator

```python
number = int(input("Enter a number: "))

for i in range(1, 13):

    print(f"{number} x {i} = {number * i}")
```

---

# Practical 3: Number Guessing Game

```python
secret = 7

guess = int(input("Guess a number: "))

if guess == secret:
    print("Correct!")

else:
    print("Wrong!")
```

---

# Improved Number Guessing Game

```python
secret = 7

while True:

    guess = int(input("Guess a number: "))

    if guess == secret:
        print("Correct!")
        break

    print("Try Again")
```

---

# Mini Project: ATM Simulator

```python
balance = 10000

withdrawal = int(
    input("Enter amount: ")
)

if withdrawal <= balance:

    balance -= withdrawal

    print("Successful")

    print(
        f"Balance: {balance}"
    )

else:
    print("Insufficient Funds")
```

---

# Common Beginner Mistakes

### Forgetting Colon

Wrong:

```python
if score > 50
```

Correct:

```python
if score > 50:
```

---

### Wrong Indentation

Wrong:

```python
if score > 50:
print("Pass")
```

Correct:

```python
if score > 50:
    print("Pass")
```

---

### Infinite While Loop

Wrong:

```python
count = 1

while count <= 5:
    print(count)
```

Correct:

```python
count = 1

while count <= 5:
    print(count)

    count += 1
```

---

# End-of-Module Challenge

Build a Student Portal that:

1. Accepts student name.
2. Accepts score.
3. Determines grade.
4. Displays Pass/Fail.
5. Allows repeated entries using a loop.
6. Stops when user enters "quit".

---

# Module Summary

In this module we learned:

✓ If Statements

✓ If-Else Statements

✓ If-Elif-Else Statements

✓ Nested Conditions

✓ Logical Operators

✓ For Loops

✓ While Loops

✓ Break

✓ Continue

✓ Pass

✓ Student Grade Checker

✓ Multiplication Table Generator

✓ Number Guessing Game

