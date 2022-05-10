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
    print("Before POST method was run.")
    if response.method == "POST":
        print("After POST method was run.")
        if response.POST.get("btn_vote") == "pressed":
            for candidate in all_candidates:
                print("For candidate in all_candidates was run.")
                t_votes = 0
                if len(candidate.position.all()) == 0:
                    candidate.position.create(total_votes=0)
                    print("This part was run.")
                for proposal in candidate.proposals.all():
                    if response.POST.get("cb" + str(proposal.id)) == "checked":
                        proposal.votes += 1
                        proposal.save()
                        t_votes += proposal.votes
                for ind, c_position in enumerate(candidate.position.all(), start=1):
                    if ind == 1:
                        c_position.total_votes = t_votes
                        c_position.save()
                        print("This part was run.")
        return redirect(to="/vote-success/")
    return render(response, "main/vote.html", {"all_candidates":all_candidates})

def successful_vote(response):
    return render(response, "main/successful_vote.html", {})


