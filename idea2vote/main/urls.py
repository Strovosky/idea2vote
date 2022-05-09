from django.urls import path
from . import views


urlpatterns = [
    path(route="", view=views.index, name="index"),
    path(route="propose/", view=views.propose, name="propose"),
    path(route="successful_proposal/", view=views.successful_proposal, name="successful_proposal"),
    path(route="vote/", view=views.vote, name="vote"),
    path(route="vote-success/", view=views.successful_vote, name="successful_vote")
]

