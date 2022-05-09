from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ProposeForm

# Create your views here.

# This will be the home page of our project.
def index(response):
    return render(response, "main/index.html", {})

def propose(response):
    if response.method ==  "POST":
        form = ProposeForm(response.POST)
        if form.is_valid():
            candidate_id = form.cleaned_data["candidate_id"]
            candidate = User.objects.get(id=candidate_id)
            candidate.proposals.text = form.cleaned_data["proposal_text"]
        if response.POST.


