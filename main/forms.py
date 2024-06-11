from django import forms
from .models import DimHub

class LoginForm(forms.Form):
    username = forms.ModelChoiceField(
        queryset=DimHub.objects.all(),
        to_field_name='username',
        empty_label="Select a hub",
        widget=forms.Select(attrs={'class': 'form-control'})
    )    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'})  # Ensure the correct class is used here
    )
