from django.shortcuts import render
from .models import Expense
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return HttpResponse(
        "Welcome To ExpenseFlow"
    )


def expense_list(request):

    expenses = Expense.objects.all()

    return render(
        request,
        "expenses/expense_list.html",
        {
            "expenses": expenses
        }
    )


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