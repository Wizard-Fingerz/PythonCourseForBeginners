# Module 13 — Expense CRUD (Create, Read, Update, Delete)

## Phase 2: Software Engineering Specialization

### Project

# ExpenseFlow — Expense Management System

---

# Module Overview

In Module 12, students built:

✓ Category Model

✓ Expense Model

✓ Database Relationships

✓ Admin Panel

✓ Database Migrations

However, there is still a major problem.

Currently, users must use:

```text
/admin
```

to manage expenses.

Real users should never need access to Django Admin.

In this module, students will build the actual ExpenseFlow application interface.

Users will now be able to:

✓ Add Expenses

✓ View Expenses

✓ Edit Expenses

✓ Delete Expenses

through web pages.

---

# Learning Objectives

By the end of this module, students should be able to:

✓ Understand CRUD Operations

✓ Create Templates

✓ Create Django Forms

✓ Create Function-Based Views

✓ Pass Data to Templates

✓ Display Database Records

✓ Update Records

✓ Delete Records

✓ Use URL Parameters

✓ Build Dynamic Web Pages

---

# What Is CRUD?

CRUD stands for:

```text
Create
Read
Update
Delete
```

Every business application performs CRUD operations.

Examples:

### Facebook

Create Post

Read Posts

Update Post

Delete Post

---

### Banking App

Create Transaction

Read Statement

Update Profile

Delete Beneficiary

---

### ExpenseFlow

Create Expense

Read Expense

Update Expense

Delete Expense

---

# ExpenseFlow Features

Students will build:

```text
/expenses/

/expenses/add/

/expenses/edit/<id>

/expenses/delete/<id>
```

---

# Visual Flow

```text
Dashboard
    │
    ▼
Expense List
    │
 ┌──┼──┐
 │  │  │
 ▼  ▼  ▼

Add Edit Delete
```

---

# Step 1 — Create Templates Folder

Inside:

```text
expenses/
```

Create:

```text
templates/

    expenses/

        expense_list.html

        expense_form.html

        expense_delete.html
```

---

# Step 2 — Understanding Templates

Templates are HTML pages displayed to users.

Example:

```html
<h1>ExpenseFlow</h1>
```

When users visit a page, Django returns a template.

---

# Step 3 — Creating Expense List View

Open:

```python
views.py
```

Add:

```python
from django.shortcuts import render
from .models import Expense


def expense_list(request):

    expenses = Expense.objects.all()

    return render(
        request,
        "expenses/expense_list.html",
        {
            "expenses": expenses
        }
    )
```

---

# Understanding This Code

Retrieve:

```python
Expense.objects.all()
```

This fetches all expenses.

---

Pass to template:

```python
{
    "expenses": expenses
}
```

Now HTML can display expenses.

---

# Step 4 — Create Expense List Template

Create:

```html
<h1>All Expenses</h1>

<table border="1">

<tr>
    <th>Title</th>
    <th>Category</th>
    <th>Amount</th>
    <th>Date</th>
</tr>

{% for expense in expenses %}

<tr>
    <td>{{ expense.title }}</td>
    <td>{{ expense.category }}</td>
    <td>{{ expense.amount }}</td>
    <td>{{ expense.date }}</td>
</tr>

{% endfor %}

</table>
```

---

# Template Tags

```html
{% for expense in expenses %}
```

Means:

```text
Loop Through Expenses
```

---

# Variable Display

```html
{{ expense.title }}
```

Displays:

```text
Lunch
Fuel
Internet
```

---

# Step 5 — Configure URL

Open:

```python
urls.py
```

Add:

```python
path(
    "expenses/",
    expense_list,
    name="expense_list"
)
```

---

# Test Page

Visit:

```text
http://127.0.0.1:8000/expenses/
```

You should see all expenses.

---

# Step 6 — Creating Forms

Open:

```python
forms.py
```

Create:

```python
from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = [
            "title",
            "category",
            "amount",
            "description",
            "date"
        ]
```

---

# Why Forms?

Without forms:

```text
Manually Collect Data
```

With forms:

```text
Django Generates Form Automatically
```

---

# Step 7 — Add Expense View

```python
from .forms import ExpenseForm
from django.shortcuts import redirect


def add_expense(request):

    if request.method == "POST":

        form = ExpenseForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "expense_list"
            )

    else:

        form = ExpenseForm()

    return render(
        request,
        "expenses/expense_form.html",
        {
            "form": form
        }
    )
```

