# Here we'll create all of our forms for main app.

from django.forms import Form, CharField


class ProposeForm(Form):
    proposal_text = CharField(label="Proposal", max_length=300)
