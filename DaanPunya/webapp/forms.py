from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import extUser

class extUserCreationForm(UserCreationForm):
    class Meta:
        model = extUser
        fields = "__all__"