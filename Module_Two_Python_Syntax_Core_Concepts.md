# Module 2: Python Syntax & Core Concepts

![Module 2 Banner](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+2:+Python+Syntax+and+Core+Concepts)

## Module Overview

Welcome to **Module 2 — Python Syntax & Core Concepts**.

In Module 1, students were introduced to programming, Python, installation, IDE setup, writing a first script, Python execution flow, and debugging basics. In this module, students now begin learning the actual building blocks of Python.

This module is like learning the grammar of Python. Before students can build calculators, websites, automation scripts, data apps, or AI tools, they must understand how Python works with values, variables, text, numbers, files, and user input.

---

## Learning Objectives

By the end of this module, students should be able to:

1. Explain Python data types.
2. Use numbers for arithmetic calculations.
3. Create and use variables.
4. Work with strings, indexing, slicing, and string methods.
5. Format output using f-strings.
6. Understand Booleans and comparison results.
7. Use `input()` and `print()` for input and output.
8. Understand files, folders, directories, and paths.
9. Read from and write to text files.
10. Use `with open()` correctly.
11. Understand file modes such as `r`, `w`, `a`, `x`, `r+`, and `w+`.
12. Understand encoding, ASCII, Unicode, and UTF-8 at beginner level.
13. Store and retrieve data using JSON.
14. Read and write CSV files.
15. Understand binary files at awareness level.
16. Use basic operators and type conversion.
17. Write comments and documentation.
18. Complete beginner-friendly practical exercises.

---

# 1. Introduction to Python Data Types

