from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from . import models

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required','class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id':'required', 'class': 'form-control', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'id':'required','class': 'form-control', 'placeholder': 'Last Name'}), required=True)
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'id':'required','class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, label="Password", widget=forms.PasswordInput(attrs={'id':'required','class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, label="Password Confirmation", widget=forms.PasswordInput(attrs={'id':'required','class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class change_data(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields= ['username', 'first_name', 'last_name', 'email']

class CarForm(forms.ModelForm):
    class Meta:
        model = models.CarModel
        fields = '__all__'

class CarBrandForm(forms.ModelForm):
    class Meta:
        model = models.BrandModel
        fields = '__all__'

class commentForm(forms.ModelForm):
    class Meta:
        model = models.Comments
        fields = ['name','email','body']