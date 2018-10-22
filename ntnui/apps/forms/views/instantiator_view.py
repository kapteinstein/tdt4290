from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ..form_types import instantiation_forms
from forms.models import FormTextModel
from forms.actions import Actions

class InstantiatorView(View):

    def get(self, request, slug):
        form = instantiation_forms[slug]()
        context = {
            'form': form
        }
        return render(request, 'form_instantiator.html', context)

    def post(self, request, slug):
        form = instantiation_forms[slug](request.POST)
        model_instance = form.save(commit=True)
        actions = Actions(model_instance)
        actions.do()
        # get formtext with highest primary key
        form_text_id = FormTextModel.objects.filter(form_slug=slug).last().id
        setattr(model_instance, 'meta_version', form_text_id)
        #model_instance.notify_signers()
        model_instance.save()
        return HttpResponse("Form instantiated")

from database.models import GroupModel, UserModel
from django.db import models
from django import forms as djangoforms
from ..form_types import *

# TODO make list of slug in form types
FORM_CHOICES = (
    ("coach", "coach"),
    ("beep", "beep"),
    ("boop", "boop"),
)

class InstantiateForm(djangoforms.Form):
    group_choices=(tuple([(group.group_id, group) for group in GroupModel.objects.all()]))
    group = djangoforms.ChoiceField(choices=group_choices)
    form_signers = djangoforms.ChoiceField()
    form_slug = djangoforms.ChoiceField(choices=FORM_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        group_widget = {'onchange': 'location = "//" + location.host + location.pathname+"?group="+this.value',
                        'class': 'uk-select'}
        self.fields['group'].widget.attrs.update(group_widget)
        self.fields['group'].label = "Gruppe"
        self.fields['form_signers'].widget.attrs.update({'class': 'uk-select'})
        self.fields['form_signers'].label = "Signerer"
        self.fields['form_slug'].widget.attrs.update({'class': 'uk-select'})
        self.fields['form_slug'].label = "Skjema"


class NewInstantiatorView(View):

    def get(self, request):
        form = InstantiateForm()
        group = request.GET.get('group')
        if not group:
                group = form.fields['group'].choices[0][0]

        form.fields['group'].initial = group
        members = GroupModel.objects.get(group_id = group).members.filter()
        form.fields['form_signers'].choices = tuple([(user.ntnui_no, user) for user in members])
        context = {
            'form': form
        }
        return render(request, 'new_form_instantiator.html', context)


    def post(self, request):
        form = InstantiateForm(request.POST)
        if form.is_valid():
            slug = form.cleaned_data['form_slug']
            group = form.cleaned_data['group']
            signee = form.cleaned_data['form_signers']
            model_instance = FORM_TYPES[slug].objects.create()
            model_instance.form_signers.set(signee)
            model_instance.group = GroupModel.objects.get(group_id=group)
            actions = Actions(model_instance)
            actions.do()
            # get formtext with highest primary key
            form_text_id = FormTextModel.objects.filter(form_slug=slug).last().id
            setattr(model_instance, 'meta_version', form_text_id)
            # model_instance.notify_signers()
            model_instance.save()
            return HttpResponse("Form instantiated")
        else:
            return "invalid form"
