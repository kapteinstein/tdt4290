from django.db import models
from django import forms
from forms.models import AbstractFormModel, enums, FormTextModel
from datetime import datetime

class CoachFormModel(AbstractFormModel):

    position = models.IntegerField(choices=enums._POSITION, null=True)
    start_date = models.DateField(null=True)
    compensation = models.IntegerField(choices=enums._COMPENSATIONS, null=True)
    compensation_comments = models.TextField(blank=True)

    form_name = "Midlertidig ansettelse"
    form_slug = 'coach'
    required_sign_type = 0
    actions = [
        "notify_signers",
    ]

class CoachSigningForm(forms.ModelForm):
    class Meta:
        model = CoachFormModel
        fields = ['position', 'compensation', 'compensation_comments', 'start_date']
        labels = {
            'position': 'Posisjon',
            'compensation': 'Kompensasjon',
            'compensation_comments': 'Kommentarer',
            'start_date': 'Startdato',
        }
        widgets = {
            'position': forms.Select(attrs={'class': 'uk-select'}),
            'compensation': forms.Select(attrs={'class': 'uk-select'}),
            'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'value': datetime.now(),  'type':'date'}),
            'compensation_comments': forms.Textarea(attrs={'class': 'uk-textarea', 'rows':3}),
        }

