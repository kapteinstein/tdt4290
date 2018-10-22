from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from forms.models import FormTextModel
from forms.actions import Actions
from database.models import GroupModel, UserModel
from django import forms as djangoforms
from ..form_types import *
from ..utils.form_utils import *
from django.core.exceptions import PermissionDenied


class InstantiateForm(djangoforms.Form):
    group = djangoforms.ChoiceField()
    form_signers = djangoforms.ChoiceField()
    form_choices = tuple([(key, value.form_name) for key,value in FORM_TYPES.items()])
    form_slug = djangoforms.ChoiceField(choices=form_choices)

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


class InstantiatorView(View):

    def get(self, request):
        form = self.get_form(request)
        context = {
            'form': form
        }
        return render(request, 'form_instantiator.html', context)

    def post(self, request):
        form = self.get_form(request)
        if form.is_valid():
            slug = form.cleaned_data['form_slug']
            group = form.cleaned_data['group']
            signee = form.cleaned_data['form_signers']
            model_instance = FORM_TYPES[slug].objects.create()
            model_instance.form_signers.set(signee)
            model_instance.group = GroupModel.objects.get(group_id=group)
            model_instance.form_instantiator = request.user
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

    def get_form(self,request):
        current_user = request.user
        leader_groups = get_leader_groups(current_user)
        if not leader_groups:
            raise PermissionDenied
        groups = tuple([(group.group_id, group) for group in leader_groups])
        group = request.GET.get('group')
        if not group:
            group = groups[0][0]
        else:
            valid_group = False
            for g in groups:
                if int(g[0]) == int(group):
                    valid_group = True
                    break
            if not valid_group:
                raise PermissionDenied

        members = GroupModel.objects.get(group_id=group).members.filter()
        form_signers = tuple([(user.ntnui_no, user) for user in members])
        if request.POST:
            return InstantiateForm(form_signers, group, groups, request.POST)
        else:
            return InstantiateForm(form_signers, group, groups)
