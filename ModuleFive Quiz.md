# Module 5 Assessment

## Functions & Functional Programming

### Instructions

* Answer all questions.
* Read each question carefully.
* Some questions may have more than one correct answer.
* Attempt all practical questions.
* Total Marks: 100
* Duration: 90 Minutes

---

# Learning Objectives Assessment

By the end of this assessment, students should be able to:

✓ Define and call functions

✓ Use parameters and return values

✓ Apply default and keyword arguments

✓ Understand local and global scope

✓ Use Python modules and imports

✓ Create lambda functions

✓ Use map(), filter(), and reduce()

✓ Write docstrings

✓ Apply type hints

✓ Understand decorators at a beginner level

✓ Build reusable utility functions

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (20 Marks)

### Question 1

What is the primary purpose of a function?

A. To create variables

B. To repeat code manually

C. To organize and reuse code

D. To create loops

**Answer:** C

---

### Question 2

Which keyword is used to define a function?

A. function

B. define

C. def

D. func

**Answer:** C

---

### Question 3

What is the output?

```python
def greet():
    print("Hello")

greet()
```

A. greet

B. Hello

C. Error

D. Nothing

**Answer:** B

---

### Question 4

What is a parameter?

A. A variable passed into a function

B. A return value

C. A loop

D. A module

**Answer:** A

---

### Question 5

What is the output?

```python
def add(a, b):
    return a + b

print(add(3, 2))
```

A. 32

B. 5

C. Error

D. add

**Answer:** B

---

### Question 6

Which keyword allows a function to send a value back?

A. print

B. output

C. return

D. send

**Answer:** C

---

### Question 7

Which argument type allows values to be specified by name?

A. Positional

B. Local

C. Keyword

D. Global

**Answer:** C

---

### Question 8

Which Python function creates an anonymous function?

A. lambda

B. map

C. filter

D. reduce

**Answer:** A

---

### Question 9

Which function is used to apply an operation to every item in a collection?

A. filter()

B. reduce()

C. map()

D. sort()

**Answer:** C

---

### Question 10

Which module contains the reduce() function?

A. math

B. functools

C. hashlib

D. turtle

**Answer:** B

---

# SECTION B — MULTIPLE SELECT QUESTIONS (15 Marks)

### Question 11

Select all valid function components.

☐ Function Name

☐ Parameters

☐ Return Value

☐ Body

☐ Database

**Answers**

✓ Function Name

✓ Parameters

✓ Return Value

✓ Body

---

### Question 12

Which are valid argument types?

☐ Positional Arguments

☐ Keyword Arguments

☐ Default Arguments

☐ Loop Arguments

**Answers**

✓ Positional Arguments

✓ Keyword Arguments

✓ Default Arguments

---

### Question 13

Select all valid import statements.

☐ import math

☐ from math import sqrt

☐ import math as m

☐ import*

**Answers**

✓ import math

✓ from math import sqrt

✓ import math as m

---

### Question 14

Which are examples of functional programming tools?

☐ map()

☐ filter()

☐ reduce()

☐ lambda

**Answers**

✓ map()

✓ filter()

✓ reduce()

✓ lambda

---

### Question 15

Which are benefits of functions?

☐ Reusability

☐ Cleaner Code

☐ Reduced Duplication

☐ Easier Maintenance

**Answers**

✓ Reusability

✓ Cleaner Code

✓ Reduced Duplication

✓ Easier Maintenance

---

# SECTION C — TRUE OR FALSE (10 Marks)

### Question 16

Functions help reduce code duplication.

☐ True

☐ False

**Answer:** True

---

### Question 17

A function must always return a value.

☐ True

☐ False

**Answer:** False

---

### Question 18

Variables created inside a function are usually local variables.

☐ True

☐ False

**Answer:** True

---

### Question 19

Lambda functions can be used with map().

☐ True

☐ False

**Answer:** True

---

### Question 20

The `__name__ == "__main__"` pattern controls module execution.

☐ True

☐ False

**Answer:** True

---

# SECTION D — FILL IN THE GAPS (15 Marks)

### Question 21

A reusable block of code is called a __________.

**Answer:** Function

---

### Question 22

The keyword used to create a function is __________.

**Answer:** def

---

### Question 23

The keyword used to send data back from a function is __________.

**Answer:** return

---

### Question 24

Variables defined inside a function belong to the __________ scope.

**Answer:** Local

---

### Question 25

The keyword used to modify a global variable is __________.

**Answer:** global

---

### Question 26

The keyword used to modify a variable in an enclosing scope is __________.

**Answer:** nonlocal

---

