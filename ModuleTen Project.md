# Module 10 Project

## Project 010 — Professional GitHub Portfolio Deployment

### Difficulty Level

🟡 Beginner to Intermediate

---

# Project Story

## EduTech Africa Ltd — Developer Portfolio Submission

You have now built several Python projects, including:

* Company Welcome Banner
* Employee Information System
* Employee Performance Evaluation System
* Employee Directory System
* HR Utility Toolkit
* Employee Records Database
* Employee Management System
* Enterprise Payroll System
* HR Management Package

Now your manager wants you to present your work professionally.

In the real world, employers, clients, and technical recruiters want to see proof of your skills.

Your task is to organize your projects with Git, upload them to GitHub, and create a professional developer portfolio.

---

# Project Goal

By the end of this project, students should have:

* A GitHub account
* At least 5 uploaded repositories
* A clean README file for each project
* Commit history showing progress
* A main portfolio repository
* A professional GitHub profile

---

# Business Requirement

EduTech Africa Ltd wants every junior developer to submit their project portfolio.

Each student must show:

1. Source code
2. Project description
3. Features
4. Technologies used
5. How to run the project
6. Screenshots if available
7. Git commit history

---

# Concepts Used

Students must use:

* Git
* GitHub
* Repository creation
* Commits
* Branches
* Push
* Pull
* Clone
* README.md
* .gitignore

---

# Student Task

Create a GitHub portfolio containing all major course projects.

---

# Required Repositories

Students should create repositories for:

```text
company-welcome-banner
employee-information-system
employee-performance-evaluation-system
employee-directory-system
hr-utility-toolkit
employee-records-database
employee-management-system
enterprise-payroll-system
hr-management-package
```

---

# Main Portfolio Repository

Create one main repository called:

```text
python-portfolio
```

This repository should contain links to all other projects.

---

# Sample Folder Structure

```text
python-portfolio/
│
├── README.md
├── screenshots/
│
└── project-links.md
```

---

# Step 1 — Create GitHub Account

Go to:

```text
https://github.com
```

Create an account using a professional username.

Good examples:

```text
adewale-dev
adewale-python
adewale-oladiti
```

Avoid usernames like:

```text
babyboy123
moneyking999
```

---

# Step 2 — Initialize Git in a Project

Open your project folder.

Example:

```text
employee-directory-system
```

Run:

```bash
git init
```

---

# Step 3 — Check Status

```bash
git status
```

This shows files that Git is tracking or not tracking.

---

# Step 4 — Create .gitignore

Create a file named:

```text
.gitignore
```

Add:

```text
venv/
__pycache__/
.env
*.pyc
```

This prevents unnecessary files from being uploaded.

---

# Step 5 — Stage Files

```bash
git add .
```

This prepares files for saving.

---

# Step 6 — Commit Files

```bash
git commit -m "Initial project commit"
```

A commit is like a save point.

---

# Step 7 — Create GitHub Repository

On GitHub:

1. Click New Repository
2. Enter repository name
3. Do not initialize with README if your local project already has one
4. Click Create Repository

---

# Step 8 — Connect Local Project to GitHub

```bash
git remote add origin https://github.com/username/repository-name.git
```

Example:

```bash
git remote add origin https://github.com/adewale-dev/employee-directory-system.git
```

---

# Step 9 — Push Project

```bash
git branch -M main
git push -u origin main
```

---

# Step 10 — Create README.md

Every project must include:

```text
README.md
```

---

# README Template

````markdown
# Employee Directory System

## Description

A Python console application for managing employee records using lists, dictionaries, sets, loops, and conditional statements.

## Features

- Add employee
- View all employees
- Search employee by ID
- View departments
- Count employees by department

## Technologies Used

- Python
- Git
- GitHub

## How to Run

```bash
python employee_directory.py
````

## Skills Demonstrated

* Lists
* Dictionaries
* Sets
* Loops
* Conditional statements
* Menu-driven programming

## Author

Your Name

````

---

# Branching Task

Create a new branch:

```bash
git checkout -b update-readme
````

Update the README file.

Stage and commit:

```bash
git add .
git commit -m "Updated README documentation"
```

Switch back to main:

```bash
git checkout main
```

Merge:

```bash
git merge update-readme
```

