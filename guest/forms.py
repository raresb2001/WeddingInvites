from django import forms
from django.forms import TextInput, Select

from guest.models import Guest


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name','is_attending', 'profile', 'invitation']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'invitation': Select(attrs={'class': 'form-select'}),
        }

class GuestUpdateForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name','is_attending', 'profile']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'invitation': Select(attrs={'class': 'form-select'}),
        }