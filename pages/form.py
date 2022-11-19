from django import forms

from .models import *
from django.forms import ModelForm


class ContactsForm(ModelForm):
    class Meta:
        model = Contact_Form
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
        labels = {'body': 'Comment'}
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'cols': 30,
                'placeholder': 'Enter your comment here '
            })
        }


class ResponseForm(ModelForm):
    class Meta:
        model = Responses
        fields = ['body']
        labels = {'body': 'Answer'}
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'cols': 10,
                'placeholder': 'Answer to this comment here'
            })
        }
