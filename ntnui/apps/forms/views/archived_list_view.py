from django.shortcuts import render
from django.views import View
from forms.models import CoachFormModel, AbstractFormModel
from database.models import MembershipModel, GroupModel
from database.models.enums import ROLE_CHOICES
from forms.form_types import FORM_TYPES

class IncomingArchiveView(View):

    def get(self, request):
        current_user = request.user
        forms = AbstractFormModel.objects.filter(form_signers=current_user).filter(form_completed=True)

        context = {
            'forms': forms,
            'navbar': 'archive',
            'archive_navbar': 'incoming-list',
        }
        return render(request, 'archived_incoming_list.html', context)


class OutgoingArchiveView(View):

    def get(self, request):
        current_user = request.user
        forms = AbstractFormModel.objects.filter(form_instantiator=current_user).filter(form_completed=True)

        context = {
            'forms': forms,
            'navbar': 'archive',
            'archive_navbar': 'outgoing-list',
        }
        return render(request, 'archived_outgoing_list.html', context)
