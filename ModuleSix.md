
---

# Module 6: File Handling & Data Persistence

![File Handling](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+6:+File+Handling+and+Data+Persistence)

---

# Learning Objectives

By the end of this module students should be able to:

✓ Read text files

✓ Write text files

✓ Append data to files

✓ Work with CSV files

✓ Work with JSON files

✓ Understand Pickle serialization

✓ Handle exceptions

✓ Use try, except, else and finally

✓ Build persistent applications

✓ Create a mini database using JSON

✓ Create a contact management system

---

# Chapter 1: Introduction to Data Persistence

## What is Data Persistence?

Data Persistence means storing information so that it remains available even after the program closes.

Example:

Without persistence:

```python
name = "John"
```

When program closes:

```text
Data Lost
```

With persistence:

```python
save_to_file("John")
```

When program closes:

```text
Data Saved
```

---

## Real World Examples

Every application uses persistence:

| Application   | Stored Data     |
| ------------- | --------------- |
| WhatsApp      | Messages        |
| Facebook      | Posts           |
| Banking Apps  | Transactions    |
| School Portal | Student Records |
| Contact App   | Phone Numbers   |

---

# Chapter 2: Reading and Writing Text Files

## What is a File?

A file is a collection of stored information.

Examples:

```text
notes.txt
students.txt
report.txt
```

---

# Opening Files

Syntax:

```python
open(filename, mode)
```

Example:

```python
file = open("students.txt", "r")
```

---

# Reading Files

Suppose:

```text
students.txt

John
Mary
Adewale
```

Code:

```python
file = open("students.txt", "r")

content = file.read()

print(content)

file.close()
```

Output:

```text
John
Mary
Adewale
```

---

# Why Close Files?

```python
file.close()
```

Releases system resources.

---

# Using with Statement (Recommended)

Instead of:

```python
file = open("data.txt")

content = file.read()

file.close()
```

Use:

```python
with open("data.txt") as file:

    content = file.read()

print(content)
```

Python closes the file automatically.

---

# Reading Line by Line

File:

```text
Apple
Banana
Orange
```

Code:

```python
with open("fruits.txt") as file:

    for line in file:

        print(line)
```

---

# read(), readline(), readlines()

### read()

Reads everything.

```python
file.read()
```

---

### readline()

Reads one line.

```python
file.readline()
```

---

### readlines()

Returns a list.

```python
file.readlines()
```

Output:

```python
[
 "Apple\n",
 "Banana\n",
 "Orange\n"
]
```

---

# Writing Files

Mode:

```python
w
```

Example:

```python
with open(
    "notes.txt",
    "w"
) as file:

    file.write(
        "Hello World"
    )
```

---

# Appending Data

Mode:

```python
a
```

Example:

```python
with open(
    "notes.txt",
    "a"
) as file:

    file.write(
        "\nNew Record"
    )
```

---

# File Modes

| Mode | Meaning      |
| ---- | ------------ |
| r    | Read         |
| w    | Write        |
| a    | Append       |
| x    | Create       |
| r+   | Read & Write |

---

# Chapter 3: Working with CSV Files

## What is CSV?

CSV means:

```text
Comma Separated Values
```

Example:

```csv
Name,Age,Department
John,20,Computer Science
Mary,21,Engineering
```

---

# Why CSV?

Used by:

* Excel
* Google Sheets
* Databases
* Reporting Systems

---

# Reading CSV

```python
import csv

with open("students.csv") as file:

    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```python
['Name', 'Age']
['John', '20']
['Mary', '21']
```

---

# CSV DictReader

```python
import csv

with open("students.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"])
```

---

# Writing CSV

```python
import csv

with open(
    "students.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Name", "Age"]
    )

    writer.writerow(
        ["John", 20]
    )
```

---

# Chapter 4: Working with JSON

## What is JSON?

JSON means:

```text
JavaScript Object Notation
```

JSON is the most common data exchange format in the world.

Used by:

* APIs
* Mobile Apps
* Websites
* Databases

---

# JSON Example

```json
{
    "name": "John",
    "age": 20,
    "department": "Computer Science"
}
```

---

# Python Dictionary Equivalent

```python
student = {
    "name": "John",
    "age": 20,
    "department": "Computer Science"
}
```

Notice the similarity.

---

# Saving JSON

```python
import json

