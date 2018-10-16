from django.shortcuts import render
from django.views import View
from django import forms
from forms.models import CoachFormModel, AbstractFormModel
from database.models import MembershipModel, GroupModel
from database.models.enums import ROLE_CHOICES
from forms.form_types import FORM_TYPES
from forms.utils import form_utils

class IncomingView(View):

    def get(self, request):
        current_user = request.user
        # TODO make it possible to look at a forms contents after signing
        forms = AbstractFormModel.objects.filter(form_signers=current_user).filter(form_completed=False)

        context = {
            'current_user': current_user,
            'forms': forms,
            'navbar': 'incoming-list',
            'is_authorized': form_utils.is_authorized(current_user),
        }
        return render(request, 'incoming_list.html', context)


class OutgoingView(View):

    def get(self, request):
        current_user = request.user
        forms = AbstractFormModel.objects.filter(form_instantiator=current_user).filter(form_completed=False)

        context = {
            'forms': forms,
            'navbar': 'outgoing-list',
            'is_authorized': form_utils.is_authorized(current_user),
        }
        return render(request, 'outgoing_list.html', context)


class InstantiateListView(View):
    def get(self, request):
        current_user = request.user
        is_authorized = False
        for group in GroupModel.objects.all():
            if current_user not in group:
                continue
            if group.board.get_role(current_user) == "President/Leader":
                is_authorized = True
                break

        if is_authorized:
            form_models = FORM_TYPES.values
        else:
            form_models = None

        context = {
            'forms': FORM_TYPES.values,
            'navbar': 'instantiate-form-list', # Slett?
            'is_authorized': form_utils.is_authorized(current_user),

        }
        return render(request, 'instantiate_form_list.html', context)