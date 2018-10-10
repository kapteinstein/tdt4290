from django.shortcuts import render
from django.views import View
from forms.models import CoachFormModel, AbstractFormModel
from database.models import MembershipModel, GroupModel
from forms.form_types import FORM_TYPES


class IncomingView(View):

    def get(self, request):
        current_user = request.user
        forms = AbstractFormModel.objects.filter(form_signers=current_user)

        context = {
            'forms': forms,
            'navbar': 'incoming-list',
        }
        # if none print "Det finnes ingen skjema til signering"
        return render(request, 'incoming_list.html', context)


class OutgoingView(View):

    def get(self, request):
        current_user = request.user
        forms = AbstractFormModel.objects.filter(form_instantiator=current_user)

        context = {
            'forms': forms,
            'navbar': 'outgoing-list',
        }
        # if none print "Det finnes ingen skjema til signering"
        return render(request, 'outgoing_list.html', context)