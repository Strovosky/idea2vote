from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE
from django.contrib.auth.models import User


# Create your models here.

class Proposals(Model):
    user = ForeignKey(to=User, on_delete=CASCADE, related_name="proposals", null=True)
    text = CharField(max_length=400)
    votes = IntegerField()

    def __str__(self) -> str:
        return self.text

# This table will tell how many votes each candidate has.
class Position(Model):
    user = ForeignKey(to=User, on_delete=CASCADE, related_name="position", null=True)
    total_votes = IntegerField()

