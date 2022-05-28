from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.

# This will be the home page of our project.
def index(response):
    return render(response, "main/index.html", {})

def propose(response):
    if response.method ==  "POST":
        if response.POST.get("btn_new_proposal") == "pressed":
            p_text = response.POST.get("create_proposal")
            response.user.proposals.create(text=p_text, votes=0)
            return redirect(to="/successful_proposal/")
        elif response.POST.get("btn_delete") == "pressed":
            proposal_to_delete = int(response.POST.get("delete_proposal"))
            for ind, proposal in enumerate(response.user.proposals.all(), start=1):
                if proposal_to_delete == ind:
                    proposal.delete()
    return render(response, "main/propose.html", {})

def successful_proposal(response):
    return render(response, "main/successful_proposal.html", {})

def vote(response):
    all_candidates = User.objects.all()
    if response.method == "POST":
        for candidate in all_candidates:
            t_votes = 0
            if len(candidate.position.all()) == 0:
                candidate.position.create(total_votes=0)
            for proposal in candidate.proposals.all():
                if response.POST.get("cb" + str(proposal.id)) == "checked":
                    proposal.votes += 1
                    proposal.save()
                    t_votes += proposal.votes
                else:
                    t_votes += proposal.votes
            for ind, c_position in enumerate(candidate.position.all(), start=1):
                if ind == 1:
                    c_position.total_votes = t_votes
                    c_position.save()
        return redirect(to="/vote-success/")
    return render(response, "main/vote.html", {"all_candidates":all_candidates})

def successful_vote(response):
    return render(response, "main/successful_vote.html", {})

def leaders(response):
    all_candidates = User.objects.all()
    all_candidates_dict = {}
    for ind, candidate in enumerate(all_candidates, start=1):
        for ind_position, position in enumerate(candidate.position.all(), start=1):
            if ind_position == 1:
                all_candidates_dict.update({f"{candidate.first_name} {candidate.last_name}": position.total_votes})

    leaders = []
    for iter in range(3):
        new_max_value = max(all_candidates_dict.keys(), key=(lambda new_k: all_candidates_dict[new_k]))
        cand_key = [cand_k for cand_k in all_candidates_dict if all_candidates_dict[cand_k] == all_candidates_dict[new_max_value]]
        winner = {cand_key[0]: all_candidates_dict[new_max_value]}
        leaders.append(winner)
        del(all_candidates_dict[cand_key[0]])
    
    return render(response, "main/leaders.html", {"leaders": leaders})

