
---

# Module 10 — Git & GitHub Fundamentals (Optional but Highly Recommended)

![Git and GitHub](https://placehold.co/1200x500/1f2937/ffffff.png?text=Module+10:+Git+and+GitHub+Fundamentals)

---

# Learning Objectives

By the end of this module students should be able to:

✓ Understand Version Control

✓ Explain why Git exists

✓ Create Git repositories

✓ Track project changes

✓ Commit code changes

✓ Create GitHub repositories

✓ Push local projects to GitHub

✓ Pull project updates

✓ Work with branches

✓ Resolve basic merge conflicts

✓ Collaborate on projects

✓ Build a professional GitHub portfolio

---

# Chapter 1: What is Version Control?

## The Problem

Imagine you are working on:

```text
student_management.py
```

Day 1:

```text
student_management.py
```

Day 2:

```text
student_management_new.py
```

Day 3:

```text
student_management_final.py
```

Day 4:

```text
student_management_final_final.py
```

Day 5:

```text
student_management_final_final_real.py
```

---

This is how many beginners manage projects.

Very quickly:

```text
Confusion
Lost Work
Deleted Code
No Backup
```

---

# Solution: Version Control

Version Control is a system that tracks changes in files over time.

Think of it like:

```text
Google Docs History
```

but for code.

---

# Real World Analogy

Imagine writing a book.

Version Control allows you to:

✓ Save versions

✓ Restore old versions

✓ See changes

✓ Collaborate with others

---

# What is Git?

Git is a Version Control System.

Created by:

Linus Torvalds

Git helps developers:

✓ Track code changes

✓ Work in teams

✓ Recover deleted work

✓ Build software safely

---

# What is GitHub?

Git and GitHub are NOT the same thing.

---

Git:

```text
Tool on Your Computer
```

GitHub:

```text
Website for Storing Git Repositories
```

Think of:

```text
Git = Microsoft Word

GitHub = Google Drive
```

---

# Git vs GitHub

| Git             | GitHub              |
| --------------- | ------------------- |
| Local Tool      | Cloud Platform      |
| Tracks Changes  | Stores Repositories |
| Works Offline   | Requires Internet   |
| Installed on PC | Website             |

---

# Chapter 2: Installing Git

## Download Git

Visit:

[Git Official Website](https://git-scm.com?utm_source=chatgpt.com)

---

# Verify Installation

Open terminal:

```bash
git --version
```

Example:

```text
git version 2.50.0
```

---

# Chapter 3: Understanding Repositories

## What is a Repository?

A repository (repo) is a project managed by Git.

Example:

```text
student_app/
```

Inside:

```text
student_app/
│
├── app.py
├── students.py
├── grades.py
```

Git tracks everything.

---

# Creating Your First Repository

Create folder:

```text
python_project
```

Open terminal:

```bash
cd python_project
```

Initialize Git:

```bash
git init
```

Output:

```text
Initialized empty Git repository
```

---

# What Happens?

Git creates:

```text
.git/
```

This hidden folder stores project history.

---

# Chapter 4: Git Workflow

The most important concept in Git.

---

# Three Areas

```text
Working Directory
       ↓
Staging Area
       ↓
Repository
```

---

# Step 1: Create a File

```python
print("Hello Git")
```

Save as:

```text
app.py
```

---

# Step 2: Check Status

```bash
git status
```

Output:

```text
Untracked file:
app.py
```

---

# Step 3: Add File

```bash
git add app.py
```

or

```bash
git add .
```

---

# Step 4: Commit Changes

```bash
git commit -m "Initial commit"
```

---

# What is a Commit?

A commit is a snapshot of your project.

Think:

```text
Save Point
```

in a game.

---

# Chapter 5: Viewing Project History

View commits:

```bash
git log
```

Example:

```text
Initial commit
Added login feature
Fixed bug
```

---

# Short Version

```bash
git log --oneline
```

---

# Chapter 6: Working with GitHub

## Create GitHub Account

Visit:

[GitHub Official Website](https://github.com?utm_source=chatgpt.com)

Create account.

---

# Create Repository

Click:

```text
New Repository
```

Example:

```text
student-management-system
```

---

# Connect Local Project

```bash
git remote add origin REPOSITORY_URL
```

Example:

```bash
git remote add origin https://github.com/username/project.git
```

---

# Push Code

```bash
git push -u origin main
```

Project appears on GitHub.

---

# Pull Changes

Download updates:

```bash
git pull origin main
```

---

# Clone Repository

Copy project:

```bash
git clone REPOSITORY_URL
```

Example:

```bash
git clone https://github.com/user/project.git
```

---

# Chapter 7: Branches

## What is a Branch?

A branch allows experimentation without affecting the main code.

---

Default branch:

```text
main
```

---

Create branch:

```bash
git branch login-feature
```

---

Switch branch:

```bash
git checkout login-feature
```

---

Modern method:

```bash
git switch login-feature
```

---

Create and switch:

```bash
git checkout -b login-feature
```

---

View branches:

```bash
git branch
```

---

# Why Branches Matter

```text
main
│
├── Login Feature
│
├── Payment Feature
│
└── Dashboard Feature
```

Developers work independently.

---

# Chapter 8: Merging Branches

Switch to:

```bash
git checkout main
```

Merge:

```bash
git merge login-feature
```

Changes combine.

---

# Merge Conflict

Occurs when:

Two people edit the same line.

Example:

```python
name = "John"
```

Person A changes:

```python
name = "Mary"
```

Person B changes:

```python
name = "David"
```

Git cannot decide.

Developer resolves manually.

---

# Chapter 9: .gitignore

Some files should NOT be uploaded.

Examples:

```text
venv/
__pycache__/
.env
```

---

Create:

```text
.gitignore
```

Example:

```text
venv/
__pycache__/
.env
```

Git ignores them.

---

# Why Ignore Files?

Avoid uploading:

✓ Virtual Environments

✓ Passwords

✓ Cache Files

✓ Temporary Files

---

# Chapter 10: GitHub Portfolio

GitHub is your developer CV.

Recruiters often check:

```text
GitHub Profile
```

before hiring.

---

# What Should Be on GitHub?

✓ Python Projects

✓ Student Projects

✓ OOP Projects

✓ Contact Management System

✓ Banking System

✓ Django Projects

---

# Good Repository Example

```text
Student Management System

README.md

Features:
- Add Students
- Calculate Grades
- Generate Reports

Built With:
- Python
- OOP
```

---

# Practical 1

## Create Your First Repository

Tasks:

1. Create project folder
2. Initialize Git
3. Create app.py
4. Commit changes
5. View commit history

---

# Practical 2

## Push Project to GitHub

Tasks:

1. Create GitHub account
2. Create repository
3. Connect local repository
4. Push code

---

# Practical 3

## Branching Exercise

Tasks:

1. Create branch:

```bash
git checkout -b feature-login
```

2. Create login.py

3. Commit changes

4. Merge into main

---

# Practical 4

## Create Professional GitHub Portfolio

Upload:

* Calculator App
* Student Class Project
* Employee Payroll Project
* Contact Management System

Add README files.

---

# Most Important Git Commands

| Command                 | Purpose           |
| ----------------------- | ----------------- |
| git init                | Create Repository |
| git status              | Check Status      |
| git add .               | Stage Files       |
| git commit -m "message" | Save Snapshot     |
| git log                 | View History      |
| git branch              | View Branches     |
| git checkout -b name    | Create Branch     |
| git merge               | Merge Branch      |
| git clone               | Copy Repository   |
| git pull                | Download Updates  |
| git push                | Upload Changes    |

---

# Common Beginner Mistakes

### Forgetting git add

Wrong:

```bash
git commit -m "Update"
```

without:

```bash
git add .
```

---

### Uploading venv

Wrong:

```text
venv/
```

inside repository.

Always use:

```text
.gitignore
```

---

### Working Directly on Main

Better:

```text
feature-login
feature-payment
```

branches.

---

### Not Writing Commit Messages

Bad:

```bash
git commit -m "update"
```

Good:

```bash
git commit -m "Added student grade calculator"
```

---

# End-of-Module Project

## Student Management System with Git

Requirements:

1. Create repository
2. Commit project
3. Create feature branch
4. Add new feature
5. Merge branch
6. Push to GitHub
7. Create README

---

# Module Summary

In this module we learned:

✓ Version Control

✓ Git

✓ GitHub

✓ Repositories

✓ Commits

✓ Push & Pull

✓ Clone

✓ Branches

✓ Merge

✓ Merge Conflicts

✓ .gitignore

✓ GitHub Portfolio

✓ Collaboration Workflows

This module is often the difference between a hobby programmer and a professional developer. Every software company—from startups to large tech organizations—expects developers to understand Git and GitHub.

---
