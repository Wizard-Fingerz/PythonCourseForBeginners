# ExpenseFlow

## Product Requirements Document (PRD)

### Version 1.0

---

# Product Overview

ExpenseFlow is a personal expense tracking web application that helps users:

* Track expenses
* Categorize spending
* View spending history
* Monitor monthly expenses
* Generate reports
* Build healthy financial habits

The application is designed specifically for beginner Django students to learn real-world software engineering while building a complete deployable product.

---

# Problem Statement

Many people:

* Spend money without tracking it
* Cannot identify spending patterns
* Struggle to budget effectively
* Lack visibility into monthly expenses

ExpenseFlow solves this by providing a simple dashboard where users can record and analyze expenses.

---

# Target Audience

### Primary Users

* Students
* Young professionals
* Freelancers
* Small business owners

### Secondary Users

* Families
* Budget-conscious individuals

---

# Product Goals

Students should learn:

* Django
* Database Design
* CRUD Operations
* Authentication
* User Authorization
* Deployment
* Software Engineering Practices

While building a complete real-world application.

---

# Core Features

## User Management

### User Registration

Users should be able to:

* Create account
* Enter email
* Create password

---

### Login

Users should:

* Log into their account
* Access personal dashboard

---

### Logout

Users should:

* End session securely

---

# Expense Management

### Add Expense

Users should be able to:

Add:

```text
Expense Title
Category
Amount
Description
Date
```

Example:

```text
Lunch
Food
₦3,500
Chicken Republic
2026-07-01
```

---

### View Expenses

Users should see:

```text
Title
Category
Amount
Date
```

in a table.

---

### Edit Expense

Users can:

* Update amount
* Update category
* Update description

---

### Delete Expense

Users can remove expenses.

---

# Categories

Default categories:

```text
Food
Transportation
Utilities
Entertainment
Education
Health
Shopping
Housing
Others
```

Users can:

* Create custom categories
* Edit categories
* Delete categories

---

# Dashboard

The Dashboard should display:

---

### Total Expenses

Example:

```text
₦250,000
```

---

### This Month Expenses

Example:

```text
₦45,000
```

---

### Number of Expenses

Example:

```text
125 Expenses
```

---

### Most Used Category

Example:

```text
Food
```

---

### Recent Expenses

Display:

```text
Food        ₦5,000
Transport   ₦2,500
Internet    ₦15,000
```

---

# Reporting Module

Users should view:

---

### Monthly Report

Example:

```text
January: ₦25,000
February: ₦18,000
March: ₦40,000
```

---

### Category Report

Example:

```text
Food: ₦35,000
Transport: ₦10,000
Health: ₦15,000
```

---

### Highest Expense

Example:

```text
Laptop Purchase
₦450,000
```

---

### Lowest Expense

Example:

```text
Water
₦200
```

---

# Search Feature

Users should search:

```text
Food
Transport
Laptop
School Fees
```

Results should appear instantly.

---

# Filtering

Filter expenses by:

* Category
* Date
* Month
* Amount Range

---

# Profile Management

Users should manage:

### Profile

* Name
* Email

---

### Password

* Change password

---

# Database Design

---

## User Model

Django built-in User model

```text
Username
Email
Password
```

---

## Category Model

```python
name
created_at
```

---

## Expense Model

```python
title
amount
description
date
created_at
user
category
```

---

# Relationships

```text
User
 │
 ├── Category
 │
 └── Expense
```

---

One User:

* Has many expenses

One Category:

* Has many expenses

---

# Screen Designs

---

# Screen 1

## Landing Page

### URL

```text
/
```

---

Components:

```text
Logo

Hero Section

Track Your Expenses
With Ease

Register Button

Login Button
```

---

# Screen 2

## Registration Page

### URL

```text
/register/
```

Fields:

```text
Username
Email
Password
Confirm Password
```

Button:

```text
Create Account
```

---

# Screen 3

## Login Page

### URL

```text
/ login /
```

Fields:

```text
Username
Password
```

Button:

```text
Login
```

---

# Screen 4

## Dashboard

### URL

```text
/dashboard/
```

Cards:

```text
Total Expenses

Monthly Expenses

Total Categories

Recent Expenses
```

---

# Screen 5

## Expense List

### URL

```text
/expenses/
```

Table:

```text
Title
Category
Amount
Date
Actions
```

Actions:

```text
Edit
Delete
```

---

# Screen 6

## Add Expense

### URL

```text
/expenses/add/
```

Fields:

```text
Title
Category
Amount
Description
Date
```

Button:

```text
Save Expense
```

---

# Screen 7

## Edit Expense

### URL

```text
/expenses/edit/<id>/
```

---

# Screen 8

## Delete Expense

### URL

```text
/expenses/delete/<id>/
```

Confirmation:

```text
Are you sure?
```

---

# Screen 9

## Categories

### URL

```text
/categories/
```

Features:

* Add Category
* Edit Category
* Delete Category

---

# Screen 10

## Reports

### URL

```text
/reports/
```

Display:

* Monthly Spending
* Category Spending
* Highest Expense
* Lowest Expense

---

# Development Roadmap

## Module 11

### Django Foundations

Build:

```text
ExpenseFlow Project Setup
```

Deliverables:

* Install Django
* Create Project
* Run Server
* Understand MVT

---

## Module 12

### Database & Models

Build:

```text
Category Model
Expense Model
```

Deliverables:

* Models
* Migrations
* Admin Panel

---

## Module 13

### Expense CRUD

Build:

```text
Add Expense
View Expense
Edit Expense
Delete Expense
```

Deliverables:

* Forms
* Views
* Templates

---

## Module 14

### Authentication

Build:

```text
Register
Login
Logout
```

Deliverables:

* User Accounts
* Protected Routes

---

## Module 15

### Dashboard & Reports

Build:

```text
Dashboard
Reports
Analytics
```

Deliverables:

* Statistics
* Aggregations
* Reports

---

## Module 16

### Deployment

Build:

```text
Live ExpenseFlow Application
```

Deliverables:

* GitHub
* Deployment
* Portfolio
* Resume Project

---

# Final Portfolio Project

Students will graduate with:

### HR Management System

Built from Modules 1–10

### ExpenseFlow

Built from Modules 11–16

### GitHub Portfolio

Containing:

* 10 Python Projects
* 1 Django Application
* Professional Documentation

### Live Application

Accessible through a public URL

### Career Outcome

Ready for:

* Junior Python Developer
* Junior Django Developer
* Backend Developer Internship
* Freelance Web Development