---

# Understanding Request Methods

## GET

```text
Show Form
```

---

## POST

```text
Submit Form
```

---

# Expense Form Template

```html
<h1>Add Expense</h1>

<form method="POST">

    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">
        Save Expense
    </button>

</form>
```

---

# What Is CSRF?

Security protection.

Always include:

```html
{% csrf_token %}
```

inside forms.

---

# Step 8 — Add URL

```python
path(
    "expenses/add/",
    add_expense,
    name="add_expense"
)
```

---

# Test

Visit:

```text
/expenses/add/
```

Add an expense.

Verify it appears in:

```text
/expenses/
```

---

# Step 9 — Edit Expense

```python
from django.shortcuts import get_object_or_404


def edit_expense(
    request,
    expense_id
):

    expense = get_object_or_404(
        Expense,
        id=expense_id
    )

    if request.method == "POST":

        form = ExpenseForm(
            request.POST,
            instance=expense
        )

        if form.is_valid():

            form.save()

            return redirect(
                "expense_list"
            )

    else:

        form = ExpenseForm(
            instance=expense
        )

    return render(
        request,
        "expenses/expense_form.html",
        {
            "form": form
        }
    )
```

---

# URL

```python
path(
    "expenses/edit/<int:expense_id>/",
    edit_expense,
    name="edit_expense"
)
```

---

# Understanding URL Parameters

```text
expenses/edit/5/
```

Expense ID:

```text
5
```

---

# Step 10 — Delete Expense

```python
def delete_expense(
    request,
    expense_id
):

    expense = get_object_or_404(
        Expense,
        id=expense_id
    )

    if request.method == "POST":

        expense.delete()

        return redirect(
            "expense_list"
        )

    return render(
        request,
        "expenses/expense_delete.html",
        {
            "expense": expense
        }
    )
```

---

# Delete Template

```html
<h2>
Delete Expense?
</h2>

<p>
{{ expense.title }}
</p>

<form method="POST">

    {% csrf_token %}

    <button type="submit">
        Confirm Delete
    </button>

</form>
```

---

# Delete URL

```python
path(
    "expenses/delete/<int:expense_id>/",
    delete_expense,
    name="delete_expense"
)
```

---

# Updating Expense List

Add Actions column.

```html
<th>Actions</th>
```

---

Inside loop:

```html
<td>

<a href="{% url 'edit_expense' expense.id %}">
Edit
</a>

|

<a href="{% url 'delete_expense' expense.id %}">
Delete
</a>

</td>
```

---

# ExpenseFlow Milestone 3

Students now have:

✓ Add Expense

✓ View Expense

✓ Edit Expense

✓ Delete Expense

✓ Dynamic Templates

✓ Forms

✓ URL Parameters

✓ CRUD Operations

---

# Practical Exercise 1

Create:

```text
10 Expenses
```

using your new form.

---

# Practical Exercise 2

Edit:

```text
5 Expenses
```

and verify updates.

---

# Practical Exercise 3

Delete:

```text
3 Expenses
```

and verify removal.

---

# Assignment

## Build Expense Manager

Requirements:

✓ Expense List Page

✓ Add Expense Page

✓ Edit Expense Page

✓ Delete Expense Page

✓ Navigation Links

---

# Professional Upgrade Challenge

Add:

```text
Expense Description
```

to list page.

---

# Super Challenge

Add:

```text
Search Expenses
```

Feature.

Example:

```text
Search:
Food
```

Only matching expenses should appear.

---

# Expert Challenge

Add:

```text
Filter By Category
```

Feature.

Example:

```text
Food

Transport

Education
```

Selecting a category filters expenses.

---

# Portfolio Section

## Project Name

ExpenseFlow Expense Manager

---

## What I Built

A Django-based expense management system implementing complete CRUD operations, allowing users to create, view, update, and delete expense records through dynamic web pages.

---

## Skills Demonstrated

* Django Views
* Django Templates
* ModelForms
* CRUD Operations
* URL Routing
* QuerySets
* Template Tags
* Dynamic Data Rendering

---

## Resume Description

Developed the Expense Management module of ExpenseFlow using Django, implementing full CRUD functionality with forms, templates, database integration, and dynamic routing.

---

