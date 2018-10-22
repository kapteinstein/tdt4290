from django.shortcuts import render
from django.views import View
from ..form_types import signing_forms
from forms.models import AbstractFormModel
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied


class SignerView(View):
    def get(self, request, slug, id):
        try:
            # Gets the joined form thanks to inheriting from polymorphic model
            record = AbstractFormModel.objects.get(id=id)
            form = signing_forms[slug](request.POST or None, instance=record)
            signatures = record.form_signatures.all()
            signers = record.form_signers.all()
            user = request.user
            if user in signatures or user not in signers:
                raise PermissionDenied
            else:
                context = {
                    'form': form,
                    'id': record.id,
                    'record': record,
                }
                return render(request, 'form_signer.html', context)
        except ObjectDoesNotExist:
            raise Http404("Could not find form record")

    def post(self, request, slug, id):
        record = AbstractFormModel.objects.get(id=id)
        form = signing_forms[slug](request.POST or None, instance=record)
        request.session['record_id'] = id
        request.session['sign_level'] = record.get_required_sign_level()

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forms:sign')) # TODO Display success page
        return render(request, 'form_signer.html', {'form': form, 'id': record.id})

