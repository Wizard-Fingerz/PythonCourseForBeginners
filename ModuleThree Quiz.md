# Module 3 Assessment

## Control Flow (Conditions and Loops)

### Instructions

* Answer all questions.
* Read every question carefully.
* Some questions may have more than one correct answer.
* Attempt the practical section.
* Total Marks: 100
* Duration: 90 Minutes

---

# Learning Objectives Assessment

By the end of this assessment, students should be able to:

✓ Use if statements

✓ Use if-else statements

✓ Use if-elif-else statements

✓ Create nested conditions

✓ Use logical operators

✓ Write for loops

✓ Write while loops

✓ Apply break, continue, and pass

✓ Build basic decision-making programs

✓ Build simple interactive applications

---

# SECTION A — MULTIPLE CHOICE QUESTIONS (20 Marks)

### Question 1

What is the purpose of an if statement?

A. To repeat code

B. To make decisions

C. To create variables

D. To print output

**Answer:** B

---

### Question 2

Which keyword is used when a condition is false?

A. elif

B. otherwise

C. else

D. break

**Answer:** C

---

### Question 3

What is the output?

```python
age = 20

if age >= 18:
    print("Adult")
```

A. Child

B. Adult

C. Error

D. Nothing

**Answer:** B

---

### Question 4

Which logical operator requires both conditions to be True?

A. or

B. not

C. and

D. if

**Answer:** C

---

### Question 5

What is the output?

```python
print(10 > 5)
```

A. False

B. Error

C. True

D. 10

**Answer:** C

---

### Question 6

Which loop is best when the number of repetitions is known?

A. while

B. for

C. if

D. else

**Answer:** B

---

### Question 7

What is the output?

```python
for i in range(3):
    print(i)
```

A.

```text
1
2
3
```

B.

```text
0
1
2
```

C.

```text
0
1
2
3
```

D. Error

**Answer:** B

---

### Question 8

Which keyword stops a loop immediately?

A. continue

B. stop

C. pass

D. break

**Answer:** D

---

### Question 9

Which keyword skips the current iteration?

A. break

B. continue

C. pass

D. stop

**Answer:** B

---

### Question 10

What is the purpose of pass?

A. Ends the loop

B. Skips an iteration

C. Does nothing

D. Repeats the loop

**Answer:** C

---

# SECTION B — MULTIPLE SELECT QUESTIONS (15 Marks)

### Question 11

Select all valid control flow statements.

☐ if

☐ else

☐ elif

☐ while

☐ repeat

**Answers**

✓ if

✓ else

✓ elif

✓ while

---

### Question 12

Select all logical operators.

☐ and

☐ or

☐ not

☐ loop

☐ compare

**Answers**

✓ and

✓ or

✓ not

---

### Question 13

Select all loop types in Python.

☐ for

☐ while

☐ repeat

☐ foreach

☐ loop

**Answers**

✓ for

✓ while

---

### Question 14

Which statements can be used inside loops?

☐ break

☐ continue

☐ pass

☐ elif

☐ input

**Answers**

✓ break

✓ continue

✓ pass

✓ input

---

### Question 15

Which situations require decision making?

☐ ATM withdrawal

☐ Login system

☐ Student grading

☐ Voting eligibility

☐ Calculator display

**Answers**

✓ ATM withdrawal

✓ Login system

✓ Student grading

✓ Voting eligibility

---

# SECTION C — TRUE OR FALSE (10 Marks)

### Question 16

Python uses indentation to define code blocks.

☐ True

☐ False

**Answer:** True

---

### Question 17

A for loop can repeat code.

☐ True

☐ False

**Answer:** True

---

### Question 18

break skips one iteration.

☐ True

☐ False

**Answer:** False

---

### Question 19

continue stops the loop completely.

☐ True

☐ False

**Answer:** False

---

### Question 20

A while loop runs while a condition remains True.

☐ True

☐ False

**Answer:** True

---

