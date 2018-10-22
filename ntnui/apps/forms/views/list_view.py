from django.shortcuts import render
from django.views import View
from forms.models import CoachFormModel, AbstractFormModel
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
