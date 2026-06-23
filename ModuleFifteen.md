# Module 15 — Dashboard Analytics & Financial Reports

## Phase 2: Software Engineering Specialization

### Project

# ExpenseFlow — Business Intelligence Dashboard

---

# Module Overview

In Module 14, students built:

✓ Registration

✓ Login

✓ Logout

✓ User Authentication

✓ Protected Routes

✓ User-Specific Expenses

✓ Dashboard Foundation

ExpenseFlow is now functional.

Users can:

* Register
* Login
* Add expenses
* Manage expenses

But there is a problem.

The application only stores expenses.

It does not provide insights.

Most users want answers such as:

```text id="m15_001"
How much did I spend this month?

Which category costs me the most?

How many expenses do I have?

What is my highest expense?

What is my lowest expense?
```

This module introduces reporting and analytics.

Students will transform ExpenseFlow into a financial intelligence application.

---

# Learning Objectives

By the end of this module, students should be able to:

✓ Aggregate data

✓ Generate reports

✓ Use Django ORM aggregations

✓ Build dashboard statistics

✓ Create summary cards

✓ Calculate totals

✓ Filter data

✓ Build business intelligence features

✓ Display analytics on templates

---

# What Is Business Intelligence?

Business Intelligence means:

```text id="m15_002"
Turning Data Into Decisions
```

---

# Example

Raw Data:

```text id="m15_003"
Food      ₦5,000

Fuel      ₦10,000

Internet  ₦15,000
```

Not very useful.

---

Business Intelligence:

```text id="m15_004"
Total Spending:
₦30,000

Highest Category:
Internet

Average Expense:
₦10,000
```

Now users can make decisions.

---

# Dashboard Goals

ExpenseFlow Dashboard should show:

---

## Card 1

### Total Expenses

Example:

```text id="m15_005"
₦250,000
```

---

## Card 2

### Total Transactions

Example:

```text id="m15_006"
85 Expenses
```

---

## Card 3

### Highest Expense

Example:

```text id="m15_007"
Laptop Purchase

₦450,000
```

---

## Card 4

### Lowest Expense

Example:

```text id="m15_008"
Bottle Water

₦200
```

---

## Card 5

### Most Used Category

Example:

```text id="m15_009"
Food
```

---

# Understanding Aggregations

Aggregation means:

```text id="m15_010"
Summarizing Data
```

---

Examples:

```text id="m15_011"
Sum

Count

Average

Maximum

Minimum
```

---

# Django Aggregation Functions

Import:

```python id="m15_012"
from django.db.models import (
    Sum,
    Count,
    Avg,
    Max,
    Min
)
```

---

# Calculating Total Expenses

```python id="m15_013"
Expense.objects.filter(
    user=request.user
).aggregate(
    Sum("amount")
)
```

---

Result:

```text id="m15_014"
{
    "amount__sum": 250000
}
```

---

# Extracting Value

```python id="m15_015"
total_expenses = (
    Expense.objects.filter(
        user=request.user
    ).aggregate(
        Sum("amount")
    )["amount__sum"]
)
```

---

# Counting Expenses

```python id="m15_016"
expense_count = (
    Expense.objects.filter(
        user=request.user
    ).count()
)
```

---

# Highest Expense

```python id="m15_017"
highest_expense = (
    Expense.objects.filter(
        user=request.user
    ).order_by(
        "-amount"
    ).first()
)
```

---

# Lowest Expense

```python id="m15_018"
lowest_expense = (
    Expense.objects.filter(
        user=request.user
    ).order_by(
        "amount"
    ).first()
)
```

---

# Dashboard View

```python id="m15_019"
@login_required
def dashboard(request):

    expenses = Expense.objects.filter(
        user=request.user
    )

    total_expenses = (
        expenses.aggregate(
            Sum("amount")
        )["amount__sum"]
        or 0
    )

    total_transactions = (
        expenses.count()
    )

    highest_expense = (
        expenses.order_by(
            "-amount"
        ).first()
    )

    lowest_expense = (
        expenses.order_by(
            "amount"
        ).first()
    )

    context = {
        "total_expenses":
            total_expenses,

        "total_transactions":
            total_transactions,

        "highest_expense":
            highest_expense,

        "lowest_expense":
            lowest_expense
    }

    return render(
        request,
        "expenses/dashboard.html",
        context
    )
```

---

# Dashboard Template

```html id="m15_020"
<h1>ExpenseFlow Dashboard</h1>

<h2>
Welcome,
{{ request.user.username }}
</h2>

<hr>

<h3>
Total Spending:
₦{{ total_expenses }}
</h3>

<h3>
Transactions:
{{ total_transactions }}
</h3>
```

