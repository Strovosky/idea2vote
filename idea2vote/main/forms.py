# Here we'll create all of our forms for main app.

from django.forms import Form, CharField, IntegerField


class ProposeForm(Form):
    proposal_text = CharField(label="New Proposal", max_length=300)
    delete_proposal = IntegerField(label="Proposal To Delete")
