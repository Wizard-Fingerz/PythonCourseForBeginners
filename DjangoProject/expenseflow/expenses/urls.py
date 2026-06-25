from django.urls import path
from expenses.views import add_expense, delete_expense, edit_expense, expense_list, home

urlpatterns = [
    path("", home),
    path(
        "expenses/",
        expense_list,
        name="expense_list"
    ),
    path(
        "expenses/add/",
        add_expense,
        name="add_expense"
    ),
    path(
        "expenses/edit/<int:expense_id>/",
        edit_expense,
        name="edit_expense"
    ),
    path(
        "expenses/delete/<int:expense_id>/",
        delete_expense,
        name="delete_expense"
    ),
    
]