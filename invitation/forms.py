from django import forms
from django.forms import TextInput, FileInput, Select

from invitation.models import Invitation


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['title', 'description', 'date', 'venue', 'dress_code', 'img_upload']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your title'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'date': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'venue': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the venue location'}),
            'dress_code': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your wedding dresscode'}),

        }


class InvitationUpdateForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['title', 'description', 'date', 'venue', 'dress_code', 'img_upload']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your title'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your description'}),
            'date': TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'venue': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the venue location'}),
            'dress_code': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your wedding dresscode'}),

        }


