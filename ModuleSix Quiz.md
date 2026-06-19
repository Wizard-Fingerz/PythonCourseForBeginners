# Module 6 Assessment

## File Handling & Data Persistence

### Instructions

* Answer all questions.
* Read each question carefully.
* Attempt all practical questions.
* Some questions may have more than one correct answer.
* Total Marks: 100
* Duration: 90 Minutes

---

# Learning Objectives Assessment

By the end of this assessment, students should be able to:

✓ Read and write text files

✓ Use Python file modes correctly

✓ Work with CSV files

✓ Work with JSON files

✓ Understand Pickle serialization

✓ Handle exceptions using try, except, else, and finally

✓ Build applications that save and retrieve data

✓ Create JSON-based mini databases

✓ Build a contact management system

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (20 Marks)

### Question 1

What is data persistence?

A. Deleting files

B. Storing data permanently for future use

C. Running a program

D. Creating variables

**Answer:** B

---

### Question 2

Which function is used to open a file?

A. read()

B. file()

C. open()

D. write()

**Answer:** C

---

### Question 3

Which file mode is used for reading?

A. w

B. a

C. r

D. x

**Answer:** C

---

### Question 4

Which file mode is used for appending data?

A. r

B. a

C. w

D. x

**Answer:** B

---

### Question 5

What is the output of:

```python
with open("file.txt", "w") as file:
    file.write("Hello")
```

A. Reads a file

B. Deletes a file

C. Writes "Hello" to a file

D. Creates a list

**Answer:** C

---

### Question 6

What does CSV stand for?

A. Computer Saved Values

B. Comma Separated Values

C. Central Storage Values

D. Common Separated Variables

**Answer:** B

---

### Question 7

What does JSON stand for?

A. Java Storage Object Notation

B. JavaScript Object Notation

C. JSON Structured Output Network

D. Java Syntax Object Notation

**Answer:** B

---

### Question 8

Which Python module is used for JSON?

A. csv

B. pickle

C. json

D. file

**Answer:** C

---

### Question 9

Which module is used for Python object serialization?

A. json

B. csv

C. pickle

D. os

**Answer:** C

---

### Question 10

Which keyword starts exception handling?

A. catch

B. try

C. error

D. handle

**Answer:** B

---

# SECTION B — MULTIPLE SELECT QUESTIONS (15 Marks)

### Question 11

Select all valid file modes.

☐ r

☐ w

☐ a

☐ x

☐ save

**Answers**

✓ r

✓ w

✓ a

✓ x

---

### Question 12

Which methods are used to read file contents?

☐ read()

☐ readline()

☐ readlines()

☐ open()

**Answers**

✓ read()

✓ readline()

✓ readlines()

---

### Question 13

Which modules are used for data persistence?

☐ csv

☐ json

☐ pickle

☐ math

**Answers**

✓ csv

✓ json

✓ pickle

---

### Question 14

Which blocks belong to exception handling?

☐ try

☐ except

☐ else

☐ finally

☐ catch

**Answers**

✓ try

✓ except

✓ else

✓ finally

---

### Question 15

Which applications require persistent storage?

☐ Banking System

☐ School Portal

☐ Contact App

☐ Student Database

**Answers**

✓ Banking System

✓ School Portal

✓ Contact App

✓ Student Database

---

# SECTION C — TRUE OR FALSE (10 Marks)

### Question 16

Files allow data to remain after a program closes.

☐ True

☐ False

**Answer:** True

---

### Question 17

JSON data is usually stored as key-value pairs.

☐ True

☐ False

**Answer:** True

---

### Question 18

CSV files are commonly used in spreadsheets.

☐ True

☐ False

**Answer:** True

---

### Question 19

Pickle files can store Python objects directly.

☐ True

☐ False

**Answer:** True

---

### Question 20

finally only executes when an error occurs.

☐ True

☐ False

**Answer:** False

---

# SECTION D — FILL IN THE GAPS (15 Marks)

### Question 21

The function used to open files is __________.

**Answer:** open()

---

### Question 22

The mode used for reading files is __________.

**Answer:** r

---

### Question 23

The mode used for appending data is __________.

**Answer:** a

---

### Question 24

CSV stands for __________.

**Answer:** Comma Separated Values

---

### Question 25

JSON stands for __________.

**Answer:** JavaScript Object Notation

---

### Question 26

The module used for JSON operations is __________.

**Answer:** json

---

### Question 27

The keyword used to handle exceptions is __________.

**Answer:** except

---

### Question 28

The block that always executes is __________.

