from django.db import models
from django import forms
from forms.models import AbstractFormModel, enums, FormTextModel
from datetime import datetime

class TeamContractFormModel(AbstractFormModel):
    start_date = models.DateField(null=True)
    form_name = "Teamkontrakt"
    form_slug = "teamcontract"
    required_sign_type = 0
    actions = [
        "notify_signers",
        "notify_owner"
    ]

class TeamContractSigningForm(forms.ModelForm):
    class Meta:
        model = TeamContractFormModel
        fields = ['start_date']
        labels = {
            'start_date': 'Start-dato'
        }
        widgets = {
             'start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'value': datetime.now(),  'type':'date'}),
        }
      
     