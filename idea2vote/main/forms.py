# Here we'll create all of our forms for main app.

from django.forms import Form, CharField, IntegerField


class ProposeForm(Form):
    candidate_id = IntegerField(label="Candidate ID")
    proposal_text = CharField(label="Proposal", max_length=300)
