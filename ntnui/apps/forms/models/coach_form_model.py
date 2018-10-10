from django.db import models
from django import forms
from forms.models import AbstractFormModel, enums
from datetime import datetime


class CoachFormModel(AbstractFormModel):

    position = models.IntegerField(choices=enums._POSITION)
    start_date = models.DateField()
    group = models.ForeignKey('database.GroupModel', on_delete=models.CASCADE, related_name="group")
    compensation = models.IntegerField(choices=enums._COMPENSATIONS)
    compensation_comments = models.TextField(null=False, blank=True)

    form_name = "Midlertidig ansettelse"
    form_slug = 'coach'
    required_sign_type = 0


class CoachInstantiationForm(forms.ModelForm):
    class Meta:
        model = CoachFormModel
        fields = ['form_signers', 'form_approvers']

class CoachSigningForm(forms.ModelForm):
    class Meta:
        model = CoachFormModel
        fields = ['position', 'group', 'compensation', 'compensation_comments', 'start_date']
        widgets = {
            'position': forms.Select(attrs={'class': 'uk-select'}),
            'group': forms.Select(attrs={'class': 'uk-select'}),
            'compensation': forms.Select(attrs={'class': 'uk-select'}),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'value': datetime.now(),  'type':'date'}),
            'compensation_comments': forms.Textarea(attrs={'class': 'uk-textarea', 'rows':3}),    

        }
