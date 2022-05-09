from django.shortcuts import render, redirect
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
            p_text = form.cleaned_data["proposal_text"]
            response.user.proposals.create(text=p_text, votes=0)
            return redirect(to="/successful_proposal/")
    else:
        form = ProposeForm()
        return render(response, "main/propose.html", {"form":form})

def successful_proposal(response):
    return render(response, "main/successful_proposal.html", {})

def vote(response):
    all_candidates = User.objects.all()
    if response.method == "POST":
        for candidate in all_candidates:
            for proposal in candidate.proposals.all():
                if response.POST.get("cb" + str(proposal.id)) == "checked":
                    proposal.votes += 1
                    proposal.save()
    return render(response, "main/vote.html", {"all_candidates":all_candidates})

def successful_vote(response):
    return render(response, "main/successful_vote.html", {})


