from django import forms
from .models import Expense

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ExpenseForm(forms.ModelForm):

    class Meta:

        model = Expense

        fields = [
            "user",
            "title",
            "category",
            "amount",
            "description",
            "date"
        ]


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