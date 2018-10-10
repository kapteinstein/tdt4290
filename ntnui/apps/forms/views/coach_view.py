from django.shortcuts import render
from django.views import View
from forms.models import CoachInstantiationForm, CoachSigningForm, CoachFormModel
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden

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
        model_instance.notify_signers()
        model_instance.save()

        context = {
            'form': form
        }
        return HttpResponse("Form instantiated")

class CoachSignerInfoView(View):
    def get(self, request):
        context = {
        }
        return render(request, 'coach_info.html', context)        

class CoachSignerView(View):
    def get(self, request):
        try:
            record = CoachFormModel.objects.get(id=request.GET.get('id')) # TODO Needs to be modified to Jans URL
            form = CoachSigningForm(request.POST or None, instance=record)
            form_signers = record.form_signers.all()
            if (request.user in form_signers):
                context = {
                    'form': form,
                    'id': record.id,
                }
                return render(request, 'coach_signer.html', context)
            else: 
                return HttpResponseForbidden("Denied Access")
        except ObjectDoesNotExist:
            raise Http404("Could not find form record")
        # example urL: http://localhost:8000/f/2?id=2#

    def post(self, request):
        # TODO Add verification before adding user to signature-list
        record = CoachFormModel.objects.get(id=request.GET.get('id'))
        form = CoachSigningForm(request.POST or None, instance=record)
        if form.is_valid():
            record.form_signatures.add(request.user)
            if record.is_form_completed():
                record.form_completed = True
                print(record.form_completed)
            form.save()
            return HttpResponse("valid")

        return HttpResponse("invalid")

class 