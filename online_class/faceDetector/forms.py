from django import forms
from .models import *


class AddFacesDataset(forms.ModelForm):

    class Meta:
        model = UserFacesTraining
        fields = ['user', 'image1', 'image2', 'image3', 'image4', 'image5']