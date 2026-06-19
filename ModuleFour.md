
---

# Module 4 Comprehensive Note Structure

Below is the style I would use for the actual note.

---

# Module 4: Collections (Data Structures)

![Collections](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+4:+Collections+and+Data+Structures)

---

# Learning Objectives

By the end of this module students should be able to:

✓ Create and manipulate lists

✓ Use tuples effectively

✓ Store data using dictionaries

✓ Work with sets

✓ Understand mutability

✓ Use list comprehensions

✓ Build real-world data models

✓ Understand basic Big-O concepts

✓ Explain hash tables

✓ Build practical collection-based applications

---

# 1. Introduction to Data Structures

## What is a Data Structure?

A data structure is a way of organizing and storing data so that it can be used efficiently.

Imagine a school.

You have:

* Student names
* Scores
* Departments
* Courses

You need a way to organize this information.

Python provides several built-in data structures.

```text
Data Structures
│
├── List
├── Tuple
├── Dictionary
└── Set
```

---

# 2. Lists in Python

![Lists](https://placehold.co/1000x400/1f2937/ffffff.png?text=Lists+Store+Multiple+Values)

A list is an ordered collection of items.

Example:

```python
students = [
    "John",
    "Mary",
    "Adewale"
]
```

---

## Why Lists?

Without Lists:

```python
student1 = "John"
student2 = "Mary"
student3 = "Adewale"
```

With Lists:

```python
students = [
    "John",
    "Mary",
    "Adewale"
]
```

Much easier.

---

## Accessing List Items

```python
students = [
    "John",
    "Mary",
    "Adewale"
]

print(students[0])
```

Output:

```text
John
```

---

## Negative Indexing

```python
print(students[-1])
```

Output:

```text
Adewale
```

---

# List Slicing

```python
students = [
    "John",
    "Mary",
    "Adewale",
    "Grace"
]

print(students[1:3])
```

Output:

```python
['Mary', 'Adewale']
```

---

# List Mutability

Lists are mutable.

Meaning:

You can change them.

```python
students = [
    "John",
    "Mary"
]

students[0] = "James"

print(students)
```

Output:

```python
['James', 'Mary']
```

---

# Adding Items

## append()

```python
students.append("Adewale")
```

---

## insert()

```python
students.insert(1, "Grace")
```

---

## extend()

```python
students.extend([
    "Tolu",
    "David"
])
```

---

# Removing Items

## remove()

```python
students.remove("Mary")
```

---

## pop()

```python
students.pop()
```

---

## clear()

```python
students.clear()
```

---

# Sorting Lists

```python
numbers = [5, 2, 7, 1]

numbers.sort()

print(numbers)
```

Output:

```python
[1, 2, 5, 7]
```

---

# List Comprehensions

One of Python's most powerful features.

Traditional:

```python
squares = []

for x in range(5):
    squares.append(x * x)
```

Pythonic:

```python
squares = [
    x * x
    for x in range(5)
]
```

Output:

```python
[0,1,4,9,16]
```

---

# Lists FAQ

### Are lists ordered?

Yes.

### Can lists contain different data types?

Yes.

```python
data = [
    "John",
    25,
    True
]
```

### Are lists mutable?

Yes.

---

# Lists Quiz

1. What symbol creates a list?
2. What method adds an item?
3. What method removes an item?
4. Are lists mutable?

---

# 3. Dictionaries

![Dictionary](https://placehold.co/1000x400/1f2937/ffffff.png?text=Dictionary+Key+Value+Storage)

A dictionary stores data as key-value pairs.

Example:

```python
student = {
    "name": "Adewale",
    "age": 25,
    "score": 90
}
```

---

## Accessing Values

```python
print(student["name"])
```

Output:

```text
Adewale
```

---

## Using get()

```python
print(
    student.get("name")
)
```

Safer than square brackets.

---

## Adding Items

```python
student["department"] = "Computer Science"
```

---

## Updating Values

```python
student["score"] = 95
```

---

## Deleting Items

```python
del student["age"]
```

or

```python
student.pop("age")
```

---

# Iterating Dictionaries

```python
for key in student:
    print(key)
```

---

```python
for value in student.values():
    print(value)
```

---

```python
for key, value in student.items():
    print(key, value)
```

---

# Nested Dictionaries

```python
students = {
    "student1": {
        "name": "John",
        "score": 80
    }
}
```

---

# Smart Fridge Example

```python
fridge = {
    "Milk": 2,
    "Eggs": 12,
    "Butter": 1
}
```

---

# Meal Planner Example

```python
recipes = {
    "Jollof Rice": [
        "Rice",
        "Tomatoes",
        "Pepper"
    ]
}
```

---

# Frequency Counter

```python
word = "banana"

freq = {}

for letter in word:

    freq[letter] = (
        freq.get(letter, 0)
        + 1
    )

print(freq)
```

Output:

```python
{
 'b':1,
 'a':3,
 'n':2
}
```

---

# Mutable Objects

```python
student1 = {
    "name":"John"
}

student2 = student1

student2["name"] = "Mary"
```

Now BOTH change.

Why?

Because both variables reference the same object.

---

# Shallow Copy

```python
student2 = student1.copy()
```

Creates a separate dictionary.

---

# Deep Copy

```python
import copy

student2 = copy.deepcopy(
    student1
)
```

Used for nested structures.

---

# Hash Tables

Dictionaries are implemented using hash tables.

```text
Key
 ↓
Hash Function
 ↓
Storage Location
```

This makes lookups extremely fast.

---

# Hash Example

```python
print(hash("John"))
```

---

# hashlib

```python
import hashlib

password = "admin123"

hashed = hashlib.sha256(
    password.encode()
).hexdigest()

print(hashed)
```

---

# 4. Tuples

![Tuple](https://placehold.co/1000x400/1f2937/ffffff.png?text=Tuple+Immutable+Collection)

Tuples are ordered collections that cannot be changed.

```python
coordinates = (
    10,
    20
)
```

---

## Tuple vs List

| List    | Tuple     |
| ------- | --------- |
| Mutable | Immutable |
| []      | ()        |

---

## Tuple Unpacking

```python
x, y = (
    10,
    20
)
```

---

# 5. Sets

![Sets](https://placehold.co/1000x400/1f2937/ffffff.png?text=Sets+Unique+Values)

A set stores unique values.

```python
numbers = {
    1,2,2,3
}

print(numbers)
```

Output:

```python
{1,2,3}
```

---

# Membership Testing

```python
if "John" in students:
    print("Found")
```

Sets are extremely fast for this.

---

# Set Operations

## Union

```python
A | B
```

or

```python
A.union(B)
```

---

## Intersection

```python
A & B
```

---

## Difference

```python
A - B
```

---

## Symmetric Difference

```python
A ^ B
```

---

# Real World Example

Applicants:

```python
python_skills = {
    "John",
    "Mary"
}

django_skills = {
    "Mary",
    "Grace"
}
```

Intersection:

```python
{
 "Mary"
}
```

---

# Stacks & Queues

## Stack

Last In First Out

```text
Plate Stack
```

Python:

```python
stack = []

stack.append(1)

stack.pop()
```

---

## Queue

First In First Out

```text
Bank Queue
```

Using:

```python
from collections import deque
```

---

# Big O Basics

| Operation | List | Set  | Dict |
| --------- | ---- | ---- | ---- |
| Search    | O(n) | O(1) | O(1) |
| Insert    | O(1) | O(1) | O(1) |
| Delete    | O(n) | O(1) | O(1) |

Beginner takeaway:

Sets and dictionaries are usually much faster for searching than lists.

---

# Practical 1: Frequency Counter

Count character occurrences.

Input:

```text
banana
```

Output:

```python
{
 'b':1,
 'a':3,
 'n':2
}
```

---

# Practical 2: Phonebook App

Store:

```python
{
 "John":"08012345678",
 "Mary":"08087654321"
}
```

Allow:

* Add contact
* Search contact
* Delete contact

---

# Practical 3: Cambridge A-Level Structure Questions

1. Differentiate between List and Tuple.
2. Differentiate between Set and Dictionary.
3. Explain mutability.
4. Explain shallow copy.
5. Explain deep copy.
6. Explain Big O.
7. Explain hash tables.

---

# Module Summary

In this module we learned:

✓ Lists

✓ Dictionaries

✓ Tuples

✓ Sets

✓ List Comprehensions

✓ Frequency Counting

✓ Hash Tables

✓ Mutable Objects

✓ Shallow Copy

✓ Deep Copy

✓ Stacks

✓ Queues

✓ Big O Basics

These are the foundational data structures used in almost every Python application, from web development and data science to cybersecurity and artificial intelligence.

```
