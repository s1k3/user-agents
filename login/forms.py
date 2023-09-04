from django import forms

class LogInUser(forms.Form):
    password = forms.CharField(max_length = 50)
    email = forms.CharField(max_length = 50)