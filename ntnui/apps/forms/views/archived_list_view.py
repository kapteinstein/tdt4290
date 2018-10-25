from django.shortcuts import render
from django.views import View
from forms.models import AbstractFormModel
from forms.utils import form_utils

class IncomingArchiveView(View):

    def get(self, request):
        current_user = request.user
        forms = AbstractFormModel.objects.filter(form_signers=current_user,form_completed=True).order_by("-form_modified_time")
       
        context = {
            'forms': forms,
            'navbar': 'archive',
            'archive_navbar': 'incoming-list',
            'is_authorized': form_utils.is_authorized(current_user),
        }
        return render(request, 'archived_incoming_list.html', context)


class OutgoingArchiveView(View):

    def get(self, request):
        current_user = request.user
        forms = AbstractFormModel.objects.filter(form_instantiator=current_user, form_completed=True).order_by("-form_created_time")
        
        context = {
            'forms': forms,
            'navbar': 'archive',
            'archive_navbar': 'outgoing-list',
            'is_authorized': form_utils.is_authorized(current_user),
        }
        return render(request, 'archived_outgoing_list.html', context)
