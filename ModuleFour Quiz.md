# Module 4 Assessment

## Collections (Data Structures)

### Instructions

* Answer all questions.
* Read every question carefully.
* Some questions may have more than one correct answer.
* Attempt all practical questions.
* Total Marks: 100
* Duration: 90 Minutes

---

# Learning Objectives Assessment

By the end of this assessment, students should be able to:

✓ Create and manipulate lists

✓ Use list slicing and comprehensions

✓ Create and work with dictionaries

✓ Store data using tuples

✓ Perform set operations

✓ Understand mutability

✓ Explain shallow and deep copying

✓ Understand hash tables and hashing concepts

✓ Use stacks and queues

✓ Explain basic Big-O performance concepts

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (20 Marks)

### Question 1

Which data structure uses square brackets?

A. Tuple

B. Dictionary

C. List

D. Set

**Answer:** C

---

### Question 2

Which data structure stores data as key-value pairs?

A. List

B. Dictionary

C. Tuple

D. Set

**Answer:** B

---

### Question 3

Which data structure stores only unique values?

A. List

B. Tuple

C. Dictionary

D. Set

**Answer:** D

---

### Question 4

Which of the following is immutable?

A. List

B. Dictionary

C. Tuple

D. Set

**Answer:** C

---

### Question 5

What is the output?

```python
numbers = [1, 2, 3]
print(numbers[1])
```

A. 1

B. 2

C. 3

D. Error

**Answer:** B

---

### Question 6

What does `append()` do?

A. Removes an item

B. Sorts a list

C. Adds an item to a list

D. Copies a list

**Answer:** C

---

### Question 7

What is the output?

```python
numbers = [1, 2, 2, 3]
print(set(numbers))
```

A.

```text
[1, 2, 2, 3]
```

B.

```text
{1, 2, 3}
```

C.

```text
(1, 2, 2, 3)
```

D. Error

**Answer:** B

---

### Question 8

Which method removes an item from a dictionary and returns its value?

A. remove()

B. delete()

C. pop()

D. clear()

**Answer:** C

---

### Question 9

Which collection is best for checking membership quickly?

A. List

B. Set

C. String

D. Tuple

**Answer:** B

---

### Question 10

What does SHA-256 generate?

A. A list

B. A tuple

C. A hash value

D. A dictionary

**Answer:** C

---

# SECTION B — MULTIPLE SELECT QUESTIONS (15 Marks)

### Question 11

Select all mutable data structures.

☐ List

☐ Dictionary

☐ Set

☐ Tuple

**Answers**

✓ List

✓ Dictionary

✓ Set

---

### Question 12

Which methods are commonly used with lists?

☐ append()

☐ remove()

☐ pop()

☐ insert()

☐ hash()

**Answers**

✓ append()

✓ remove()

✓ pop()

✓ insert()

---

### Question 13

Select valid dictionary methods.

☐ get()

☐ keys()

☐ values()

☐ items()

☐ reverse()

**Answers**

✓ get()

✓ keys()

✓ values()

✓ items()

---

### Question 14

Select all valid set operations.

☐ Union

☐ Intersection

☐ Difference

☐ Symmetric Difference

☐ Compilation

**Answers**

✓ Union

✓ Intersection

✓ Difference

✓ Symmetric Difference

---

### Question 15

Which are real-world uses of dictionaries?

☐ Phonebook

☐ Inventory System

☐ Student Records

☐ Shopping Cart

☐ Password Storage

**Answers**

✓ Phonebook

✓ Inventory System

✓ Student Records

✓ Shopping Cart

✓ Password Storage

---

# SECTION C — TRUE OR FALSE (10 Marks)

### Question 16

Lists maintain order.

☐ True

☐ False

**Answer:** True

---

### Question 17

Tuples can be modified after creation.

☐ True

☐ False

**Answer:** False

---

### Question 18

Sets allow duplicate values.

☐ True

☐ False

**Answer:** False

---

### Question 19

Dictionaries store data using keys and values.

☐ True

☐ False

**Answer:** True

---

### Question 20

Hash tables make dictionary lookups very fast.

☐ True

☐ False

**Answer:** True

---

# SECTION D — FILL IN THE GAPS (15 Marks)

### Question 21

