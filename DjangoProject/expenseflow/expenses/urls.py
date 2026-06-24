from django.urls import path
from expenses.views import home

urlpatterns = [
    path("", home),
]