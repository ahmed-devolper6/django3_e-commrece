from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Sginup(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

class ActiveFrom(forms.Form):
    code = forms.CharField(max_length=8)