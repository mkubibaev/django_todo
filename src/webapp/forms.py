from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class TodoForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Title')
    date = forms.CharField(max_length=20, required=False, label='Date')
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Status')
    content = forms.CharField(max_length=3000, required=True, label='Description', widget=widgets.Textarea)