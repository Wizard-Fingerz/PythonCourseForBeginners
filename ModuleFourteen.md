# Module 14 — Authentication & User Management

## Phase 2: Software Engineering Specialization

### Project

# ExpenseFlow — User Registration, Login & Protected Expenses

---

# Module Overview

In Module 13, students built:

✓ Add Expense

✓ View Expenses

✓ Edit Expenses

✓ Delete Expenses

✓ CRUD Operations

However, there is a serious problem.

Currently:

```text id="auth001"
Everyone Sees Everyone's Expenses
```

Imagine:

* Adewale logs in
* Mary logs in

Both users can see the same expenses.

This is unacceptable.

Every user should only see their own expenses.

To solve this problem, we need:

```text id="auth002"
Authentication
```

---

# Learning Objectives

By the end of this module, students should be able to:

✓ Understand Authentication

✓ Understand Authorization

✓ Register Users

✓ Login Users

✓ Logout Users

✓ Protect Routes

✓ Restrict Access

✓ Associate Expenses With Users

✓ Display User-Specific Data

✓ Use Django Authentication System

---

# What Is Authentication?

Authentication answers:

```text id="auth003"
Who Are You?
```

Example:

```text id="auth004"
Username:
adewale

Password:
********
```

If correct:

```text id="auth005"
Access Granted
```

---

# What Is Authorization?

Authorization answers:

```text id="auth006"
What Can You Access?
```

Example:

```text id="auth007"
Adewale
↓
Can View Adewale Expenses

Cannot View Mary's Expenses
```

---

# ExpenseFlow Security Goal

Before Authentication:

```text id="auth008"
User A
     ↓
All Expenses

User B
     ↓
All Expenses
```

---

After Authentication:

```text id="auth009"
User A
     ↓
Only User A Expenses

User B
     ↓
Only User B Expenses
```

---

# Django Authentication System

Django already provides:

✓ User Model

✓ Login System

✓ Logout System

✓ Password Hashing

✓ Session Management

---

# User Journey

```text id="auth010"
Register
   ↓
Login
   ↓
Dashboard
   ↓
Manage Expenses
   ↓
Logout
```

---

# Step 1 — Create Registration Form

Create:

```python id="auth011"
forms.py
```

Add:

```python id="auth012"
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(
    UserCreationForm
):

    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "password1",
            "password2"
        ]
```

---

# Understanding UserCreationForm

Django automatically provides:

```text id="auth013"
Username

Password

Confirm Password

Validation
```

---

# Step 2 — Create Register View

```python id="auth014"
from .forms import RegisterForm
from django.shortcuts import render, redirect


def register(request):

    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "login"
            )

    else:

        form = RegisterForm()

    return render(
        request,
        "expenses/register.html",
        {
            "form": form
        }
    )
```

---

# Registration Template

Create:

```html id="auth015"
<h1>Create Account</h1>

<form method="POST">

    {% csrf_token %}

    {{ form.as_p }}

    <button type="submit">
        Register
    </button>

</form>
```

---

# Step 3 — Configure URL

```python id="auth016"
path(
    "register/",
    register,
    name="register"
)
```

---

# Test Registration

Visit:

```text id="auth017"
/register/
```

Create:

```text id="auth018"
Username:
adewale

Password:
password123
```

---

# Step 4 — Login View

Import:

```python id="auth019"
from django.contrib.auth import authenticate
from django.contrib.auth import login
```

---

Create:

```python id="auth020"
def login_view(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                "dashboard"
            )

    return render(
        request,
        "expenses/login.html"
    )
```

---

# Login Template

```html id="auth021"
<h1>Login</h1>

<form method="POST">

    {% csrf_token %}

    <input
        type="text"
        name="username"
        placeholder="Username"
    >

    <input
        type="password"
        name="password"
        placeholder="Password"
    >

    <button type="submit">
        Login
    </button>

</form>
```

---

# Step 5 — Logout

Import:

```python id="auth022"
from django.contrib.auth import logout
```

---

Create:

```python id="auth023"
def logout_view(request):

    logout(request)

    return redirect(
        "login"
    )
```

---

# URL

```python id="auth024"
path(
    "logout/",
    logout_view,
    name="logout"
)
```

