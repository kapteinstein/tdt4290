"""
SignView

This view is presented to the user when the user generate the signature.
The current system supports only password authentication, but higher order types
of authentication should be implementet as future work.

Required signature type/level are specified in abstract_form_model.py.
Available labels are:
    0: password authentication
    1: paper signature or BankID

"""

from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

from forms.models import *
from forms.forms import SignForm
from forms.actions import Actions

class SignView(View):
    def get(self, request):
        sign_level = request.session.get('sign_level', 1)  # fallback on high sign level (1)

        if sign_level == 1:
            return HttpResponse('paper signature or BankID required')

        form = SignForm()
        return render(request, 'confirm_password.html', {'form': form})

    def post(self, request):
        sign_level = request.session.get('sign_level', 1)
        record_id = request.session.get('record_id', False)
        record = AbstractFormModel.objects.get(id=record_id)

        if sign_level == 1:
            return HttpResponse('paper signature or BankID required')

        password_form = SignForm(request.POST)
        if password_form.is_valid():
            password = password_form.cleaned_data['password']
            if request.user.check_password(password):
                record.form_signatures.add(request.user)
                if record.is_form_completed():
                    record.form_completed = True
                record.save()
                try:
                    actions = Actions(record)
                    actions.do()
                except:
                    pass
                return HttpResponseRedirect(reverse('forms:archive-incoming-list'))
        password_form.add_error(None, "Feil passord")
        return render(request, 'confirm_password.html', {'form': password_form, 'form_error': 'feil passord'})