Push:

```bash
git push
```

---

# Portfolio README Example

```markdown
# My Python Portfolio

Welcome to my Python portfolio.

This portfolio contains projects I built while learning Python from beginner level to object-oriented programming and software packaging.

## Projects

### 1. Company Welcome Banner
A beginner Python project that displays formatted company welcome messages.

### 2. Employee Information System
A Python program that collects employee details and calculates annual salary.

### 3. Employee Performance Evaluation System
A decision-making system that evaluates employee performance using conditions and loops.

### 4. Employee Directory System
A collection-based employee management application using lists, dictionaries, and sets.

### 5. HR Utility Toolkit
A modular Python project that uses functions to organize HR operations.

### 6. Employee Records Database
A JSON-powered employee record system with persistent storage.

### 7. Employee Management System
An object-oriented employee system using classes and inheritance.

### 8. Enterprise Payroll System
An advanced OOP payroll system using abstract classes, polymorphism, and operator overloading.

### 9. HR Management Package
A reusable Python package for HR operations.

## Skills Covered

- Python fundamentals
- Control flow
- Data structures
- Functions
- File handling
- JSON and CSV
- OOP
- Advanced OOP
- Git and GitHub
- Software documentation

## Author

Your Name
```

---

# Project Checklist

Before submission, confirm:

☐ I created a GitHub account

☐ I installed Git

☐ I initialized Git in my projects

☐ I created commits

☐ I pushed projects to GitHub

☐ I created README files

☐ I created .gitignore files

☐ I used at least one branch

☐ I created a main portfolio repository

☐ I shared my GitHub portfolio link

---

# Instructor Solution Standard

A complete submission should include:

```text
GitHub Profile Link:
https://github.com/username

Portfolio Repository:
https://github.com/username/python-portfolio

Project Repositories:
1. company-welcome-banner
2. employee-information-system
3. employee-performance-evaluation-system
4. employee-directory-system
5. hr-utility-toolkit
6. employee-records-database
7. employee-management-system
8. enterprise-payroll-system
9. hr-management-package
```

---

# Professional Upgrade Challenge

Improve your GitHub profile by adding:

* Profile photo
* Professional bio
* Location
* Skills
* Pinned repositories
* GitHub profile README

---

# GitHub Profile README Challenge

Create a special repository with your GitHub username.

Example:

```text
adewale-dev/adewale-dev
```

Add a README.md file.

Example:

```markdown
# Hi, I'm Adewale

I am a Python developer learning software engineering by building real-world business applications.

## Skills

- Python
- Git
- GitHub
- OOP
- File Handling
- JSON
- CSV

## Featured Projects

- Employee Directory System
- Enterprise Payroll System
- HR Management Package
```

---

# Super Challenge

Add screenshots to your repositories.

Suggested screenshots:

* Program running in terminal
* Output report
* GitHub repository page
* Project folder structure

---

# Expert Challenge

Record a short project demo video.

In the video, explain:

1. What the project does
2. What Python concepts you used
3. How to run the project
4. What you learned

Upload the video link in your README.

---

# Real-World Connection

This project teaches students how developers present their work professionally.

In real hiring situations, employers may ask:

* Can I see your GitHub?
* What projects have you built?
* Can you explain your code?
* Do you understand version control?
* Can you document your work?

This project prepares students for those questions.

---

# Portfolio Section

## Project Name

Professional GitHub Portfolio Deployment

---

## What I Built

A professional GitHub portfolio containing multiple Python projects, complete documentation, version control history, README files, and organized repositories.

---

## Skills Demonstrated

* Git
* GitHub
* Version Control
* Repository Management
* Branching
* Commit History
* Documentation
* Technical Portfolio Building

---

## Resume Description

Built and documented a professional GitHub portfolio containing multiple Python projects, demonstrating version control, repository management, technical documentation, and beginner-to-intermediate software development skills.

---

## Final Deliverable

Students must submit:

```text
GitHub Profile Link
Portfolio Repository Link
At least 5 Project Repository Links
```

---

# What Students Have Achieved

After completing this project, students have:

* Published their projects online
* Built a professional GitHub presence
* Practiced version control
* Created documentation
* Prepared a portfolio for internships, jobs, and freelance opportunities

---