---

# Protecting Pages

Currently:

```text id="auth025"
Anyone
Can Access Dashboard
```

We need:

```text id="auth026"
Logged-In Users Only
```

---

# Step 6 — Login Required

Import:

```python id="auth027"
from django.contrib.auth.decorators import login_required
```

---

Protect View:

```python id="auth028"
@login_required
def expense_list(request):
    ...
```

---

Now:

```text id="auth029"
Not Logged In
↓
Redirect To Login
```

---

# Associating Expenses With Users

Current Problem:

```text id="auth030"
Expense Has No Owner
```

Need:

```text id="auth031"
Expense Belongs To User
```

---

# Update Add Expense View

Replace:

```python id="auth032"
form.save()
```

With:

```python id="auth033"
expense = form.save(
    commit=False
)

expense.user = request.user

expense.save()
```

---

# What Is commit=False?

Allows us to modify the object before saving.

---

# User-Specific Expenses

Current:

```python id="auth034"
Expense.objects.all()
```

Shows everybody's expenses.

---

Replace with:

```python id="auth035"
Expense.objects.filter(
    user=request.user
)
```

Now users only see their own records.

---

# Security Example

Before:

```text id="auth036"
Adewale
 ↓
Sees Mary's Expenses

Mary
 ↓
Sees Adewale's Expenses
```

---

After:

```text id="auth037"
Adewale
 ↓
Only Adewale Expenses

Mary
 ↓
Only Mary Expenses
```

---

# Showing Logged-In User

Inside Template:

```html id="auth038"
<h2>
Welcome,
{{ request.user.username }}
</h2>
```

Output:

```text id="auth039"
Welcome, Adewale
```

---

# Navigation Bar

Example:

```html id="auth040"
<a href="/">Home</a>

<a href="/expenses/">
Expenses
</a>

<a href="/logout/">
Logout
</a>
```

---

# Creating Dashboard Page

View:

```python id="auth041"
@login_required
def dashboard(request):

    expenses = Expense.objects.filter(
        user=request.user
    )

    return render(
        request,
        "expenses/dashboard.html",
        {
            "expenses": expenses
        }
    )
```

---

# Dashboard Template

```html id="auth042"
<h1>ExpenseFlow Dashboard</h1>

<h3>
Welcome,
{{ request.user.username }}
</h3>

<p>
Total Expenses:
{{ expenses.count }}
</p>
```

---

# ExpenseFlow Milestone 4

Students now have:

✓ Registration

✓ Login

✓ Logout

✓ Protected Routes

✓ User Sessions

✓ User-Specific Expenses

✓ Dashboard

✓ Authentication System

---

# Practical Exercise 1

Create:

```text id="auth043"
Two User Accounts
```

Example:

```text id="auth044"
Adewale

Mary
```

---

# Practical Exercise 2

Login as:

```text id="auth045"
Adewale
```

Add expenses.

---

# Practical Exercise 3

Login as:

```text id="auth046"
Mary
```

Verify:

```text id="auth047"
Mary Cannot See Adewale Expenses
```

---

# Assignment

## Build Secure ExpenseFlow

Requirements:

✓ Register

✓ Login

✓ Logout

✓ Protected Expense Pages

✓ User-Specific Expenses

✓ Welcome Dashboard

---

# Professional Upgrade Challenge

Add:

```text id="auth048"
Email Validation
```

during registration.

---

# Super Challenge

Add:

```text id="auth049"
Change Password
```

feature.

---

# Expert Challenge

Add:

```text id="auth050"
Profile Page
```

Display:

* Username
* Email
* Date Joined

---

# Portfolio Section

## Project Name

ExpenseFlow Authentication System

---

## What I Built

Implemented a secure user authentication system for ExpenseFlow, including registration, login, logout, session management, route protection, and user-specific expense ownership.

---

## Skills Demonstrated

* Django Authentication
* User Management
* Sessions
* Login Protection
* Authorization
* Forms
* User Ownership
* Security Fundamentals

---

## Resume Description

Developed a secure authentication and authorization system for a Django expense management application, implementing user registration, login, logout, protected routes, and user-specific data access controls.

---

