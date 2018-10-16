from django import forms

class SignForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())