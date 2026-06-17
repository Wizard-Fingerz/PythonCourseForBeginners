# Module 1: Introduction to Computing & Python

> **Lesson Goal:** By the end of this module, students should understand what programming means, what Python is used for, how to install Python, how to set up a coding environment, how to write their first script, and how to identify basic errors.

---

## 1. What is Programming?

Programming is the process of giving instructions to a computer so that it can perform specific tasks.

Think of a computer as a very intelligent but obedient machine. It can do almost anything, but only if you tell it exactly what to do.
![alt text](image-1.png)![alt text](image-2.png)![alt text](image-3.png)
For example, a computer can:

* Open a web page
* Calculate a student's result
* Send an email
* Build a website
* Analyze business data

All these tasks are possible because programmers write instructions called **code**.

![Programming Input Process Output](https://placehold.co/1200x500/0f172a/ffffff.png?text=INPUT+%E2%86%92+PROCESS+%E2%86%92+OUTPUT%0AProgramming+means+giving+clear+instructions+to+a+computer)

**Figure 1:** Programming follows a simple pattern: the computer receives input, processes it, and gives output.

### Real-Life Example

Imagine you want to make a cup of tea.

The steps might be:

1. Boil water
2. Put tea bag in cup
3. Pour hot water
4. Add sugar
5. Stir

These instructions are called an **algorithm**.

In programming, we write similar instructions for computers.

![Algorithm Example](https://placehold.co/1200x600/f8fafc/0f172a.png?text=Algorithm+Example%0ABoil+Water+%E2%86%92+Put+Tea+Bag+%E2%86%92+Pour+Water+%E2%86%92+Add+Sugar+%E2%86%92+Stir)

**Figure 2:** An algorithm is a step-by-step process for solving a problem.

### Who is a Programmer?

A programmer is someone who writes code to solve problems using a computer.

Examples of programmers include:

* Web Developers
* Software Engineers
* Data Scientists
* AI Engineers
* Cybersecurity Experts

---

## 2. What is Python?

Python is a high-level programming language. A programming language is a language humans use to give instructions to computers.

Python is one of the most popular programming languages because it is:

* Easy to learn
* Easy to read
* Powerful
* Flexible
* Useful in many career paths

### Why Learn Python?

Python is beginner-friendly because its syntax looks similar to plain English.

Example:

```python
print("Hello World")
```

Even without programming knowledge, most people can guess that this code prints **Hello World** on the screen.

![Python Simple Syntax](https://placehold.co/1200x550/1e293b/ffffff.png?text=Python+is+Beginner+Friendly%0Aprint(%22Hello+World%22)+%E2%86%92+Hello+World)

**Figure 3:** Python code is usually easy to read and understand.

### Companies and Products That Use Python

Python is used by many technology companies and products in areas like search engines, social media, automation, data analysis, and artificial intelligence.

Examples include:

* Google
* Netflix
* Instagram
* Spotify
* Dropbox

---

# 3. Python Use Cases

Python can be used in many industries.

![Python Use Cases](https://placehold.co/1200x650/e0f2fe/0f172a.png?text=Python+Use+Cases%0AAI+%7C+Web+Development+%7C+Cybersecurity+%7C+Data+Analysis+%7C+Automation)

**Figure 4:** Python is useful in many fields, from web development to artificial intelligence.

## A. Artificial Intelligence (AI)

Python is widely used for AI and Machine Learning.

Examples:

* Chatbots
* Recommendation systems
* Face recognition
* Voice assistants

Real-life examples include:

* ChatGPT-like systems
* Siri-like assistants
* Netflix-style recommendations

---

## B. Web Development

Python is used to build websites and web applications.

Popular Python web frameworks include:

* Django
* Flask
* FastAPI

Examples of web applications:

* E-commerce platforms
* School portals
* Banking systems
* Hospital management systems

---

## C. Cybersecurity

Python helps cybersecurity professionals automate security tasks.

Examples:

* Network scanning
* Log analysis
* Password checking
* Security monitoring

---

## D. Data Analysis

Organizations collect large amounts of data every day. Python helps analyze data and discover useful insights.

Examples:

* Sales reports
* Financial analysis
* Student performance analysis
* Customer behavior analysis

---

## E. Automation

Python can automate repetitive tasks.

Examples:

* Sending emails automatically
* Renaming files
* Generating reports
* Updating spreadsheets

Automation saves time and reduces human error.

---

# 4. Installing Python

Before writing Python programs, we must install Python on our computer.

![Python Installation Guide](https://placehold.co/1200x550/fff7ed/0f172a.png?text=Python+Installation+Process%0AVisit+Website+%E2%86%92+Download+Python+%E2%86%92+Install+%E2%86%92+Verify+Installation)

**Figure 5:** Python installation follows four basic steps.

## Step 1: Visit the Python Website

Go to:

https://www.python.org

![Python Website](https://placehold.co/1200x600/ffffff/0f172a.png?text=Step+1%3A+Open+www.python.org%0AClick+Downloads+to+get+Python)

**Figure 6:** Open the official Python website and locate the download section.

## Step 2: Download Python

Choose the latest stable version.

Example:

Python 3.x

![Download Python](https://placehold.co/1200x600/dbeafe/0f172a.png?text=Step+2%3A+Download+Python+3.x%0AChoose+the+latest+stable+version+for+your+operating+system)

**Figure 7:** Download the correct Python version for your operating system.

## Step 3: Run the Installer

During installation, make sure you check:

☑ **Add Python to PATH**

This is very important because it allows your computer to recognize Python from the command line.

Then click:

**Install Now**

![Add Python to PATH](https://placehold.co/1200x600/fef2f2/991b1b.png?text=Important%3A+Tick+Add+Python+to+PATH%0AThen+click+Install+Now)

**Figure 8:** Beginners often forget this step. Always tick **Add Python to PATH** before installing.

## Step 4: Verify Installation

Open Command Prompt on Windows or Terminal on Mac.

Type:

```bash
python --version
```

or

```bash
python3 --version
```

You should see something like:

```bash
Python 3.13.0
```

This confirms successful installation.

![Verify Python Installation](https://placehold.co/1200x600/0f172a/ffffff.png?text=Command+Prompt+or+Terminal%0Apython+--version%0AOutput%3A+Python+3.x.x)

**Figure 9:** If Python is installed correctly, the terminal will display the installed Python version.

---

# 5. Introduction to Jupyter Notebook

Jupyter Notebook is a tool that allows us to write and run Python code inside a web browser.

It is widely used for:

* Learning Python
* Data Science
* Machine Learning
* Research

### Advantages

* Easy to use
* Interactive
* Supports text and code together
* Excellent for beginners

### Example

```python
print("Welcome to Python")
```

The output appears immediately below the code.

![Jupyter Notebook Interface](https://placehold.co/1200x650/f8fafc/0f172a.png?text=Jupyter+Notebook%0ACode+Cell%3A+print(%22Welcome+to+Python%22)%0AOutput%3A+Welcome+to+Python)

**Figure 10:** Jupyter Notebook allows students to write code and see the result immediately.

---

# 6. Setting Up IDEs

## What is an IDE?

IDE means:

**Integrated Development Environment**

An IDE is software that helps programmers write code more efficiently.

Think of it as a digital workspace for programmers.

![IDE Workspace](https://placehold.co/1200x600/e2e8f0/0f172a.png?text=IDE+Workspace%0ACode+Editor+%7C+Terminal+%7C+File+Explorer+%7C+Extensions)

**Figure 11:** An IDE combines the tools a programmer needs in one workspace.

---

## A. Visual Studio Code (VS Code)

VS Code is recommended for beginners.

Advantages:

* Free
* Fast
* Lightweight
* Supports many programming languages
* Has many useful extensions

### Installation

1. Download VS Code
2. Install the Python extension
3. Create a Python file
4. Start coding

![VS Code Setup](https://placehold.co/1200x650/dbeafe/0f172a.png?text=VS+Code+Setup%0A1.+Download+VS+Code%0A2.+Install+Python+Extension%0A3.+Create+hello.py%0A4.+Run+Your+Code)

**Figure 12:** VS Code is a good beginner-friendly editor for Python.

---

## B. PyCharm

PyCharm is a professional Python IDE.

Advantages:

* Excellent debugging tools
* Smart code suggestions
* Great for large projects

Disadvantages:

* Uses more computer memory
* Slightly harder for beginners

---

## C. Jupyter Notebook

Jupyter Notebook is best for:

* Learning
* Experimenting
* Data Science

It is not ideal for building large software projects.

---

# 7. Writing Your First Python Script

The traditional first program is called:

**Hello World**

Create a file named:

```python
hello.py
```

Write:

```python
print("Hello World")
```

Run it.

Output:

```text
Hello World
```

Congratulations! You have written your first Python program.

![Hello World Process](https://placehold.co/1200x650/ecfdf5/064e3b.png?text=Your+First+Python+Script%0ACreate+hello.py+%E2%86%92+Write+print(%22Hello+World%22)+%E2%86%92+Run+%E2%86%92+See+Output)

**Figure 13:** The first script teaches students how to create, write, run, and view program output.

---

# 8. Understanding Python Execution Flow

Execution flow means the order in which Python executes code.

Python executes code from top to bottom.

Example:

```python
print("Step 1")
print("Step 2")
print("Step 3")
```

Output:

```text
Step 1
Step 2
Step 3
```

Python follows the instructions exactly in the order they appear.

![Python Execution Flow](https://placehold.co/1200x650/fefce8/713f12.png?text=Python+Execution+Flow%0ALine+1+%E2%86%93%0ALine+2+%E2%86%93%0ALine+3+%E2%86%93%0AOutput)

**Figure 14:** Python reads code line by line from top to bottom.

### Another Example

```python
name = "Adewale"
print(name)
print("Welcome")
```

Output:

```text
Adewale
Welcome
```

Python reads line by line from top to bottom.

---

# 9. Understanding Errors and Debugging Basics

Errors happen when Python cannot understand or execute our code.

Making mistakes is normal. Even experienced developers make mistakes every day.

The important skill is learning how to find and fix them.

This process is called:

**Debugging**

![Debugging Process](https://placehold.co/1200x600/f3e8ff/581c87.png?text=Debugging+Process%0ARead+Error+%E2%86%92+Find+Line+%E2%86%92+Understand+Cause+%E2%86%92+Fix+Code+%E2%86%92+Run+Again)

**Figure 15:** Debugging is the process of finding and fixing errors in code.

---

## Common Error 1: Syntax Error

A syntax error happens when Python cannot understand the structure of your code.

Example:

```python
print("Hello World"
```

Output:

```text
SyntaxError
```

Cause:

Missing closing bracket.

Correct version:

```python
print("Hello World")
```

![Syntax Error](https://placehold.co/1200x600/fee2e2/7f1d1d.png?text=SyntaxError%0AProblem%3A+Missing+closing+bracket%0AFix%3A+print(%22Hello+World%22))

**Figure 16:** Syntax errors usually happen when Python cannot understand the code structure.

---

## Common Error 2: Name Error

A name error happens when you try to use something that has not been created yet.

Example:

```python
print(age)
```

Output:

```text
NameError
```

Cause:

The variable `age` does not exist.

Correct version:

```python
age = 25
print(age)
```

![Name Error](https://placehold.co/1200x600/ffedd5/7c2d12.png?text=NameError%0AProblem%3A+Variable+was+not+created%0AFix%3A+age+%3D+25+then+print(age))

**Figure 17:** Name errors happen when Python sees a name it does not recognize.

---

## Common Error 3: Type Error

A type error happens when Python cannot perform an operation on incompatible data types.

Example:

```python
"10" + 5
```

Output:

```text
TypeError
```

Cause:

Python cannot add text and numbers together.

Correct version:

```python
int("10") + 5
```

Output:

```text
15
```

![Type Error](https://placehold.co/1200x600/dbeafe/1e3a8a.png?text=TypeError%0AProblem%3A+Text+%2B+Number%0AFix%3A+Convert+%2210%22+to+integer+first)

**Figure 18:** Type errors happen when the data types do not match the operation.

---

## Debugging Tips

1. Read error messages carefully.
2. Check spelling mistakes.
3. Verify brackets are closed.
4. Check indentation.
5. Test code in small parts.
6. Use `print()` statements to inspect values.

Remember:

Every programmer spends a large part of their career fixing errors.

Debugging is not a sign of failure; it is part of programming.

---

# Class Practical Activities

## Practical 1: Print Your Details

Write a program that prints your name, age, school, and career goal.

Example:

```python
print("Name: Adewale")
print("Age: 25")
print("Career Goal: Software Engineer")
```

## Practical 2: Hello Python

Write a program that displays:

```text
Welcome to Python Programming
```

## Practical 3: Identify the Error

Find and correct the error in this code:

```python
print("I am learning Python"
```

---

# Module Summary

At the end of this lesson, you should be able to:

✓ Explain what programming is

✓ Describe Python and its applications

✓ Install Python successfully

✓ Set up VS Code and Jupyter Notebook

✓ Write your first Python program

✓ Understand how Python executes code

✓ Identify common programming errors

✓ Apply basic debugging techniques

Programming is simply solving problems by giving clear instructions to a computer. Python makes that process easier because of its simple and readable syntax.
