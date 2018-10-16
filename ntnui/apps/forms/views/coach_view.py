from django.shortcuts import render
from django.views import View

from forms.models import CoachInstantiationForm, CoachSigningForm, CoachFormModel
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponseForbidden, HttpResponseRedirect

from django.urls import reverse


class CoachInstantiatorView(View):

    def get(self, request):
        form = CoachInstantiationForm()
        context = {
            'form': form
        }
        return render(request, 'coach_instantiator.html', context)

    def post(self, request):
        form = CoachInstantiationForm(request.POST)
        model_instance = form.save(commit=True)
        #model_instance.notify_signers()
        model_instance.save()
        return HttpResponse("Form instantiated")

class CoachSignerInfoView(View):
    def get(self, request, id):
        context = {
            'form_id': id
        }
        return render(request, 'coach_info.html', context)

class CoachSignerView(View):
    def get(self, request, id):
        try:
            record = CoachFormModel.objects.get(id=id) # TODO Needs to be modified to Jans URL
            form = CoachSigningForm(request.POST or None, instance=record)
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
                return render(request, 'coach_signer.html', context)
        except ObjectDoesNotExist:
            raise Http404("Could not find form record")
        # example urL: http://localhost:8000/f/2?id=2#

    def post(self, request, id):
        record = CoachFormModel.objects.get(id=id)
        form = CoachSigningForm(request.POST or None, instance=record)
        request.session['record_id'] = id

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forms:sign')) # TODO Display success page
        return render(request, 'coach_signer.html', {'form': form, 'id': record.id})
