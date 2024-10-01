from django import forms
from .models import *


class QuestForm(forms.ModelForm):
    class Meta:
        model = Emails
        fields = ['name', 'email', 'text']
