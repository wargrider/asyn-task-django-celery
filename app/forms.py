# -*- coding: utf-8 -*-

# Django Imports
from django import forms


class MessageForm(forms.Form):
    """
    Form to send Email
    """
    receiver = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

