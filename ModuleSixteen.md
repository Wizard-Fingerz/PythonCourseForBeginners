# Module 16 — Deployment, Portfolio & Career Readiness

## Phase 2: Software Engineering Specialization

### Final Project

# ExpenseFlow — Production Deployment

---

# Module Overview

Congratulations!

By this point students have built:

✓ Django Project

✓ Expense Models

✓ Categories

✓ CRUD Operations

✓ Authentication

✓ Dashboard

✓ Reports

✓ Analytics

ExpenseFlow is now a complete application.

However, it still has one major problem.

The application only works on the student's computer.

Nobody else can use it.

In this module, students will deploy ExpenseFlow to the internet and prepare it for employers, recruiters, clients, and portfolio reviews.

---

# Learning Objectives

By the end of this module, students should be able to:

✓ Understand deployment

✓ Understand production environments

✓ Deploy a Django application

✓ Use GitHub professionally

✓ Configure production settings

✓ Create requirements files

✓ Use environment variables

✓ Connect PostgreSQL

✓ Create project documentation

✓ Present projects professionally

---

# What Is Deployment?

Deployment means:

```text id="m16_001"
Moving Application

From

Your Computer

To

The Internet
```

---

# Before Deployment

Only you can access:

```text id="m16_002"
http://127.0.0.1:8000
```

---

# After Deployment

Anyone can access:

```text id="m16_003"
https://expenseflow.onrender.com
```

---

# Real-World Development Lifecycle

```text id="m16_004"
Build
 ↓

Test
 ↓

Deploy
 ↓

Users
```

---

# Production vs Development

## Development

Used while building software.

```python id="m16_005"
DEBUG = True
```

---

## Production

Used when users access the application.

```python id="m16_006"
DEBUG = False
```

---

# Why Production Matters

Production provides:

✓ Security

✓ Reliability

✓ Public Access

✓ Scalability

---

# Preparing ExpenseFlow For Deployment

---

# Step 1 — Create requirements.txt

Inside project:

```bash id="m16_007"
pip freeze > requirements.txt
```

Example:

```text id="m16_008"
Django==5.2.1

asgiref==3.8.1

sqlparse==0.5.3
```

---

# Why requirements.txt?

Allows hosting platforms to install dependencies automatically.

---

# Step 2 — Create .gitignore

Create:

```text id="m16_009"
.gitignore
```

Add:

```text id="m16_010"
venv/

__pycache__/

.env

db.sqlite3

*.pyc
```

---

# Why .gitignore?

Prevents:

* Secrets
* Temporary files
* Virtual environments

from being uploaded.

---

# Step 3 — Create Environment Variables

Never store:

```python id="m16_011"
SECRET_KEY
```

inside GitHub.

---

Bad:

```python id="m16_012"
SECRET_KEY = "abc123"
```

---

Good:

```python id="m16_013"
SECRET_KEY = os.getenv(
    "SECRET_KEY"
)
```

---

# Install python-dotenv

```bash id="m16_014"
pip install python-dotenv
```

---

# Create .env

```text id="m16_015"
SECRET_KEY=your-secret-key

DEBUG=False
```

---

# GitHub Setup

---

# Step 4 — Create Repository

Repository Name:

```text id="m16_016"
expenseflow
```

---

# Initialize Git

```bash id="m16_017"
git init
```

---

# Stage Files

```bash id="m16_018"
git add .
```

---

# Commit

```bash id="m16_019"
git commit -m "ExpenseFlow Final Project"
```

---

# Connect GitHub

```bash id="m16_020"
git remote add origin

https://github.com/username/expenseflow.git
```

---

# Push

```bash id="m16_021"
git push -u origin main
```

---

# ExpenseFlow Repository Structure

```text id="m16_022"
expenseflow/

├── expenses/
│
├── templates/
│
├── static/
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── manage.py
```

---

# Hosting Options

Recommended:

### Beginner Friendly

* Render
* PythonAnywhere

---

### Intermediate

* Railway
* Fly.io

---

# Recommended Choice

For students:

```text id="m16_023"
Render
```

because:

✓ Free Tier

✓ Easy Setup

✓ GitHub Integration

✓ PostgreSQL Support

---

# Database Upgrade

Current:

```text id="m16_024"
SQLite
```

Production:

```text id="m16_025"
PostgreSQL
```

---

# Why PostgreSQL?

