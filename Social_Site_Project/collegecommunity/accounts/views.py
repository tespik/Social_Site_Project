from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.shortcuts import render

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
