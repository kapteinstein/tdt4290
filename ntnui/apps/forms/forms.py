from django import forms
from .form_types import *

class SignForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    password.label = "Skriv inn ditt passord for å signere skjema"


"""
InstantiateForm is a django form used to instantiate a model form of any type present in FORM_TYPES.
This form is used in InstantiatorView.
form_choices are fetched from FORM_TYPES and made into a tuple for the sake of the input field.
Arguments in __init__ are used to specify the possible input values and the initial group.
The initial group is used in InstantiatorView to restrict the possible form_signers to the members of the group.

Group field has a widget with a JavaScript snippet that refreshes the page and puts the chosen group's id in the url.
This is used when a person is able to send out forms in multiple groups. This causes the form signers to be sorted
by group again. 
"""
class InstantiateForm(forms.Form):
    group = forms.ChoiceField()
    form_signers = forms.ChoiceField()
    form_choices = tuple([(key, value.form_name) for key,value in FORM_TYPES.items()])
    form_slug = forms.ChoiceField(choices=form_choices)

    def __init__(self,form_signers,group,groups, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['group'].choices = groups
        self.fields['group'].initial = group
        group_widget = {'onchange': 'location = "//" + location.host + location.pathname+"?group="+this.value',
                        'class': 'uk-select'}
        self.fields['group'].widget.attrs.update(group_widget)
        self.fields['group'].label = "Gruppe"

        self.fields['form_signers'].choices = form_signers
        self.fields['form_signers'].widget.attrs.update({'class': 'uk-select'})
        self.fields['form_signers'].label = "Mottaker"

        self.fields['form_slug'].widget.attrs.update({'class': 'uk-select'})
        self.fields['form_slug'].label = "Skjema"