Professional applications use:

* PostgreSQL
* MySQL
* SQL Server

Not SQLite.

---

# Install PostgreSQL Driver

```bash id="m16_026"
pip install psycopg2-binary
```

---

# Update Requirements

```bash id="m16_027"
pip freeze > requirements.txt
```

---

# Deployment Flow

```text id="m16_028"
GitHub
 ↓

Render
 ↓

Build
 ↓

Deploy
 ↓

Live URL
```

---

# Testing Before Deployment

Verify:

✓ Registration Works

✓ Login Works

✓ Logout Works

✓ Add Expense Works

✓ Edit Expense Works

✓ Delete Expense Works

✓ Reports Work

✓ Dashboard Works

---

# Creating README

Every project must include:

```text id="m16_029"
README.md
```

---

# ExpenseFlow README Template

```markdown id="m16_030"
# ExpenseFlow

A Django-based personal expense tracking application.

## Features

- User Registration
- Login
- Logout
- Add Expense
- Edit Expense
- Delete Expense
- Categories
- Dashboard
- Reports

## Technologies

- Python
- Django
- SQLite
- PostgreSQL
- HTML
- CSS

## Installation

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

## Author

Your Name
```

---

# Screenshots Section

Add screenshots:

```text id="m16_031"
Dashboard

Expense List

Reports

Login Page
```

inside README.

---

# Building Portfolio Page

Students should create:

```text id="m16_032"
Python Portfolio Repository
```

Include:

* HR Management System
* ExpenseFlow
* GitHub Profile

---

# Creating LinkedIn Project Entry

Example:

```text id="m16_033"
ExpenseFlow

Developed a full-stack expense management web application using Django featuring authentication, expense tracking, reporting, analytics, and PostgreSQL database integration.
```

---

# Demo Presentation

Students should prepare:

### 2–5 Minute Demo

Show:

1. Registration
2. Login
3. Add Expense
4. Edit Expense
5. Dashboard
6. Reports

---

# Final Project Assessment

Students must demonstrate:

✓ Django Setup

✓ Models

✓ Database Design

✓ CRUD

✓ Authentication

✓ Reporting

✓ Deployment

✓ Documentation

---

# Capstone Deliverables

Students must submit:

### Source Code

```text id="m16_034"
GitHub Repository
```

---

### Live Application

```text id="m16_035"
Production URL
```

---

### Documentation

```text id="m16_036"
README.md
```

---

### Demo Video

```text id="m16_037"
2–5 Minute Walkthrough
```

---

# ExpenseFlow Final Milestone

Students now have:

✓ Real Django Project

✓ Full Authentication

✓ Database Design

✓ CRUD Operations

✓ Reporting

✓ Analytics

✓ Deployment

✓ Portfolio Project

---

# Portfolio Section

## Project Name

ExpenseFlow — Personal Expense Tracking System

---

## What I Built

A full-stack Django web application that allows users to register accounts, track expenses, categorize spending, generate reports, and monitor financial activity through a dashboard.

---

## Skills Demonstrated

* Python
* Django
* PostgreSQL
* Authentication
* CRUD Operations
* Database Design
* Deployment
* Git & GitHub
* Software Engineering

---

## Resume Description

Designed, developed, and deployed ExpenseFlow, a full-stack Django expense tracking platform featuring user authentication, expense management, analytics dashboards, reporting, and PostgreSQL database integration.

---

# Graduation Outcome

After completing the entire program, students will have built:

### Python Fundamentals Track

* 10 Python Projects
* HR Management System

---

### Software Engineering Specialization

* ExpenseFlow Web Application

---

### Professional Portfolio

* GitHub Profile
* LinkedIn Projects
* Live Application
* Technical Documentation

---

# Career Paths After Graduation

Students are now prepared for:

✓ Junior Python Developer

✓ Junior Django Developer

✓ Backend Developer Intern

✓ Software Engineering Intern

✓ Freelance Python Developer

✓ Technical Startup Founder

---

# What's Next?

Advanced Tracks (Optional):

### Track A

Django REST Framework (APIs)

---

### Track B

React + Django

---

### Track C

Cloud & DevOps

---

### Track D

AI-Powered Django Applications

---

## Final Message

You started with:

```python
print("Hello World")
```

And finished with:

```text
A Deployed Production Web Application
```

That transformation is what makes a software engineer.
