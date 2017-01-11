from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label='Password', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','email','password']
        username = forms.CharField(label='Username', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
        first_name = forms.CharField(label='Player Name', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}))
        email = forms.CharField(label='email', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))
        password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
