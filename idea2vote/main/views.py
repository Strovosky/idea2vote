from django.shortcuts import render

# Create your views here.

# This will be the home page of our project.
def index(response):
    return render(response, "main/index.html", {})

