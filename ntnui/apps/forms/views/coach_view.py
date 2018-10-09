from django.shortcuts import render
from django.views import View
from forms.models import CoachInstantiationForm, CoachSigningForm, CoachFormModel

class CoachInstantiatorView(View):
    def get(self, request):
        if request.method == 'post':
            form = CoachInstantiationForm(request.POST)
            model_instance = form.save(commit=True)
            model_instance.save()

        else:
            form = CoachInstantiationForm()


        # record = CoachModel.objects.get(id=1)
        # form = CoachSigningForm(instance=record)

        context = {
            'form': form
        }

        return render(request, 'coach_instantiator.html', context)

class CoachSignerInfoView(View):
    def get(self, request):
        context = {}
        return render(request, 'coach_info.html', context)        

class CoachSignerView(View):
    def get(self, request):
        if request.method == 'post':
            form = CoachSigningForm(request.POST)
            print(form.id)
            model_instance = form.save(commit=True)
            model_instance.save()

        else:
            form = CoachSigningForm()


        """ record = CoachModel.objects.get(id=1)
        form = CoachSigningForm(instance=record) """

        context = {
            'form'      : form,
        }
        return render(request, 'coach_signer.html', context)