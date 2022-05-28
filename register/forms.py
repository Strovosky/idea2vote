from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, EmailField
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = CharField(max_length=70)
    last_name = CharField(max_length=70)
    email = EmailField
    
    class Meta:
        model = User
        # FYI, These are all the built-in attributes of the User instances.
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]
