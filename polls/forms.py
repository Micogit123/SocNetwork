from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput
from .models import UserInformation, City


YEARS= [x for x in range(1940,2019)]


class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput
                            (attrs={'placeholder': ' myusername'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput
                            (attrs={'placeholder': ' myfirstname'}))
    last_name = forms.CharField(required=False,widget=forms.TextInput
                            (attrs={'placeholder': ' mylastname'}))
    email = forms.EmailField(required=True, widget=forms.TextInput
                            (attrs={'placeholder': ' myemail@gmail.com'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput
                            (attrs={'placeholder': ' eg. mypass123'}))
    password2 = forms.CharField(required=True, widget=forms.PasswordInput
                            (attrs={'placeholder': ' eg. mypass123'}))
    country = forms.CharField(required=True)
    city = forms.CharField(required=True)


class EditProfileForm(forms.Form):

    first_name = forms.CharField(required=False, widget=forms.TextInput
                            (attrs={'placeholder': ' myfirstname'}))
    last_name = forms.CharField(required=False,widget=forms.TextInput
                            (attrs={'placeholder': ' mylastname'}))
    email = forms.EmailField(required=True, widget=forms.TextInput
                            (attrs={'placeholder': ' myemail@gmail.com'}))
    country = forms.CharField(required=True)
    city = forms.CharField(required=True)