### Question 27

The module commonly used for mathematics is __________.

**Answer:** math

---

### Question 28

A function without a name is commonly called a __________ function.

**Answer:** Lambda

---

# SECTION E — MATCH THE FOLLOWING (10 Marks)

| Column A  | Column B                  |
| --------- | ------------------------- |
| def       | Define Function           |
| return    | Send Value Back           |
| lambda    | Anonymous Function        |
| map()     | Transform Data            |
| filter()  | Select Data               |
| reduce()  | Aggregate Data            |
| global    | Access Global Variable    |
| nonlocal  | Access Enclosing Variable |
| import    | Load Module               |
| Docstring | Function Documentation    |

---

# SECTION F — SHORT ANSWER QUESTIONS (10 Marks)

### Question 29

What is a function?

---

### Question 30

Explain the difference between a parameter and an argument.

---

### Question 31

Differentiate between local and global scope.

---

### Question 32

What is a module?

---

### Question 33

What is the purpose of a docstring?

---

# SECTION G — CODE READING (10 Marks)

### Question 34

Predict the output.

```python
def greet():
    return "Hello"

print(greet())
```

**Answer**

```text
Hello
```

---

### Question 35

Predict the output.

```python
def square(x):
    return x * x

print(square(4))
```

**Answer**

```text
16
```

---

### Question 36

Predict the output.

```python
double = lambda x: x * 2

print(double(5))
```

**Answer**

```text
10
```

---

### Question 37

Predict the output.

```python
numbers = [1, 2, 3]

result = map(
    lambda x: x * 2,
    numbers
)

print(list(result))
```

**Answer**

```python
[2, 4, 6]
```

---

# SECTION H — DEBUGGING QUESTIONS (5 Marks)

### Question 38

Identify the error.

```python
def greet()
    print("Hello")
```

**Answer**

Missing colon.

Correct:

```python
def greet():
    print("Hello")
```

---

### Question 39

Identify the error.

```python
def add(a, b):
    print(a + b)

result = add(2, 3)

print(result + 5)
```

**Answer**

add() returns None because it uses print instead of return.

Correct:

```python
def add(a, b):
    return a + b
```

---

# SECTION I — PRACTICAL PROGRAMMING (15 Marks)

### Question 40

Create a function called:

```python
calculate_area()
```

that calculates the area of a rectangle.

Formula:

```text
Area = Length × Width
```

---

### Question 41

Create a function called:

```python
is_even()
```

that returns True if a number is even and False otherwise.

---

### Question 42

Create a custom math module containing:

```python
add()
subtract()
multiply()
divide()
```

Import and use the module.

---

### Question 43

Create a function that counts the number of vowels in a string.

Example:

```text
Input:
Adewale

Output:
4
```

---

# SECTION J — PALINDROME CHALLENGE (Bonus 5 Marks)

A palindrome reads the same forward and backward.

Examples:

```text
madam
level
radar
```

### Question 44

Create a function called:

```python
is_palindrome()
```

that checks if a word is a palindrome.

---

### Question 45

Improve your palindrome checker so that:

```text
Madam
```

and

```text
madam
```

both return True.

---

### Question 46

Further improve the checker so that:

```text
A man a plan a canal Panama
```

returns True by ignoring spaces and capitalization.

---

# SECTION K — FIBONACCI CHALLENGE (Bonus 5 Marks)

### Question 47

Write a function that generates the first 10 Fibonacci numbers.

Expected Output:

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

### Question 48

Modify the function so that the user specifies how many Fibonacci numbers should be generated.

---

# SECTION L — PROFESSIONAL PYTHON QUESTIONS (Bonus 5 Marks)

### Question 49

Write a proper docstring for a function that calculates student averages.

---

### Question 50

Add type hints to the following function:

```python
def add(a, b):
    return a + b
```

Expected:

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

# END-OF-MODULE PROJECT

## Personal Utility Toolkit

Build a Python utility module containing:

### Mathematical Functions

* add()
* subtract()
* multiply()
* divide()

### String Functions

* reverse_text()
* count_vowels()
* is_palindrome()

### Number Functions

* is_even()
* fibonacci()

### Requirements

1. Use functions.
2. Use docstrings.
3. Use type hints.
4. Import functions from another file.
5. Demonstrate usage.

---

# Grading Guide

| Score    | Grade             |
| -------- | ----------------- |
| 90 - 100 | Excellent         |
| 80 - 89  | Very Good         |
| 70 - 79  | Good              |
| 60 - 69  | Fair              |
| Below 60 | Needs Improvement |

---

# End of Module 5 Assessment
