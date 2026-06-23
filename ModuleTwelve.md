# Module 12 — Database Design, Models & Admin Panel

## Phase 2: Software Engineering Specialization

### Project

# ExpenseFlow — Expense Categories & Database Models

---

# Module Overview

In Module 11, students built:

✓ ExpenseFlow Project

✓ Django Application

✓ URLs

✓ Views

✓ HTTP Responses

✓ Django Project Structure

However, ExpenseFlow currently has a major limitation:

```text id="g18s9f"
No Data Is Stored
```

Users cannot:

* Save expenses
* Create categories
* Track spending
* Store records

Module 12 solves this problem by introducing databases and Django models.

---

# Learning Objectives

By the end of this module, students should be able to:

✓ Explain what a database is

✓ Explain tables, rows, and columns

✓ Understand Django Models

✓ Create Django Models

✓ Create Relationships

✓ Generate Migrations

✓ Apply Migrations

✓ Use Django ORM

✓ Register Models in Admin Panel

✓ Create Records through Admin Panel

---

# What Is A Database?

A database is a system used to store information permanently.

Examples:

```text id="kxtj3v"
Bank Accounts

Student Records

Hospital Records

Employee Records

Expenses
```

---

# Without Database

```text id="w9v7m7"
Open App
↓
Add Expense
↓
Close App
↓
Expense Lost
```

---

# With Database

```text id="fqjv1j"
Open App
↓
Add Expense
↓
Close App
↓
Open App Again
↓
Expense Still Exists
```

---

# Understanding Tables

Imagine a spreadsheet.

---

## Expense Table

| ID | Title    | Amount |
| -- | -------- | ------ |
| 1  | Food     | 5000   |
| 2  | Fuel     | 15000  |
| 3  | Internet | 20000  |

---

Each row represents:

```text id="wxy4pj"
One Expense
```

---

Each column represents:

```text id="iqy1c4"
One Attribute
```

---

# Django Models

Models define how data is stored.

Think of a model as a blueprint.

Example:

```python id="klc8ps"
Expense
```

Django automatically creates the database table.

---

# ExpenseFlow Database Design

We need:

```text id="7m8v7r"
Category
Expense
```

---

# Relationship Design

```text id="l6rj2r"
User
 │
 ├── Category
 │
 └── Expense
```

---

One User:

```text id="jvhn29"
Can Have Many Expenses
```

---

One Category:

```text id="b5mp9m"
Can Have Many Expenses
```

---

# Creating Category Model

Open:

```python id="gnskwb"
models.py
```

Create:

```python id="g2e8c8"
from django.db import models


class Category(models.Model):

    name = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
```

---

# Understanding Category Fields

### name

```python id="18a4ha"
models.CharField()
```

Stores text.

Example:

```text id="rllvha"
Food
Transport
Health
```

---

### created_at

```python id="7l2go2"
auto_now_add=True
```

Automatically saves creation date.

---

# Creating Expense Model

Add:

```python id="h6c0ec"
from django.contrib.auth.models import User


class Expense(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        blank=True
    )

    date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
```

---

# Understanding Relationships

## ForeignKey

```python id="v92v5e"
user = models.ForeignKey(...)
```

Means:

```text id="7ewhz7"
One User
Can Own Many Expenses
```

---

## Category Relationship

```python id="t0hcmj"
category = models.ForeignKey(...)
```

Means:

```text id="6c9g5v"
One Category
Can Have Many Expenses
```

---

# Visual Example

```text id="7rjybm"
User: Adewale

Expenses:

Food
Transport
Internet
Fuel
```

All belong to the same user.

---

# Creating Migrations

Tell Django:

```text id="ejnhtn"
Build Database Tables
```

Run:

```bash id="jlwm1t"
python manage.py makemigrations
```

Expected:

```text id="3wjlwm"
Migrations for expenses
```

---

# Applying Migrations

Run:

```bash id="5t6e8m"
python manage.py migrate
```

Django creates database tables.

---

# Understanding Migration

Think of migration as:

```text id="fl1kn6"
Blueprint
↓
Actual Building
```

Models are blueprints.

Migrations build the database.

---

# Creating Superuser

Admin panel requires a superuser.

Run:

```bash id="8x1g3r"
python manage.py createsuperuser
```

Example:

```text id="d4g6h5"
Username: admin

Email:
admin@example.com

Password:
********
```

---

# Register Models in Admin Panel

Open:

```python id="y5f79n"
admin.py
```

Add:

```python id="abz7xk"
from django.contrib import admin
from .models import Category, Expense

admin.site.register(Category)
admin.site.register(Expense)
```

---

# Run Server

```bash id="8bh11z"
python manage.py runserver
```

---

# Open Admin

Visit:

```text id="yzm89f"
http://127.0.0.1:8000/admin
```

Login with superuser.

---

# First ExpenseFlow Database

Students can now:

✓ Add Categories

✓ Add Expenses

✓ View Expenses

✓ Store Data Permanently

---

# Creating Sample Categories

Create:

```text id="m7tzq5"
Food

Transport

Health

Education

Utilities

Entertainment
```

---

# Creating Sample Expenses

Example:

```text id="g9p0y5"
Title:
Lunch

Amount:
3500

Category:
Food

Date:
2026-07-01
```

---

# Introduction to Django ORM

ORM means:

```text id="95a7cg"
Object Relational Mapper
```

Allows Python to communicate with database.

---

# Creating Records

Open:

```bash id="6gg2m0"
python manage.py shell
```

---

Example:

```python id="9ul20x"
from expenses.models import Category

Category.objects.create(
    name="Food"
)
```

---

# Retrieving Records

```python id="byknw7"
Category.objects.all()
```

---

# Filtering Records

```python id="kkg6xa"
Category.objects.filter(
    name="Food"
)
```

---

# Project Assignment

## ExpenseFlow Database Setup

Build:

```text id="ehbmk9"
ExpenseFlow Database Layer
```

Requirements:

✓ Create Category Model

✓ Create Expense Model

✓ Create Relationships

✓ Generate Migrations

✓ Apply Migrations

✓ Register Models

✓ Create Admin User

✓ Create Sample Data

---

# Practical Exercise 1

Create a category called:

```text id="g0c8k8"
Shopping
```

using Django Admin.

---

# Practical Exercise 2

Create:

```text id="6wttb7"
5 Expenses
```

using Admin Panel.

---

# Practical Exercise 3

Use Django Shell to:

```python id="t31wfk"
Retrieve All Expenses
```

---

# ExpenseFlow Milestone 2

At the end of Module 12 students should have:

✓ Working Database

✓ Expense Model

✓ Category Model

✓ Admin Panel

✓ Stored Expenses

✓ Stored Categories

✓ Django ORM Knowledge

---

# Portfolio Section

## Project Name

ExpenseFlow Database Design

---

## What I Built

Designed and implemented the database layer of ExpenseFlow using Django Models, database migrations, relationships, and the Django Admin Panel.

---

## Skills Demonstrated

* Django Models
* Database Design
* Migrations
* Relationships
* Foreign Keys
* Admin Panel
* Django ORM

---

## Resume Description

Designed and implemented relational database models for ExpenseFlow using Django ORM, including category and expense management with user relationships and administrative functionality.

---