# SECTION D — FILL IN THE GAPS (15 Marks)

### Question 21

Python uses __________ statements to make decisions.

**Answer:** if

---

### Question 22

The keyword used for an alternative condition is __________.

**Answer:** elif

---

### Question 23

The keyword used when all conditions fail is __________.

**Answer:** else

---

### Question 24

The logical operator requiring both conditions to be true is __________.

**Answer:** and

---

### Question 25

The loop used to iterate through a range of values is __________.

**Answer:** for

---

### Question 26

The loop used when a condition controls repetition is __________.

**Answer:** while

---

### Question 27

The statement used to stop a loop immediately is __________.

**Answer:** break

---

### Question 28

The statement used to skip the current iteration is __________.

**Answer:** continue

---

# SECTION E — MATCH THE FOLLOWING (10 Marks)

| Column A | Column B                    |
| -------- | --------------------------- |
| if       | Decision Making             |
| elif     | Additional Condition        |
| else     | Default Action              |
| and      | Both Conditions True        |
| or       | At Least One Condition True |
| not      | Reverse Condition           |
| for      | Fixed Repetition            |
| while    | Conditional Repetition      |
| break    | Stop Loop                   |
| continue | Skip Iteration              |

---

# SECTION F — SHORT ANSWER QUESTIONS (10 Marks)

### Question 29

What is control flow?

---

### Question 30

Explain the difference between if and if-else.

---

### Question 31

What is a nested condition?

---

### Question 32

Differentiate between for and while loops.

---

### Question 33

Explain the purpose of break and continue.

---

# SECTION G — CODE READING (10 Marks)

### Question 34

Predict the output.

```python
score = 60

if score >= 50:
    print("Pass")
else:
    print("Fail")
```

**Answer**

```text
Pass
```

---

### Question 35

Predict the output.

```python
for i in range(1, 4):
    print(i)
```

**Answer**

```text
1
2
3
```

---

### Question 36

Predict the output.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

**Answer**

```text
1
2
3
```

---

### Question 37

Predict the output.

```python
for i in range(5):

    if i == 2:
        break

    print(i)
```

**Answer**

```text
0
1
```

---

# SECTION H — DEBUGGING QUESTIONS (5 Marks)

### Question 38

Find and correct the error.

```python
age = 20

if age >= 18
    print("Adult")
```

**Answer**

Missing colon.

Correct:

```python
if age >= 18:
    print("Adult")
```

---

### Question 39

Find and correct the error.

```python
count = 1

while count <= 5:
    print(count)
```

**Answer**

Infinite loop.

Correct:

```python
count = 1

while count <= 5:
    print(count)

    count += 1
```

---

# SECTION I — PRACTICAL PROGRAMMING (15 Marks)

### Question 40

Write a program that asks for a student's score and displays:

* A for 70 and above
* B for 60–69
* C for 50–59
* Fail below 50

---

### Question 41

Write a program that displays the multiplication table of any number entered by the user.

Example:

```text
5 x 1 = 5
5 x 2 = 10
...
5 x 12 = 60
```

---

### Question 42

Write a program that asks a user to enter a password.

If the password is:

```text
python123
```

display:

```text
Access Granted
```

Otherwise display:

```text
Access Denied
```

---

# SECTION J — MINI PROJECT (Bonus 10 Marks)

## Student Grade Checker

Build a program that:

1. Accepts student name.
2. Accepts score.
3. Calculates grade.
4. Displays Pass or Fail.
5. Uses if-elif-else.
6. Allows multiple students using a loop.
7. Stops when the user enters:

```text
quit
```

---

# End-of-Module Challenge

## Number Guessing Game

Build a complete Number Guessing Game that:

* Uses a secret number.
* Allows unlimited guesses.
* Uses a while loop.
* Uses break when the user guesses correctly.
* Displays:

```text
Too High
```

or

```text
Too Low
```

until the correct answer is entered.

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

# End of Module 3 Assessment


