from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Issue, Reply

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='First Name')
    last_name = forms.CharField(max_length=100, required=True, label='Last Name')
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'tags']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']