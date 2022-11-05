from django.contrib import admin
from django.urls import path
from loan.views import get_loans, add_new_loan

urlpatterns = [
    path("", get_loans),
    path("new", add_new_loan),
]