from django import forms

class CreateUserForm(forms.Form):
  name = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'name'}))
  username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'username_input'}))
  password = forms.CharField(widget=forms.TextInput(attrs={'class': 'password'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'username_input'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'password_input'}))