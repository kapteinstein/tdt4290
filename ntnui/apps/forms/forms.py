from django import forms
from .form_types import *

class SignForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['password'].widget.attrs.update({'class':'uk-form-password'})
        
class InstantiateForm(forms.Form):
    group = forms.ChoiceField()
    form_signers = forms.ChoiceField()
    form_choices = tuple([(key, value.form_name) for key,value in FORM_TYPES.items()])
    form_slug = forms.ChoiceField(choices=form_choices)

    def __init__(self,form_signers,group,groups, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].choices = groups
        self.fields['group'].initial = group
        self.fields['form_signers'].choices = form_signers
        group_widget = {'onchange': 'location = "//" + location.host + location.pathname+"?group="+this.value',
                        'class': 'uk-select'}
        self.fields['group'].widget.attrs.update(group_widget)
        self.fields['group'].label = "Gruppe"
        self.fields['form_signers'].widget.attrs.update({'class': 'uk-select'})
        self.fields['form_signers'].label = "Signerer"
        self.fields['form_slug'].widget.attrs.update({'class': 'uk-select'})
        self.fields['form_slug'].label = "Skjema"