---

# Monthly Report

Users want:

```text id="m15_021"
How much did I spend this month?
```

---

# Current Month

Import:

```python id="m15_022"
from datetime import date
```

---

Get current month:

```python id="m15_023"
current_month = (
    date.today().month
)
```

---

Filter:

```python id="m15_024"
monthly_expenses = (
    Expense.objects.filter(
        user=request.user,
        date__month=current_month
    )
)
```

---

Calculate Total:

```python id="m15_025"
monthly_total = (
    monthly_expenses.aggregate(
        Sum("amount")
    )["amount__sum"]
    or 0
)
```

---

# Category Report

Question:

```text id="m15_026"
Which category costs me the most?
```

---

Import:

```python id="m15_027"
from django.db.models import Sum
```

---

Calculate:

```python id="m15_028"
category_report = (
    Expense.objects.filter(
        user=request.user
    )
    .values(
        "category__name"
    )
    .annotate(
        total=Sum("amount")
    )
    .order_by(
        "-total"
    )
)
```

---

# Result Example

```text id="m15_029"
Food
₦55,000

Transport
₦25,000

Internet
₦15,000
```

---

# Reports View

```python id="m15_030"
@login_required
def reports(request):

    category_report = (
        Expense.objects.filter(
            user=request.user
        )
        .values(
            "category__name"
        )
        .annotate(
            total=Sum("amount")
        )
        .order_by(
            "-total"
        )
    )

    return render(
        request,
        "expenses/reports.html",
        {
            "category_report":
                category_report
        }
    )
```

---

# Reports Template

```html id="m15_031"
<h1>Expense Reports</h1>

<table border="1">

<tr>
    <th>Category</th>
    <th>Total</th>
</tr>

{% for item in category_report %}

<tr>

<td>
{{ item.category__name }}
</td>

<td>
₦{{ item.total }}
</td>

</tr>

{% endfor %}

</table>
```

---

# Recent Expenses Section

Dashboard should display:

```python id="m15_032"
recent_expenses = (
    Expense.objects.filter(
        user=request.user
    ).order_by(
        "-created_at"
    )[:5]
)
```

---

# Dashboard Cards Layout

```text id="m15_033"
----------------------------------

Total Expenses

₦250,000

----------------------------------

Transactions

85

----------------------------------

Highest Expense

Laptop

₦450,000

----------------------------------

Lowest Expense

Water

₦200

----------------------------------
```

---

# ExpenseFlow Milestone 5

Students now have:

✓ Financial Dashboard

✓ Monthly Report

✓ Category Report

✓ Expense Statistics

✓ Business Intelligence

✓ Analytics System

---

# Practical Exercise 1

Create:

```text id="m15_034"
20 Expense Records
```

---

# Practical Exercise 2

Generate:

```text id="m15_035"
Monthly Spending Report
```

---

# Practical Exercise 3

Generate:

```text id="m15_036"
Category Spending Report
```

---

# Assignment

## Build Expense Analytics

Requirements:

✓ Total Expenses

✓ Expense Count

✓ Highest Expense

✓ Lowest Expense

✓ Monthly Total

✓ Category Report

✓ Recent Expenses

---

# Professional Upgrade Challenge

Add:

```text id="m15_037"
Average Expense
```

using:

```python id="m15_038"
Avg("amount")
```

---

# Super Challenge

Add:

```text id="m15_039"
Top 5 Most Expensive Purchases
```

Feature.

---

# Expert Challenge

Create:

```text id="m15_040"
Expense Trend Report
```

Display:

```text id="m15_041"
January

February

March

April
```

with totals.

---

# Future Upgrade

In production systems, dashboards use:

* Charts
* Graphs
* Data Visualization

Examples:

* Bar Charts
* Pie Charts
* Line Charts

Students will explore this in advanced tracks.

---

# Portfolio Section

## Project Name

ExpenseFlow Analytics Dashboard

---

## What I Built

Built a business intelligence dashboard for ExpenseFlow that generates expense summaries, monthly reports, category reports, and financial statistics using Django ORM aggregations.

---

## Skills Demonstrated

* Django Aggregations
* QuerySets
* Reporting
* Business Intelligence
* Analytics
* Data Summarization
* Dashboard Development
* Django Templates

---

## Resume Description

Developed a financial analytics dashboard in Django that generates real-time expense summaries, category reports, monthly spending analysis, and business intelligence insights using database aggregations.

---

