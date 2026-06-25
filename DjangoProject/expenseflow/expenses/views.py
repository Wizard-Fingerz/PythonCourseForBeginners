from django.shortcuts import render, redirect
from .models import Expense
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .forms import ExpenseForm, ExpenseForm, RegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.models import (
    Sum,
    Count,
    Avg,
    Max,
    Min
)
# Create your views here.

def home(request):
    return HttpResponse(
        "Welcome To ExpenseFlow"
    )


@login_required
def expense_list(request):

    expenses = Expense.objects.filter(
                    user=request.user
                )

    return render(
        request,
        "expenses/expense_list.html",
        {
            "expenses": expenses
        }
    )




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

            expense = form.save(
                commit=False
            )

            expense.user = request.user

            expense.save()

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


def logout_view(request):

    logout(request)

    return redirect(
        "login"
    )

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