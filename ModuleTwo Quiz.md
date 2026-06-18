# Module 2 Assessment

## Python Syntax & Core Concepts

### Instructions

* Answer all questions.
* Read every question carefully.
* Some questions may have more than one correct answer.
* Show workings where necessary.
* Total Marks: 100
* Duration: 90 Minutes

---

# Learning Objectives Assessment

By the end of this assessment, students should be able to:

✓ Identify and use Python data types.

✓ Perform arithmetic operations using Python.

✓ Create and manage variables.

✓ Work with strings using indexing, slicing, and methods.

✓ Format output using Python string formatting.

✓ Understand and use Boolean values.

✓ Collect user input and display output.

✓ Work with files and folders.

✓ Read and write text files.

✓ Understand JSON and CSV file formats.

✓ Apply type conversion correctly.

✓ Write clean and documented Python code.

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (20 Marks)

### Question 1

Which Python data type is used to store text?

A. int

B. float

C. str

D. bool

**Answer:** C

---

### Question 2

What is the data type of:

```python
25
```

A. float

B. int

C. str

D. bool

**Answer:** B

---

### Question 3

What is the result of:

```python
10 + 5
```

A. 15

B. 105

C. 50

D. Error

**Answer:** A

---

### Question 4

What is the result of:

```python
10 / 2
```

A. 5

B. 5.0

C. 2

D. 20

**Answer:** B

---

### Question 5

Which symbol is used for exponentiation?

A. %

B. //

C. **

D. //

**Answer:** C

---

### Question 6

Which function displays output?

A. input()

B. show()

C. print()

D. display()

**Answer:** C

---

### Question 7

What is the output?

```python
name = "Python"
print(name[0])
```

A. y

B. P

C. Python

D. Error

**Answer:** B

---

### Question 8

What is the output?

```python
print("Python"[::-1])
```

A. Python

B. nohtyP

C. P

D. Error

**Answer:** B

---

### Question 9

Which method converts text to uppercase?

A. .upper()

B. .lower()

C. .title()

D. .capitalize()

**Answer:** A

---

### Question 10

Which file mode is used for appending data?

A. r

B. w

C. a

D. x

**Answer:** C

---

# SECTION B — MULTIPLE SELECT QUESTIONS (15 Marks)

### Question 11

Select all valid Python data types.

☐ int

☐ float

☐ str

☐ bool

☐ excel

**Correct Answers**

✓ int

✓ float

✓ str

✓ bool

---

### Question 12

Select all arithmetic operators.

☐ +

☐ -

☐ *

☐ /

☐ %

☐ ==

**Correct Answers**

✓ +

✓ -

✓ *

✓ /

✓ %

---

### Question 13

Which of the following are string methods?

☐ upper()

☐ lower()

☐ replace()

☐ split()

☐ average()

**Correct Answers**

✓ upper()

✓ lower()

✓ replace()

✓ split()

---

### Question 14

Select all file modes.

☐ r

☐ w

☐ a

☐ x

☐ readall

**Correct Answers**

✓ r

✓ w

✓ a

✓ x

---

### Question 15

Select all valid file formats.

☐ .txt

☐ .json

☐ .csv

☐ .pdf

☐ .mp3

**Correct Answers**

✓ .txt

✓ .json

✓ .csv

✓ .pdf

✓ .mp3

---

# SECTION C — TRUE OR FALSE (10 Marks)

### Question 16

A string is written inside quotation marks.

☐ True

☐ False

**Answer:** True

---

### Question 17

Python indexing starts from 1.

☐ True

☐ False

**Answer:** False

---

### Question 18

The value of a Boolean can only be True or False.

☐ True

☐ False

**Answer:** True

---

### Question 19

JSON is commonly used for storing and exchanging data.

☐ True

☐ False

**Answer:** True

---

### Question 20

CSV stands for Computer Saved Values.

☐ True

☐ False

**Answer:** False

---

# SECTION D — FILL IN THE GAPS (15 Marks)

### Question 21

Python uses __________ to store text data.

**Answer:** Strings

---

### Question 22

The function used to collect user input is __________.

**Answer:** input()

---

### Question 23

The method used to remove spaces from both ends of a string is __________.

**Answer:** strip()

---

### Question 24

The file extension for JSON files is __________.

**Answer:** .json

---

### Question 25

The file extension for CSV files is __________.

**Answer:** .csv

---

### Question 26

The operator used to calculate remainder is __________.

**Answer:** %

---

### Question 27

The process of changing one data type to another is called __________.

**Answer:** Type Conversion

---

### Question 28

Python reads files using the __________ function.

**Answer:** open()

---

# SECTION E — MATCH THE FOLLOWING (10 Marks)

| Column A | Column B           |
| -------- | ------------------ |
| int      | Whole Number       |
| float    | Decimal Number     |
| str      | Text               |
| bool     | True/False         |
| open()   | File Handling      |
| json     | Data Serialization |
| csv      | Tabular Data       |
| input()  | Collect User Data  |
| print()  | Display Output     |
| strip()  | Remove Spaces      |

---

# SECTION F — SHORT ANSWER QUESTIONS (10 Marks)

### Question 29

Explain what a data type is.

---

### Question 30

Differentiate between an integer and a float.

---

### Question 31

What is a variable?

---

### Question 32

Explain string indexing.

---

### Question 33

What is the difference between an absolute path and a relative path?

---

# SECTION G — CODE READING (5 Marks)

### Question 34

Predict the output.

```python
name = "Adewale"

print(name[0])
print(name[-1])
```

**Answer**

```text
A
e
```

---

### Question 35

Predict the output.

```python
price = 500
quantity = 4

print(price * quantity)
```

**Answer**

```text
2000
```

---

### Question 36

Predict the output.

```python
text = "python"

print(text.upper())
```

**Answer**

```text
PYTHON
```

---

# SECTION H — DEBUGGING QUESTIONS (5 Marks)

### Question 37

Identify and correct the error.

```python
print("Hello World"
```

**Answer**

Missing closing bracket.

Correct Code:

```python
print("Hello World")
```

---

### Question 38

Identify and correct the error.

```python
age = "20"

print(age + 5)
```

**Answer**

String cannot be added directly to integer.

Correct Code:

```python
age = int(age)

print(age + 5)
```

---

# SECTION I — PRACTICAL PROGRAMMING (10 Marks)

### Question 39

Write a program that asks the user for their name and age and displays:

```text
My name is Adewale and I am 25 years old.
```

---

### Question 40

Write a Temperature Converter program.

Convert Celsius to Fahrenheit.

Formula:

```text
F = (C × 9/5) + 32
```

---

### Question 41

Write a Simple Interest Calculator.

Formula:

```text
SI = (P × R × T) / 100
```

---

### Question 42

Create a text file called:

```text
student.txt
```

Write your:

* Name
* Age
* Course

into the file.

---

### Question 43

Create a Python dictionary and save it into a JSON file.

Example:

```python
{
    "name": "Adewale",
    "age": 25
}
```

---

# SECTION J — MINI PROJECT (Bonus 10 Marks)

### Student Registration System

Build a program that:

1. Collects:

   * Name
   * Age
   * Email
   * Course

2. Displays the information using f-strings.

3. Saves the information into a JSON file.

4. Reads the JSON file and displays the data again.

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

# End of Module 2 Assessment

