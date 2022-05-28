from importlib.resources import path
from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

# This view is incomplete and is temporary
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect(to="/")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})
