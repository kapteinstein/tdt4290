from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect

from forms.models import *
from forms.forms import SignForm
from forms.actions import Actions


class SignView(View):
    def get(self, request):
        form = SignForm()
        return render(request, 'sign.html', {'form': form})

    def post(self, request):
        record_id = request.session.get('record_id', False)
        record = AbstractFormModel.objects.get(id=record_id)

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
                return HttpResponseRedirect(reverse('forms:incoming-list'))
        return render(request, 'sign.html', {'form': password_form, 'form_error': 'incorrect password'})
