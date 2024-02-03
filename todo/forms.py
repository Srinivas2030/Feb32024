from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput

#--------- REEgister a User -----#

       
        
class CreateUserForm(UserCreationForm):
    class Meta:
        
        model = User
        fields=['username','email','password1','password2']
    
class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    passowrd:forms.CharField(widget=PasswordInput())
            