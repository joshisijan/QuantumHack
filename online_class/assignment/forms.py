from django import forms
from .models import *


class AssignmentAddForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'subject', 'submission_date', 'question']