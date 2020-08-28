from django import forms
from . import models


class AssignmentAddForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = ['title', 'subject', 'submission_date', 'question']