![Python Data Types](https://placehold.co/1200x500/1f2937/ffffff.png?text=Python+Data+Types:+int,+float,+str,+bool,+list,+tuple,+set,+dict)

## What is a Data Type?

A **data type** is the category or kind of data a value belongs to.

In real life, we classify things into categories:

| Real-Life Item | Category |
|---|---|
| 25 | Number |
| Adewale | Name/Text |
| True | Yes/No |
| 3.75 | Decimal number |
| Rice, Beans, Yam | List of items |

Python also classifies data because it needs to know how to treat each value.

Example:

```python
age = 25
name = "Adewale"
height = 1.75
is_student = True
```

| Variable | Value | Data Type |
|---|---|---|
| `age` | `25` | Integer |
| `name` | `"Adewale"` | String |
| `height` | `1.75` | Float |
| `is_student` | `True` | Boolean |

---

## Why Data Types Matter

Data types matter because Python handles values based on their type.

Example 1:

```python
print(10 + 5)
```

Output:

```text
15
```

Example 2:

```python
print("10" + "5")
```

Output:

```text
105
```

In the first example, Python performs mathematical addition. In the second example, Python joins two strings together.

So, `10` and `"10"` are not the same thing in Python.

---

## Common Python Data Types

| Data Type | Python Name | Example | Meaning |
|---|---|---|---|
| Integer | `int` | `20` | Whole number |
| Float | `float` | `20.5` | Decimal number |
| String | `str` | `"Hello"` | Text |
| Boolean | `bool` | `True` | True or False |
| List | `list` | `[1, 2, 3]` | Ordered collection |
| Tuple | `tuple` | `(1, 2, 3)` | Ordered, unchangeable collection |
| Set | `set` | `{1, 2, 3}` | Unordered unique collection |
| Dictionary | `dict` | `{ "name": "John" }` | Key-value collection |

In this module, we will focus more on beginner concepts: numbers, strings, Booleans, variables, input/output, files, JSON, CSV, operators, and type conversion.

---

## Checking Data Types with `type()`

Python has a function called `type()` that tells us the data type of a value.

```python
print(type(25))
print(type(3.14))
print(type("Hello"))
print(type(True))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

Do not worry too much about the word `class` for now. You will understand it better when you get to Object-Oriented Programming.

---

## Practice

```python
student_name = "Mary"
student_age = 19
student_score = 87.5
has_paid = True

print(type(student_name))
print(type(student_age))
print(type(student_score))
print(type(has_paid))
```

---

# 2. Python Numbers

![Python Numbers](https://placehold.co/1200x500/1f2937/ffffff.png?text=Python+Numbers:+Integer,+Float,+Complex)

Python can work with numbers like a calculator.

The main number types are:

1. Integers
2. Floats
3. Complex numbers

For beginners, the most important number types are **integers** and **floats**.

---

## 2.1 Integers

An integer is a whole number.

```python
age = 25
students = 50
temperature = -3
```

Examples of integers:

```text
10
0
-5
1000
```

---

## 2.2 Floats

A float is a number with a decimal point.

```python
price = 2500.50
height = 1.75
average_score = 82.6
```

Examples of floats:

```text
3.14
0.5
-7.25
100.0
```

Even `100.0` is a float because it has a decimal point.

---

## 2.3 Complex Numbers

Complex numbers contain real and imaginary parts.

```python
number = 2 + 3j
```

This is mostly useful in advanced mathematics, science, and engineering.

For beginners, just know that Python supports it.

---

# 3. Numbers: Simple Arithmetic

![Arithmetic Operators](https://placehold.co/1200x500/1f2937/ffffff.png?text=Simple+Arithmetic:+plus,+minus,+multiply,+divide,+modulus,+power)

Python can perform arithmetic operations.

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `5 + 2` | `7` |
| `-` | Subtraction | `5 - 2` | `3` |
| `*` | Multiplication | `5 * 2` | `10` |
| `/` | Division | `5 / 2` | `2.5` |
| `//` | Floor division | `5 // 2` | `2` |
| `%` | Modulus/remainder | `5 % 2` | `1` |
| `**` | Power | `5 ** 2` | `25` |

---

## Addition

```python
a = 10
b = 5
result = a + b
print(result)
```

Output:

```text
15
```

---

## Subtraction

```python
balance = 10000
withdrawal = 2500
new_balance = balance - withdrawal
print(new_balance)
```

Output:

```text
7500
```

---

## Multiplication

```python
price = 500
quantity = 4
total = price * quantity
print(total)
```

Output:

```text
2000
```

---

## Division

```python
total_score = 360
subjects = 4
average = total_score / subjects
print(average)
```

Output:

```text
90.0
```

Division usually returns a float.

---

## Floor Division

Floor division removes the decimal part.

```python
print(10 // 3)
```

Output:

```text
3
```

---

## Modulus

Modulus gives the remainder after division.

```python
print(10 % 3)
```

Output:

```text
1
```

Modulus is useful for checking even and odd numbers.

```python
number = 8
print(number % 2)
```

Output:

```text
0
```

If a number divided by 2 has remainder 0, it is even.

---

## Power

```python
print(2 ** 3)
```

Output:

```text
8
```

Because:

```text
2 × 2 × 2 = 8
```

---

## Order of Operations

Python follows normal mathematical rules.

```python
print(2 + 3 * 4)
```

Output:

```text
14
```

Multiplication happens before addition.

Use brackets to control the order:

```python
print((2 + 3) * 4)
```

Output:

```text
20
```

---

# 4. Numbers FAQ

## What is the difference between `int` and `float`?

An `int` is a whole number.

```python
age = 25
```

A `float` is a decimal number.

```python
price = 25.5
```

---

## Why does division return `90.0` instead of `90`?

Because Python's `/` operator returns a float.

```python
print(180 / 2)
```

Output:

```text
90.0
```

If you want whole number division, use `//`.

```python
print(180 // 2)
```

Output:

```text
90
```

---

## Can Python handle very large numbers?

Yes.

```python
big_number = 999999999999999999999999999999
print(big_number)
```

---

## Why does `0.1 + 0.2` sometimes show `0.30000000000000004`?

This happens because computers store decimal numbers in binary form, and some decimal values cannot be represented perfectly.

For beginner programs, this is usually not a serious issue. For financial applications, Python has a special `decimal` module.

---

# 5. Numbers Quiz

1. What is the output of `5 + 3`?
2. What is the output of `10 / 2`?
3. What is the output of `10 // 3`?
4. What is the output of `10 % 3`?
5. What is the output of `2 ** 4`?
6. Is `25.0` an integer or a float?
7. Which operator is used for multiplication?
8. Which operator is used to get remainder?
9. What is the output of `(2 + 3) * 4`?
10. What is the output of `2 + 3 * 4`?

## Answers

1. `8`
2. `5.0`
3. `3`
4. `1`
5. `16`
6. Float
7. `*`
8. `%`
9. `20`
10. `14`

---

# 6. Variables and Data Types

![Variables](https://placehold.co/1200x500/1f2937/ffffff.png?text=Variables+store+values+inside+memory)

## What is a Variable?

A variable is a name used to store a value.

Think of a variable like a labelled container.

```python
age = 25
```

This means:

> Store the value `25` inside a variable called `age`.

---

## Creating Variables

```python
name = "John"
age = 20
score = 85.5
is_registered = True
```

---

## Printing Variables

```python
name = "John"
print(name)
```

Output:

```text
John
```

---

## Updating Variables

```python
score = 50
print(score)

score = 80
print(score)
```

Output:

```text
50
80
```

The second value replaces the first value.

---

## Variable Naming Rules

Valid names:

```python
student_name = "John"
age = 20
total_score = 95
first_name = "Mary"
```

Invalid names:

```python
2name = "John"
student-name = "John"
first name = "John"
class = "Python"
```

| Invalid Name | Reason |
|---|---|
| `2name` | Cannot start with a number |
| `student-name` | Hyphen is not allowed |
| `first name` | Space is not allowed |
| `class` | Python keyword |

---

## Best Practice: Use Snake Case

Python variable names usually use **snake_case**.

```python
student_name = "John"
total_amount = 4500
account_balance = 10000
```

Avoid unclear names:

```python
x = "Adewale"
y = 25
z = 90
```

Use meaningful names:

```python
student_name = "Adewale"
student_age = 25
student_score = 90
```

Readable code is better than short confusing code.

---

# 7. Introduction to Strings

![Strings](https://placehold.co/1200x500/1f2937/ffffff.png?text=Strings+are+text+values+inside+quotes)

## What is a String?

A string is text.

In Python, strings are written inside quotes.

```python
name = "Adewale"
message = "Welcome to Python"
```

You can use single quotes or double quotes.

```python
name = 'Adewale'
name = "Adewale"
```

Both are correct.

---

## Why Strings Are Important

Strings are used for:

- Names
- Emails
- Phone numbers
- Passwords
- Messages
- Addresses
- File names
- User input

Example:

```python
student_name = "Blessing"
email = "student@example.com"
phone = "08012345678"
address = "Ibadan, Nigeria"
```

Phone numbers are usually stored as strings because we do not normally calculate with phone numbers.

---

## Multi-Line Strings

Use triple quotes for multi-line strings.

```python
message = '''Welcome to Python.
This is Module 2.
We are learning strings.'''

print(message)
```

You can also use triple double quotes:

```python
message = """This is another
multi-line string."""
```

---

# 8. Quick Print Check

The `print()` function displays output.

```python
print("Hello World")
```

Output:

```text
Hello World
```

Print a variable:

```python
name = "Adewale"
print(name)
```

Print multiple values:

```python
name = "Adewale"
age = 25
print(name, age)
```

Output:

```text
Adewale 25
```

---

## Practice

Write a program that prints:

```text
My name is Adewale
I am learning Python
Python is beginner-friendly
```

Solution:

```python
print("My name is Adewale")
print("I am learning Python")
print("Python is beginner-friendly")
```

---

# 9. Indexing and Slicing with Strings

![String Indexing](https://placehold.co/1200x500/1f2937/ffffff.png?text=String+Indexing:+P+Y+T+H+O+N+=+0+1+2+3+4+5)

Strings are sequences of characters.

```python
word = "PYTHON"
```

Python stores it like this:

```text
P   Y   T   H   O   N
0   1   2   3   4   5
```

Each character has a position called an **index**.

Python indexing starts from `0`, not `1`.

---

# 10. String Indexing

To get one character from a string, use square brackets.

```python
word = "PYTHON"

print(word[0])
print(word[1])
print(word[2])
```

Output:

```text
P
Y
T
```

---

## Negative Indexing

Python supports negative indexing.

```text
P    Y    T    H    O    N
-6   -5   -4   -3   -2   -1
```

Example:

```python
word = "PYTHON"

print(word[-1])
print(word[-2])
```

Output:

```text
N
O
```

---

## Common Beginner Mistake

```python
word = "PYTHON"
print(word[6])
```

This causes an error because there is no index `6`.

The last index is `5`.

Error:

```text
IndexError: string index out of range
```

---

# 11. String Slicing

![String Slicing](https://placehold.co/1200x500/1f2937/ffffff.png?text=String+Slicing:+word[start:stop:step])

Slicing means taking a part of a string.

Syntax:

```python
string[start:stop]
```

Important:

The `stop` index is not included.

Example:

```python
word = "PYTHON"
print(word[0:3])
```

Output:

```text
PYT
```

It starts from index `0` and stops before index `3`.

---

## Common Slicing Examples

```python
word = "PYTHON"

print(word[0:2])
print(word[2:5])
print(word[:3])
print(word[3:])
print(word[:])
```

Output:

```text
PY
THO
PYT
HON
PYTHON
```

---

## Using Step

```python
word = "PYTHON"
print(word[0:6:2])
```

Output:

```text
PTO
```

This means start at index `0`, stop before index `6`, and move by `2`.

---

## Reversing a String

```python
word = "PYTHON"
print(word[::-1])
```

Output:

```text
NOHTYP
```

---

# 12. String Properties and Methods

![String Methods](https://placehold.co/1200x500/1f2937/ffffff.png?text=String+Methods:+upper,+lower,+strip,+replace,+split)

## Strings Are Immutable

Strings cannot be changed directly after they are created.

```python
name = "John"
name[0] = "M"
```

This causes an error.

Correct way:

```python
name = "John"
new_name = "M" + name[1:]
print(new_name)
```

Output:

```text
Mohn
```

---

## Common String Methods

| Method | Meaning |
|---|---|
| `.upper()` | Converts to uppercase |
| `.lower()` | Converts to lowercase |
| `.title()` | Capitalizes each word |
| `.strip()` | Removes extra spaces |
| `.replace()` | Replaces part of a string |
| `.split()` | Splits a string into parts |
| `.startswith()` | Checks beginning |
| `.endswith()` | Checks ending |

Example:

```python
name = " adewale oladiti "

print(name.upper())
print(name.lower())
print(name.title())
print(name.strip())
```

---

## Replace

```python
message = "I love Java"
new_message = message.replace("Java", "Python")
print(new_message)
```

Output:

```text
I love Python
```

---

## Split

```python
full_name = "Adewale Oladiti"
parts = full_name.split()
print(parts)
```

Output:

```text
['Adewale', 'Oladiti']
```

---

## Startswith and Endswith

```python
email = "student@example.com"

print(email.endswith(".com"))
print(email.startswith("student"))
```

Output:

```text
True
True
```

---

# 13. String Strip Methods

![Strip Methods](https://placehold.co/1200x500/1f2937/ffffff.png?text=strip,+lstrip,+rstrip+remove+unwanted+spaces)

Sometimes user input contains unwanted spaces.

```python
name = "   Adewale   "
```

Use `.strip()` to remove spaces from both sides.

```python
clean_name = name.strip()
print(clean_name)
```

Output:

```text
Adewale
```

---

## `lstrip()`

Removes spaces from the left side.

```python
name = "   Adewale   "
print(name.lstrip())
```

---

## `rstrip()`

Removes spaces from the right side.

```python
name = "   Adewale   "
print(name.rstrip())
```

---

## Practical Example

```python
email = "  STUDENT@example.COM  "
clean_email = email.strip().lower()
print(clean_email)
```

Output:

```text
student@example.com
```

---

# 14. `removeprefix()` and `removesuffix()`

Python 3.9 introduced two useful string methods:

- `removeprefix()`
- `removesuffix()`

## Remove Website Prefix

```python
url = "https://example.com"
clean_url = url.removeprefix("https://")
print(clean_url)
```

Output:

```text
example.com
```

---

## Remove File Extension

```python
filename = "report.csv"
name_only = filename.removesuffix(".csv")
print(name_only)
```

Output:

```text
report
```

---

# 15. Strings FAQ

## What is the difference between `'Hello'` and `"Hello"`?

There is no major difference. Both are valid strings.

```python
name = 'Adewale'
name = "Adewale"
```

Use one style consistently.

---

## Can a string contain numbers?

Yes.

```python
phone = "08012345678"
```

This is a string, not a number.

---

## Why is my number not adding correctly?

```python
a = "10"
b = "5"
print(a + b)
```

Output:

```text
105
```

Because they are strings.

Correct:

```python
print(int(a) + int(b))
```

Output:

```text
15
```

---

# 16. Strings Quiz

1. What is a string?
2. Which function prints output in Python?
3. What is the index of the first character in a string?
4. What does `word[0]` return?
5. What does `word[-1]` return?
6. What does `.upper()` do?
7. What does `.strip()` do?
8. What is the output of `"Python"[0:3]`?
9. What is the output of `"Python"[::-1]`?
10. What method can replace text inside a string?

## Answers

1. Text data
2. `print()`
3. `0`
4. First character
5. Last character
6. Converts to uppercase
7. Removes spaces from both ends
8. `Pyt`
9. `nohtyP`
10. `.replace()`

---

# 17. Print Formatting with Strings

![Print Formatting](https://placehold.co/1200x500/1f2937/ffffff.png?text=Print+Formatting:+combine+text+and+variables)

Print formatting means combining text and variables neatly.

```python
name = "Adewale"
age = 25
print("My name is", name, "and I am", age, "years old.")
```

Output:

```text
My name is Adewale and I am 25 years old.
```

---

## Method 1: Comma Separation

```python
name = "Adewale"
age = 25
print("My name is", name, "and I am", age, "years old.")
```

This is simple, but less flexible.

---

## Method 2: `.format()`

```python
name = "Adewale"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
```

---

## Method 3: f-Strings

This is the recommended modern method.

```python
name = "Adewale"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)
```

Output:

```text
My name is Adewale and I am 25 years old.
```

---

## Formatting Decimals

```python
amount = 1234.56789
print(f"Amount: {amount:.2f}")
```

Output:

```text
Amount: 1234.57
```

`.2f` means show two decimal places.

---

# 18. Print Formatting FAQ

## Which formatting method should beginners use?

Use f-strings. They are clean, modern, and readable.

```python
name = "Mary"
print(f"Hello {name}")
```

---

## Can f-strings calculate values?

Yes.

```python
price = 100
quantity = 5
print(f"Total: {price * quantity}")
```

Output:

```text
Total: 500
```

---

# 19. Booleans in Python

![Booleans](https://placehold.co/1200x500/1f2937/ffffff.png?text=Booleans:+True+or+False)

A Boolean is a value that can only be:

```python
True
```

or:

```python
False
```

Booleans are used for decision-making.

| Question | Boolean Answer |
|---|---|
| Is the student registered? | `True` |
| Has the user paid? | `False` |
| Is password correct? | `True` |
| Is account active? | `False` |

---

## Boolean Examples

```python
is_student = True
has_paid = False

print(is_student)
print(has_paid)
```

---

## Comparisons Return Booleans

```python
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 5)
```

Output:

```text
True
False
True
True
```

---

## Common Comparison Operators

| Operator | Meaning |
|---|---|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

---

# 20. Sets and Booleans Quiz

A set is a collection of unique items.

```python
students = {"John", "Mary", "Adewale"}
```

Set membership returns a Boolean.

```python
students = {"John", "Mary", "Adewale"}

print("Mary" in students)
print("Peter" in students)
```

Output:

```text
True
False
```

## Quiz

1. What are the two Boolean values?
2. What is the result of `10 > 5`?
3. What is the result of `10 == 5`?
4. What does `!=` mean?
5. What does `"a" in "apple"` return?
6. What does `"z" in "apple"` return?

## Answers

1. `True` and `False`
2. `True`
3. `False`
4. Not equal to
5. `True`
6. `False`

---

# 21. Python Input and Output Fundamentals

![Input Output](https://placehold.co/1200x500/1f2937/ffffff.png?text=Input+and+Output:+User+to+Python+to+Result)

I/O means **Input and Output**.

- Input means data entering a program.
- Output means data leaving a program.

Example:

```python
name = input("Enter your name: ")
print(f"Welcome {name}")
```

If the user enters:

```text
Adewale
```

Output:

```text
Welcome Adewale
```

---

## `input()` Always Returns a String

```python
age = input("Enter your age: ")
print(type(age))
```

Even if the user types `25`, Python treats it as `"25"`.

---

## Converting Input

```python
age = input("Enter your age: ")
age = int(age)
print(age + 5)
```

If user enters `25`, output is:

```text
30
```

---

## Beginner Example: Age Calculator

```python
birth_year = input("Enter your birth year: ")
birth_year = int(birth_year)

current_year = 2026
age = current_year - birth_year

print(f"You are {age} years old.")
```

---

# 22. Understanding Computer File Systems

![File System](https://placehold.co/1200x500/1f2937/ffffff.png?text=Files,+Folders,+Directories,+and+Paths)

Before learning file handling, students must understand files and folders.

## What is a File?

A file stores data.

Examples:

- `notes.txt`
- `students.csv`
- `config.json`
- `photo.png`
- `report.pdf`

---

## What is a Folder?

A folder is a container for files and other folders.

Example:

```text
PythonCourse/
│
├── module2.py
├── notes.txt
├── data.csv
└── images/
    └── diagram.png
```

---

## What is a Directory?

A directory is another name for a folder.

---

## What is a Path?

A path tells Python where a file is located.

Windows example:

```text
C:\Users\Adewale\Documents\notes.txt
```

Mac/Linux example:

```text
/home/adewale/Documents/notes.txt
```

---

# 23. Command Line Navigation

![Command Line](https://placehold.co/1200x500/1f2937/ffffff.png?text=Command+Line+Navigation:+cd,+dir,+ls,+pwd)

The command line allows us to control the computer using text commands.

On Windows, it may be called:

- Command Prompt
- PowerShell
- Windows Terminal

On Mac/Linux, it is called:

- Terminal

---

## Common Commands

| Purpose | Windows | Mac/Linux |
|---|---|---|
| Show current folder | `cd` | `pwd` |
| List files | `dir` | `ls` |
| Enter folder | `cd folder_name` | `cd folder_name` |
| Go back | `cd ..` | `cd ..` |
| Clear screen | `cls` | `clear` |

Example:

```bash
cd Documents
dir
cd PythonCourse
python module2.py
```

---

# 24. File Paths: Absolute vs Relative

![File Paths](https://placehold.co/1200x500/1f2937/ffffff.png?text=Absolute+Path+vs+Relative+Path)

## Absolute Path

An absolute path starts from the root of the computer.

Windows example:

```text
C:\Users\Adewale\Documents\PythonCourse\notes.txt
```

Mac/Linux example:

```text
/home/adewale/Documents/PythonCourse/notes.txt
```

---

## Relative Path

A relative path starts from your current project folder.

Example:

```text
notes.txt
```

or:

```text
data/students.csv
```

If your Python file and `notes.txt` are in the same folder, you can write:

```python
open("notes.txt")
```

---

# 25. Defining and Working with Text Files

![Text Files](https://placehold.co/1200x500/1f2937/ffffff.png?text=Text+Files:+.txt+stores+plain+readable+text)

A text file stores plain readable text.

Example content of `notes.txt`:

```text
Python is easy to learn.
We are studying file handling.
This is Module 2.
```

Text files usually end with `.txt`.

---

## Creating a Text File

1. Open VS Code.
2. Create a file called `notes.txt`.
3. Type some text inside it.
4. Save it in the same folder as your Python file.

Example folder:

```text
Module2/
│
├── read_notes.py
└── notes.txt
```

---

# 26. Reading Data from Text Files

![Reading Files](https://placehold.co/1200x500/1f2937/ffffff.png?text=Reading+Files+in+Python+with+open+and+read)

## Basic Reading

```python
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()
```

Explanation:

| Code | Meaning |
|---|---|
| `open("notes.txt", "r")` | Opens file for reading |
| `file.read()` | Reads the content |
| `print(content)` | Displays content |
| `file.close()` | Closes the file |

---

## Why Close Files?

You should close files because:

- It frees system resources.
- It prevents file corruption.
- It is good programming practice.

But Python has a better way: `with open()`.

---

# 27. Python's `with` Statement

![With Open](https://placehold.co/1200x500/1f2937/ffffff.png?text=with+open+automatically+closes+files)

The `with` statement automatically closes the file after use.

Recommended method:

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

This is better than manually calling `file.close()`.

---

## Reading Line by Line

```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line)
```

---

# 28. Parsing Text File Data

Parsing means extracting useful information from text.

Example file: `countries.txt`

```text
Nigeria,Abuja
Ghana,Accra
Kenya,Nairobi
South Africa,Pretoria
```

Python code:

```python
with open("countries.txt", "r") as file:
    for line in file:
        country, capital = line.strip().split(",")
        print(f"The capital of {country} is {capital}")
```

Output:

```text
The capital of Nigeria is Abuja
The capital of Ghana is Accra
The capital of Kenya is Nairobi
The capital of South Africa is Pretoria
```

---

# 29. Efficient Data Retrieval with Dictionaries

![Dictionary Lookup](https://placehold.co/1200x500/1f2937/ffffff.png?text=Dictionary+Lookup:+key+to+value)

A dictionary stores data as key-value pairs.

```python
capitals = {
    "Nigeria": "Abuja",
    "Ghana": "Accra",
    "Kenya": "Nairobi"
}

country = input("Enter country: ")
print(capitals[country])
```

Safer version:

```python
country = input("Enter country: ")
capital = capitals.get(country)

if capital:
    print(f"The capital of {country} is {capital}")
else:
    print("Country not found.")
```

---

# 30. Writing to Text Files

![Writing Files](https://placehold.co/1200x500/1f2937/ffffff.png?text=Writing+Files+in+Python)

Writing means saving data into a file.

```python
with open("output.txt", "w") as file:
    file.write("Hello Python")
```

This creates a file called `output.txt` and writes text inside it.

---

## Writing Multiple Lines

```python
with open("students.txt", "w") as file:
    file.write("John\n")
    file.write("Mary\n")
    file.write("Adewale\n")
```

`\n` means new line.

---

## Appending to a File

Appending means adding new content without deleting old content.

```python
with open("students.txt", "a") as file:
    file.write("Blessing\n")
```

---

# 31. Understanding Python File Modes

![File Modes](https://placehold.co/1200x500/1f2937/ffffff.png?text=File+Modes:+r,+w,+a,+x,+rplus,+wplus)

| Mode | Meaning |
|---|---|
| `r` | Read file |
| `w` | Write file; overwrite existing content |
| `a` | Append to file |
| `x` | Create new file; error if file exists |
| `r+` | Read and write |
| `w+` | Write and read; overwrites existing content |

Beginner warning:

Be careful with `w`. It replaces old content.

If you want to add content, use `a`.

---

# 32. Character Encodings

![Encoding](https://placehold.co/1200x500/1f2937/ffffff.png?text=Encoding:+characters+become+numbers+and+bytes)

Computers store text as numbers.

Example:

```text
A -> 65
B -> 66
C -> 67
```

Encoding is the system used to convert characters into numbers.

---

## ASCII

ASCII is an older encoding system for basic English characters.

```text
A = 65
a = 97
0 = 48
```

---

## Unicode

Unicode supports many languages and symbols.

Examples:

```text
A
é
₦
你
😊
```

---

## UTF-8

UTF-8 is the most common encoding today.

Recommended:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Use `encoding="utf-8"` when reading and writing text files.

---

# 33. Data Serialization with JSON

![JSON](https://placehold.co/1200x500/1f2937/ffffff.png?text=JSON+stores+structured+data)

JSON means **JavaScript Object Notation**.

It is used to store and exchange data.

Example JSON:

```json
{
  "name": "Adewale",
  "age": 25,
  "is_student": true
}
```

JSON looks similar to Python dictionaries, but they are not exactly the same.

Python uses `True`; JSON uses `true`.

---

## Writing JSON to a File

```python
import json

student = {
    "name": "Adewale",
    "age": 25,
    "course": "Python"
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)
```

---

## Reading JSON from a File

```python
import json

with open("student.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print(data)
print(data["name"])
```

---

## JSON Data Types

| JSON Type | Python Equivalent |
|---|---|
| string | `str` |
| number | `int` or `float` |
| true/false | `True`/`False` |
| null | `None` |
| array | `list` |
| object | `dict` |

---

# 34. Downloading and Parsing JSON from the Internet

![API JSON](https://placehold.co/1200x500/1f2937/ffffff.png?text=APIs+often+send+data+as+JSON)

Many websites and apps send data using JSON.

Examples:

- Weather apps
- Payment gateways
- School portals
- Hospital systems
- Banking APIs

Example:

```python
import requests

url = "https://api.github.com"
response = requests.get(url)
data = response.json()

print(data)
```

You may need to install requests:

```bash
pip install requests
```

This topic is more intermediate, so beginners should first master local JSON files.

---

# 35. Introduction to CSV

![CSV](https://placehold.co/1200x500/1f2937/ffffff.png?text=CSV:+rows+and+columns+separated+by+commas)

CSV means **Comma-Separated Values**.

It stores tabular data.

Example CSV:

```csv
name,age,score
John,20,85
Mary,21,90
Adewale,25,95
```

CSV files are commonly opened with:

- Microsoft Excel
- Google Sheets
- Python
- Database tools

---

# 36. Reading CSV Files

```python
import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

Output:

```text
['name', 'age', 'score']
['John', '20', '85']
['Mary', '21', '90']
['Adewale', '25', '95']
```

---

## Skipping Header Row

```python
import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        print(row)
```

`next(reader)` skips the first row.

---

# 37. CSV DictReader

![DictReader](https://placehold.co/1200x500/1f2937/ffffff.png?text=csv.DictReader+reads+CSV+rows+as+dictionaries)

`csv.DictReader` reads each row as a dictionary.

```python
import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"], row["score"])
```

Output:

```text
John 85
Mary 90
Adewale 95
```

---

# 38. Writing CSV Files

```python
import csv

with open("new_students.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "score"])
    writer.writerow(["John", 20, 85])
    writer.writerow(["Mary", 21, 90])
```

---

## Writing CSV with DictWriter

```python
import csv

students = [
    {"name": "John", "age": 20, "score": 85},
    {"name": "Mary", "age": 21, "score": 90},
    {"name": "Adewale", "age": 25, "score": 95},
]

with open("students_output.csv", "w", encoding="utf-8", newline="") as file:
    fieldnames = ["name", "age", "score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students)
```

---

# 39. CSV Quoting and Dialects

CSV can become tricky when data contains commas.

Example:

```csv
name,address
Adewale,"Ibadan, Oyo State"
```

The address contains a comma, so it is wrapped in quotes.

Python's `csv` module handles this correctly.

Important rule:

> Do not manually split serious CSV files with `.split(",")`. Use the `csv` module.

---

# 40. Transforming Data with `zip()`

![Zip Function](https://placehold.co/1200x500/1f2937/ffffff.png?text=zip+combines+related+lists+together)

The `zip()` function combines values from multiple lists.

```python
names = ["John", "Mary", "Adewale"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(name, score)
```

Output:

```text
John 85
Mary 90
Adewale 95
```

---

# 41. Simultaneous Read and Write Operations

Sometimes you may read from one file and write processed results into another.

```python
with open("students.csv", "r", encoding="utf-8") as input_file:
    with open("passed_students.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            output_file.write(line)
```

Beginner warning:

Avoid reading and writing to the same file at the same time until you understand file pointers properly.

---

# 42. `seek()` and `tell()`

![Seek Tell](https://placehold.co/1200x500/1f2937/ffffff.png?text=seek+and+tell+control+the+file+cursor+position)

When Python reads a file, it uses a cursor/pointer.

- `tell()` tells you where the cursor is.
- `seek()` moves the cursor.

Example:

```python
with open("notes.txt", "r", encoding="utf-8") as file:
    print(file.tell())

    content = file.read(5)
    print(content)
    print(file.tell())

    file.seek(0)
    print(file.read())
```

For beginners, this is awareness-level. Do not spend too much time here initially.

---

# 43. Binary Files

![Binary Files](https://placehold.co/1200x500/1f2937/ffffff.png?text=Binary+Files+store+bytes:+images,+audio,+PDFs)

Text files store readable text.

Binary files store bytes.

Examples:

- Images
- Audio files
- Videos
- PDFs
- Executable files

Binary mode uses `b`.

```python
with open("image.png", "rb") as file:
    data = file.read()
```

`rb` means read binary.

```python
with open("copy.png", "wb") as file:
    file.write(data)
```

`wb` means write binary.

---

## bytes and bytearray

```python
data = b"Hello"
print(data)
print(type(data))
```

Output:

```text
b'Hello'
<class 'bytes'>
```

Binary file handling is an advanced topic. For this beginner module, students only need to know that binary files are not normal text files.

---

# 44. Big Endian and Little Endian

![Endian](https://placehold.co/1200x500/1f2937/ffffff.png?text=Big+Endian+vs+Little+Endian+byte+order)

Endianess describes the order in which bytes are stored.

Example number:

```text
0x12345678
```

Big endian:

```text
12 34 56 78
```

Little endian:

```text
78 56 34 12
```

This is useful in computer architecture, networking, binary file formats, and low-level programming.

For absolute beginners, this should be treated as awareness, not mastery.

---

# 45. MP3 Metadata and ID3 Tags

![MP3 Metadata](https://placehold.co/1200x500/1f2937/ffffff.png?text=MP3+metadata+stores+title,+artist,+album,+cover+art)

MP3 files can contain metadata such as:

- Song title
- Artist
- Album
- Year
- Cover image

This metadata is often stored using ID3 tags.

Reading and editing MP3 metadata is advanced Python work. It involves binary files, byte parsing, file formats, encoding, and metadata frames.

For a beginner course, introduce it only as an example of what Python can do later.

---

# 46. SHA-256 Hash Checksums

![SHA256](https://placehold.co/1200x500/1f2937/ffffff.png?text=SHA-256+Hash:+verify+file+integrity)

A checksum helps verify that a file has not changed.

SHA-256 produces a unique fingerprint for data.

```python
import hashlib

text = "Hello Python"
hash_value = hashlib.sha256(text.encode()).hexdigest()
print(hash_value)
```

Use cases:

- Verifying downloads
- Cybersecurity
- Password hashing concepts
- File integrity checks

Important:

Hashing is not encryption. Hashing is one-way. Encryption is meant to be reversible with a key.

---

# 47. Basic Operators

![Operators](https://placehold.co/1200x500/1f2937/ffffff.png?text=Python+Operators:+arithmetic,+comparison,+logical,+assignment)

Python operators are symbols used to perform operations.

## Arithmetic Operators

| Operator | Meaning |
|---|---|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `//` | Floor division |
| `%` | Remainder |
| `**` | Power |

---

## Assignment Operators

```python
x = 10
x += 5
x -= 2
x *= 3
```

`x += 5` means:

```python
x = x + 5
```

---

## Logical Operators

| Operator | Meaning |
|---|---|
| `and` | Both conditions must be true |
| `or` | At least one condition must be true |
| `not` | Reverses the result |

Example:

```python
age = 20
has_id = True
print(age >= 18 and has_id)
```

Output:

```text
True
```

---

# 48. Type Conversion

![Type Conversion](https://placehold.co/1200x500/1f2937/ffffff.png?text=Type+Conversion:+str,+int,+float,+bool)

Type conversion means changing data from one type to another.

---

## String to Integer

```python
age = "25"
age = int(age)
print(age + 5)
```

Output:

```text
30
```

---

## Integer to String

```python
age = 25
message = "I am " + str(age) + " years old"
print(message)
```

---

## String to Float

```python
price = "2500.50"
price = float(price)
print(price + 100)
```

---

## Common Conversion Functions

| Function | Meaning |
|---|---|
| `int()` | Convert to integer |
| `float()` | Convert to decimal |
| `str()` | Convert to string |
| `bool()` | Convert to Boolean |
| `list()` | Convert to list where possible |

Beginner warning:

```python
age = int("twenty")
```

This will fail because `"twenty"` is not a valid number.

---

# 49. Comments and Documentation Standards

![Comments](https://placehold.co/1200x500/1f2937/ffffff.png?text=Comments+explain+code+to+humans)

Comments are notes inside code.

Python ignores comments when running the program.

---

## Single-Line Comment

```python
# This program calculates student average score
score1 = 80
score2 = 90

average = (score1 + score2) / 2
print(average)
```

---

## Why Comments Are Useful

Comments help:

- Explain difficult code
- Make code easier to maintain
- Help other developers understand your logic
- Remind you why you wrote something

---

## Bad Comment

```python
# Add 2 and 3
result = 2 + 3
```

This comment is unnecessary because the code is already obvious.

---

## Good Comment

```python
# Convert input to integer because input() returns a string
age = int(input("Enter your age: "))
```

This comment explains why the code is written that way.

---

## Docstrings

Docstrings explain what a function, class, or module does.

```python
def calculate_average(score1, score2):
    """Calculate the average of two scores."""
    return (score1 + score2) / 2
```

---

# 50. Practical 1: Temperature Conversion Program

![Temperature Converter](https://placehold.co/1200x500/1f2937/ffffff.png?text=Practical:+Temperature+Conversion+Program)

## Task

Write a program that converts Celsius to Fahrenheit.

Formula:

```text
Fahrenheit = (Celsius × 9/5) + 32
```

## Solution

```python
celsius = input("Enter temperature in Celsius: ")
celsius = float(celsius)

fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")
```

## Improved Version

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
```

---

# 51. Practical 2: Interest Calculator

![Interest Calculator](https://placehold.co/1200x500/1f2937/ffffff.png?text=Practical:+Simple+Interest+Calculator)

## Task

Write a program to calculate simple interest.

Formula:

```text
Simple Interest = (Principal × Rate × Time) / 100
```

## Solution

```python
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time in years: "))

interest = (principal * rate * time) / 100
print(f"Simple Interest: ₦{interest:.2f}")
```

## Improved Version with Total Amount

```python
principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time in years: "))

interest = (principal * rate * time) / 100
total_amount = principal + interest

print(f"Principal: ₦{principal:.2f}")
print(f"Interest: ₦{interest:.2f}")
print(f"Total Amount: ₦{total_amount:.2f}")
```

---

# 52. Cambridge-Style Practice Questions

## Question 1

A student enters their name, age, and score. Write a Python program that displays the information in a sentence.

Expected output:

```text
Mary is 18 years old and scored 85 marks.
```

Solution:

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
score = input("Enter your score: ")

print(f"{name} is {age} years old and scored {score} marks.")
```

---

## Question 2

Write a program that asks for two numbers and displays their sum, difference, product, and quotient.

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Quotient: {num1 / num2}")
```

---

## Question 3

A shop sells an item for a given price and quantity. Write a program to calculate the total cost.

```python
price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = price * quantity
print(f"Total cost: ₦{total:.2f}")
```

---

## Question 4

Write a program that stores a student's information in a JSON file.

```python
import json

student = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "course": input("Enter course: ")
}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

print("Student information saved successfully.")
```

---

## Question 5

Write a program that reads a CSV file containing student names and scores and prints each record.

Sample CSV: `students.csv`

```csv
name,score
John,80
Mary,90
Adewale,95
```

Solution:

```python
import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"{row['name']} scored {row['score']}")
```

---

# 53. End-of-Module Mini Projects

## Mini Project 1: Student Bio Generator

Ask the user for:

- Full name
- Age
- Course
- School
- Favorite programming language

Then display a formatted student profile.

---

## Mini Project 2: Basic Calculator

Ask the user for two numbers.

Display:

- Addition
- Subtraction
- Multiplication
- Division
- Modulus
- Power

---

## Mini Project 3: Simple Student Record File

Ask the user for:

- Student name
- Age
- Score

Save it into a text file called `student_record.txt`.

---

## Mini Project 4: JSON Contact Saver

Ask the user for:

- Name
- Phone number
- Email

Save the data into `contact.json`.

---

## Mini Project 5: CSV Score Recorder

Create a program that allows the user to enter student records and save them into `scores.csv`.

---

# 54. Module Summary

In this module, we learned:

- Python data types
- Numbers and arithmetic
- Variables
- Strings
- Indexing and slicing
- String methods
- Print formatting
- Booleans
- Input and output
- Files and folders
- Paths
- Command line basics
- Text files
- File modes
- Encodings
- JSON
- CSV
- Binary files overview
- Operators
- Type conversion
- Comments and documentation
- Practical beginner programs

This module is one of the most important modules in Python because it gives students the foundation they need before learning control flow, loops, functions, data structures, and OOP.

---

# 55. Recommended Class Breakdown

For absolute beginners, this module should not be rushed.

| Section | Recommended Time |
|---|---:|
| Data types, numbers, variables | 2 hours |
| Strings, indexing, slicing, methods | 3 hours |
| Print formatting, Booleans, operators | 2 hours |
| Input/output and type conversion | 2 hours |
| Files, folders, paths, command line | 2 hours |
| Text file reading/writing | 3 hours |
| JSON and CSV introduction | 3 hours |
| Practicals and assessment | 3 hours |
| **Total** | **20 hours** |

For your 3-month beginner-to-OOP program, Module 2 can be taught across **3 to 4 weeks**, depending on your weekly contact hours.

---

# 56. Teacher's Note

This module contains some advanced topics such as:

- Binary files
- MP3 metadata
- Big endian/little endian
- SHA-256
- File pointers

For absolute beginners, these should be introduced lightly as awareness topics. Do not expect students to master them at this stage.

The beginner mastery focus should be:

1. Numbers
2. Variables
3. Strings
4. Booleans
5. Input/output
6. Basic files
7. JSON
8. CSV
9. Operators
10. Type conversion

---

# 57. Final Assessment

## Theory Questions

1. What is a data type?
2. Mention four Python data types.
3. What is the difference between an integer and a float?
4. What is a variable?
5. Give three rules for naming variables.
6. What is a string?
7. What is string indexing?
8. What is string slicing?
9. What does `.strip()` do?
10. What is a Boolean?
11. What does `input()` do?
12. Why do we convert input values?
13. What is a file path?
14. What is the difference between absolute and relative paths?
15. What does `with open()` do?
16. What is JSON used for?
17. What is CSV used for?
18. What is UTF-8?
19. What is type conversion?
20. What is a comment?

## Coding Questions

1. Write a program that asks for a user's name and prints a welcome message.
2. Write a program that calculates the area of a rectangle.
3. Write a program that converts naira to dollars using a fixed exchange rate.
4. Write a program that checks the type of four different variables.
5. Write a program that slices the first three characters from a string.
6. Write a program that removes spaces from user input.
7. Write a program that formats a receipt.
8. Write a program that saves text to a file.
9. Write a program that reads text from a file.
10. Write a program that saves a student's record as JSON.

---

# End of Module 2

![End of Module](https://placehold.co/1200x500/1f2937/ffffff.png?text=End+of+Module+2:+Practice,+Build,+Repeat)