**Answer:** finally

---

# SECTION E — MATCH THE FOLLOWING (10 Marks)

| Column A | Column B                 |
| -------- | ------------------------ |
| open()   | Open File                |
| read()   | Read Entire File         |
| write()  | Write Data               |
| csv      | Spreadsheet Data         |
| json     | Structured Data          |
| pickle   | Object Serialization     |
| try      | Start Exception Handling |
| except   | Handle Errors            |
| else     | Execute When No Error    |
| finally  | Always Execute           |

---

# SECTION F — SHORT ANSWER QUESTIONS (10 Marks)

### Question 29

What is data persistence?

---

### Question 30

Explain the difference between reading and writing a file.

---

### Question 31

What is the difference between CSV and JSON?

---

### Question 32

What is Pickle used for?

---

### Question 33

Why is exception handling important?

---

# SECTION G — CODE READING (10 Marks)

### Question 34

Predict the output.

```python
with open("sample.txt", "w") as file:
    file.write("Python")
```

What happens?

**Answer:**

A file named `sample.txt` is created and the text `"Python"` is written into it.

---

### Question 35

Predict the output.

```python
student = {
    "name": "John",
    "age": 20
}

import json

print(
    json.dumps(student)
)
```

**Answer**

```json
{"name": "John", "age": 20}
```

---

### Question 36

Predict the output.

```python
try:
    print(10 / 2)

except:
    print("Error")
```

**Answer**

```text
5.0
```

---

### Question 37

Predict the output.

```python
try:
    print(10 / 0)

except:
    print("Cannot divide")
```

**Answer**

```text
Cannot divide
```

---

# SECTION H — DEBUGGING QUESTIONS (5 Marks)

### Question 38

Find the error.

```python
file = open("data.txt", "r")

print(file.read()
```

**Answer**

Missing closing bracket.

Correct:

```python
file = open("data.txt", "r")

print(file.read())
```

---

### Question 39

Find the error.

```python
try
    age = int(input())
except:
    print("Invalid")
```

**Answer**

Missing colon after try.

Correct:

```python
try:
    age = int(input())
except:
    print("Invalid")
```

---

# SECTION I — PRACTICAL PROGRAMMING (15 Marks)

### Question 40

Write a program that:

* Creates a file named `notes.txt`
* Writes your name into the file
* Reads the file and displays the content

---

### Question 41

Create a CSV file containing:

| Name | Age |
| ---- | --- |
| John | 20  |
| Mary | 21  |

Using Python's csv module.

---

### Question 42

Create a JSON file containing:

```json
{
    "name": "Adewale",
    "course": "Python Programming"
}
```

Save and load the data.

---

### Question 43

Write a program that safely accepts a user's age using:

```python
try
except
```

and prevents crashes when non-numeric values are entered.

---

# SECTION J — MINI PROJECT (Bonus 10 Marks)

## Student Mini Database

Build a JSON-based database that:

### Features

1. Add Student
2. View Students
3. Save Data
4. Load Data

Student Structure:

```json
{
    "name": "John",
    "age": 20,
    "department": "Computer Science"
}
```

Store all records in:

```text
students.json
```

---

# SECTION K — CONTACT MANAGEMENT SYSTEM PROJECT

### Requirements

Build a Contact Manager that can:

#### Add Contact

```json
{
    "John": "08012345678"
}
```

#### Search Contact

```text
Enter Name:
```

Displays phone number.

#### Update Contact

Modify existing contact information.

#### Delete Contact

Remove a contact.

#### Save Automatically

Store all data inside:

```text
contacts.json
```

---

# SECTION L — CAMBRIDGE A-LEVEL STYLE QUESTIONS

### Question 44

Explain the difference between:

```text
r
```

and

```text
w
```

file modes.

---

### Question 45

Explain three advantages of JSON over plain text files.

---

### Question 46

Describe a situation where CSV is more suitable than JSON.

---

### Question 47

Explain how try-except improves user experience.

---

### Question 48

Differentiate between JSON serialization and Pickle serialization.

---

# END-OF-MODULE CHALLENGE

## Personal Expense Tracker

Build a system that:

### Features

* Add Expenses
* Save Expenses
* View Expenses
* Delete Expenses

Data Example:

```json
[
    {
        "item": "Transport",
        "amount": 1500
    },
    {
        "item": "Food",
        "amount": 3000
    }
]
```

Requirements:

* Store data in JSON.
* Use exception handling.
* Prevent invalid inputs.
* Load saved data when the application starts.

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

# End of Module 6 Assessment