A __________ stores multiple values in order.

**Answer:** List

---

### Question 22

A __________ stores key-value pairs.

**Answer:** Dictionary

---

### Question 23

A __________ stores unique values.

**Answer:** Set

---

### Question 24

A __________ cannot be modified after creation.

**Answer:** Tuple

---

### Question 25

The method used to add an item to a list is __________.

**Answer:** append()

---

### Question 26

The method used to retrieve dictionary values safely is __________.

**Answer:** get()

---

### Question 27

A __________ copy duplicates nested objects completely.

**Answer:** Deep

---

### Question 28

The Python module used for cryptographic hashes is __________.

**Answer:** hashlib

---

# SECTION E — MATCH THE FOLLOWING (10 Marks)

| Column A   | Column B             |
| ---------- | -------------------- |
| List       | Ordered Collection   |
| Dictionary | Key-Value Storage    |
| Tuple      | Immutable Collection |
| Set        | Unique Items         |
| append()   | Add Item             |
| pop()      | Remove Item          |
| get()      | Retrieve Value       |
| union()    | Combine Sets         |
| deepcopy() | Independent Copy     |
| hashlib    | Hash Generation      |

---

# SECTION F — SHORT ANSWER QUESTIONS (10 Marks)

### Question 29

What is a data structure?

---

### Question 30

Differentiate between a list and a tuple.

---

### Question 31

What is the difference between a dictionary and a set?

---

### Question 32

Explain mutability in Python.

---

### Question 33

What is the purpose of hashing?

---

# SECTION G — CODE READING (10 Marks)

### Question 34

Predict the output.

```python
students = [
    "John",
    "Mary",
    "Adewale"
]

print(students[2])
```

**Answer**

```text
Adewale
```

---

### Question 35

Predict the output.

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

**Answer**

```python
[1, 2, 3, 4]
```

---

### Question 36

Predict the output.

```python
student = {
    "name": "John",
    "age": 20
}

print(student["name"])
```

**Answer**

```text
John
```

---

### Question 37

Predict the output.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)
```

**Answer**

```python
{3}
```

---

# SECTION H — DEBUGGING QUESTIONS (5 Marks)

### Question 38

Find the error.

```python
students = [
    "John",
    "Mary"
)

print(students)
```

**Answer**

Incorrect closing bracket.

Correct:

```python
students = [
    "John",
    "Mary"
]
```

---

### Question 39

Find the error.

```python
student = {
    "name": "John"
}

print(student[name])
```

**Answer**

`name` should be a string key.

Correct:

```python
print(student["name"])
```

---

# SECTION I — PRACTICAL PROGRAMMING (15 Marks)

### Question 40

Create a list of five student names and display the third student.

---

### Question 41

Create a dictionary that stores:

* Name
* Age
* Department

Display all values.

---

### Question 42

Create a set containing:

```text
1, 2, 2, 3, 4, 4, 5
```

Display the result and explain what happened.

---

### Question 43

Write a program that counts how many times each letter appears in:

```text
banana
```

Expected Output:

```python
{
    "b": 1,
    "a": 3,
    "n": 2
}
```

---

# SECTION J — MINI PROJECT (Bonus 10 Marks)

## Phonebook Application

Build a phonebook using a dictionary.

Requirements:

1. Store names and phone numbers.
2. Allow users to:

   * Add contact
   * Search contact
   * Delete contact
3. Display all contacts.

Example:

```python
{
    "John": "08012345678",
    "Mary": "08098765432"
}
```

---

# SECTION K — CAMBRIDGE A-LEVEL STYLE QUESTIONS

### Question 44

Explain three differences between Lists and Tuples.

---

### Question 45

Explain how Sets help remove duplicates from data.

---

### Question 46

Describe the role of Dictionaries in storing real-world data.

---

### Question 47

Explain the difference between shallow copy and deep copy.

---

### Question 48

Why are Dictionaries generally faster than Lists for searching?

---

# END-OF-MODULE CHALLENGE

## Smart Fridge Inventory System

Create a dictionary-based inventory system that:

* Stores food items and quantities.
* Allows adding new items.
* Allows updating quantities.
* Checks if ingredients exist.
* Generates a shopping list for missing ingredients.

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

# End of Module 4 Assessment

