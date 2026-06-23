# Module 11 — Django Foundations & ExpenseFlow Setup

## Phase 2: Software Engineering Specialization

### Project

# ExpenseFlow — Personal Expense Tracking System

---

# Module Overview

Welcome to the second phase of the program.

In Modules 1–10, students learned:

* Python Fundamentals
* Data Structures
* Functions
* File Handling
* Object-Oriented Programming
* Git & GitHub

Now students will learn how professional software engineers use Python to build web applications.

This module introduces Django and lays the foundation for the ExpenseFlow application.

---

# Learning Objectives

By the end of this module, students should be able to:

✓ Explain what a web application is

✓ Differentiate frontend and backend

✓ Understand client-server architecture

✓ Explain HTTP requests and responses

✓ Understand what Django is

✓ Explain Django's MVT architecture

✓ Install Django

✓ Create a Django project

✓ Run a Django development server

✓ Understand Django project structure

✓ Create a Django app

✓ Build their first Django page

---

# What Is a Web Application?

A web application is software that runs inside a web browser.

Examples:

* Facebook
* Instagram
* X (Twitter)
* YouTube
* Jumia
* Amazon
* Paystack

Instead of installing software:

```text
Computer
↓
Install Application
```

users simply visit:

```text
Website URL
↓
Application Opens
```

---

# Understanding Client and Server

## Client

The client is:

```text
Browser
Phone
Tablet
Laptop
```

Examples:

* Chrome
* Firefox
* Safari
* Edge

---

## Server

The server is:

```text
Computer
Running Application Logic
```

It processes requests and returns responses.

---

# Client-Server Flow

```text
User
 ↓
Browser
 ↓
Request
 ↓
Django Server
 ↓
Database
 ↓
Response
 ↓
Browser
```

---

# Real Example

Imagine you log into Facebook.

Step 1:

```text
You Click Login
```

---

Step 2:

Browser sends request:

```text
POST /login
```

---

Step 3:

Server checks database.

---

Step 4:

Server responds:

```text
Login Successful
```

---

Step 5:

Dashboard appears.

---

# Frontend vs Backend

## Frontend

What users see.

Examples:

* Buttons
* Forms
* Pages
* Navigation

Technologies:

```text
HTML
CSS
JavaScript
```

---

## Backend

What users don't see.

Examples:

* Authentication
* Business Logic
* Databases
* Security

Technologies:

```text
Python
Django
Node.js
PHP
Java
```

---

# What Is Django?

Django is a Python web framework.

A framework is a collection of tools that helps developers build applications faster.

Instead of building everything from scratch:

```text
Authentication
Database
Admin Panel
Security
Forms
```

Django already provides them.

---

# Why Django?

Advantages:

✓ Fast Development

✓ Secure

✓ Scalable

✓ Batteries Included

✓ Used by Large Companies

---

# Companies That Use Django

Instagram

Pinterest

Mozilla

Disqus

---

# Django Architecture

Django uses:

```text
MVT
```

Model

View

Template

---

# MVT Architecture

```text
User
 ↓
Template
 ↓
View
 ↓
Model
 ↓
Database
```

---

# Model

Models handle data.

Example:

```python
Expense
Category
User
```

Models communicate with databases.

---

# View

Views handle application logic.

Example:

```python
Show Dashboard
Save Expense
Delete Expense
```

---

# Template

Templates handle presentation.

Example:

```html
Dashboard Page
Expense List
Login Form
```

---

# Installing Django

Verify Python Installation:

```bash
python --version
```

Expected:

```text
Python 3.x.x
```

---

# Creating Virtual Environment

Create:

```bash
python -m venv venv
```

---

# Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

### Mac/Linux

```bash
source venv/bin/activate
```

---

# Install Django

```bash
pip install django
```

Verify Installation:

```bash
django-admin --version
```

---

# Creating ExpenseFlow Project

Create project:

```bash
django-admin startproject expenseflow
```

---

# Project Structure

```text
expenseflow/

├── manage.py
│
├── expenseflow/
│   │
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
```

---

# Understanding Project Files

## manage.py

Used for:

```bash
runserver
makemigrations
migrate
createsuperuser
```

---

## settings.py

Project configuration.

Contains:

* Installed apps
* Database settings
* Security settings

---

## urls.py

Application routing.

Example:

```text
/dashboard/
/expenses/
/login/
```

---

## wsgi.py

Used in deployment.

---

## asgi.py

Used for asynchronous applications.

---

# Running the Server

Move into project:

```bash
cd expenseflow
```

Run:

```bash
python manage.py runserver
```

---

# Open Browser

Visit:

```text
http://127.0.0.1:8000
```

You should see:

```text
The install worked successfully!
Congratulations!
```

This is your first Django application.

---

# Creating Your First App

Create app:

```bash
python manage.py startapp expenses
```

---

# New Structure

```text
expenseflow/

├── expenses/
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── migrations/
```

---

# Register App

Open:

```python
settings.py
```

Add:

```python
INSTALLED_APPS = [
    ...
    "expenses",
]
```

---

# Creating First View

Open:

```python
views.py
```

Add:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "Welcome To ExpenseFlow"
    )
```

---

# Configure URL

Open:

```python
urls.py
```

Add:

```python
from expenses.views import home

urlpatterns = [
    path("", home),
]
```

---

# Test Page

Visit:

```text
http://127.0.0.1:8000
```

Output:

```text
Welcome To ExpenseFlow
```

---

# ExpenseFlow Milestone 1

At the end of Module 11 students should have:

✓ Django Installed

✓ Virtual Environment

✓ ExpenseFlow Project

✓ Expenses App

✓ Running Server

✓ First Route

✓ First View

✓ First Response

---

# Practical Exercise 1

Create a page:

```text
/about/
```

Output:

```text
About ExpenseFlow
```

---

# Practical Exercise 2

Create:

```text
/contact/
```

Output:

```text
Contact ExpenseFlow Team
```

---

# Practical Exercise 3

Create:

```text
/help/
```

Output:

```text
ExpenseFlow Help Center
```

---

# Project Assignment

## ExpenseFlow Setup

Build:

```text
ExpenseFlow v1.0
```

Requirements:

✓ Create Django Project

✓ Create expenses App

✓ Configure URLs

✓ Create Home Page

✓ Create About Page

✓ Create Contact Page

✓ Run Server Successfully

---

# Portfolio Section

## Project Name

ExpenseFlow v1.0 Setup

---

## What I Built

A Django web application foundation including project setup, application configuration, routing, views, and a running development server.

---

## Skills Demonstrated

* Django Installation
* Virtual Environments
* Project Structure
* Apps
* Views
* URLs
* HTTP Responses
* MVT Architecture

---

## Resume Description

Built the foundational architecture for ExpenseFlow, a Django-based expense tracking application, including project setup, application configuration, URL routing, and dynamic HTTP responses.

---

