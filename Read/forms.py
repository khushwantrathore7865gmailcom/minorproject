from django import forms
from django.contrib.auth.forms import UserCreationForm
from User.models import Users
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your first name', 'class': "input100"}))
    last_name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your first name', 'class': "input100"}))
    ApiKey = forms.CharField(max_length=352, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Enter your Api key of read', 'class': "input100"}))
    email = forms.EmailField(max_length=254,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter email address', 'class': "input100"}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password ', 'class': "input100"}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(
        attrs={'placeholder': 'confirm Password ', 'class': "input100"}))


    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'ApiKey',
            'email',
            'password1',
            'password2',
        ]
