from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Signup(UserCreationForm):
    emails = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email address'}))
    first_name = forms.CharField(label="", max_length=120,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}))
    last_name = forms.CharField(label="",  max_length=120,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')