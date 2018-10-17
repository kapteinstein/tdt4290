from django.shortcuts import render
from django.views import View
from .form_types import signing_forms
from forms.models import AbstractFormModel
from django.http import HttpResponse, Http404
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
                }
                return render(request, 'form_signer.html', context)
        except ObjectDoesNotExist:
            raise Http404("Could not find form record")

    def post(self, request, slug, id):
        # TODO Add verification before adding user to signature-list
        record = AbstractFormModel.objects.get(id=id)
        form = signing_forms[slug](request.POST or None, instance=record)
        if form.is_valid():
            record.form_signatures.add(request.user)
            if record.is_form_completed():
                record.form_completed = True
            form.save()
            return HttpResponse("valid") # TODO Display success page

        return HttpResponse("invalid")