student = {
    "name": "John",
    "age": 20
}

with open(
    "student.json",
    "w"
) as file:

    json.dump(
        student,
        file,
        indent=4
    )
```

---

# Reading JSON

```python
import json

with open(
    "student.json"
) as file:

    data = json.load(file)

print(data)
```

---

# JSON vs CSV

| JSON               | CSV           |
| ------------------ | ------------- |
| Nested Data        | Flat Data     |
| APIs               | Spreadsheets  |
| Complex Structures | Simple Tables |

---

# Chapter 5: Pickle

## What is Pickle?

Pickle allows Python objects to be saved directly.

Example:

```python
students = [
    "John",
    "Mary",
    "Adewale"
]
```

Save it exactly as it is.

---

# Saving with Pickle

```python
import pickle

students = [
    "John",
    "Mary"
]

with open(
    "students.pkl",
    "wb"
) as file:

    pickle.dump(
        students,
        file
    )
```

---

# Loading Pickle Data

```python
import pickle

with open(
    "students.pkl",
    "rb"
) as file:

    data = pickle.load(
        file
    )

print(data)
```

Output:

```python
['John', 'Mary']
```

---

# When to Use Pickle

Good:

* Python-only applications
* Saving program state
* Caching

Not ideal for:

* Data exchange between systems

Use JSON instead.

---

# Chapter 6: Exception Handling

## What is an Exception?

An exception is an error that occurs while the program is running.

Example:

```python
print(10 / 0)
```

Output:

```text
ZeroDivisionError
```

Program crashes.

---

# try and except

```python
try:

    print(10 / 0)

except:

    print(
        "Something went wrong"
    )
```

Output:

```text
Something went wrong
```

---

# Catching Specific Errors

```python
try:

    age = int(
        input("Age:")
    )

except ValueError:

    print(
        "Enter a valid number"
    )
```

---

# Multiple Exceptions

```python
try:

    number = int(input())

    result = 10 / number

except ValueError:

    print("Invalid Number")

except ZeroDivisionError:

    print("Cannot divide by zero")
```

---

# else Block

Runs if no exception occurs.

```python
try:

    age = int(input())

except ValueError:

    print("Invalid")

else:

    print("Success")
```

---

# finally Block

Always runs.

```python
try:

    print("Running")

finally:

    print("Finished")
```

Output:

```text
Running
Finished
```

---

# Exception Flow Diagram

```text
Try Block
     |
     v
Error?
 /      \
Yes      No
 |         |
Except    Else
     \   /
    Finally
```

---

# Practical 1: Mini Database Using JSON

Store student records:

```json
[
    {
        "name":"John",
        "age":20
    },
    {
        "name":"Mary",
        "age":21
    }
]
```

Features:

* Add Student
* View Students
* Save Automatically

---

# Practical 2: Contact Management System

Store:

```json
{
    "John":"08012345678",
    "Mary":"08098765432"
}
```

Functions:

* Add Contact
* Search Contact
* Delete Contact
* Update Contact
* Save to JSON

---

# Practical Project: Student Registration System

Features:

### Add Student

```text
Name
Age
Department
```

### Save Data

Using JSON.

### Read Data

Display all students.

### Error Handling

Use:

```python
try
except
```

to validate input.

---

# Real-World Example

Without Error Handling:

```python
age = int(input())
```

User enters:

```text
abc
```

Program crashes.

---

With Error Handling:

```python
try:

    age = int(input())

except ValueError:

    print(
        "Invalid age"
    )
```

Program survives.

---

# Best Practices

✓ Always use `with open()` for files

✓ Use JSON for structured data

✓ Use CSV for spreadsheet-like data

✓ Use Pickle for Python-only objects

✓ Handle exceptions gracefully

✓ Catch specific exceptions where possible

✓ Use finally for cleanup operations

---

# Module Summary

In this module we learned:

✓ Reading Files

✓ Writing Files

✓ Appending Files

✓ CSV Files

✓ JSON Files

✓ Pickle Serialization

✓ try

✓ except

✓ else

✓ finally

✓ Data Persistence

✓ Contact Management Systems

✓ Mini JSON Databases

✓ Error Handling

This module is important because it teaches students how to build applications that can save, retrieve, and protect data—an essential skill for web development, automation, data science, and software engineering.

---
