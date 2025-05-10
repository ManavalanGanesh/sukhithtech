from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from .models import userlog



class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=60, help_text='Required, Add a valid email Address')


    class Meta:

        model = User

        fields = ["email", "username","password1", "password2"]

