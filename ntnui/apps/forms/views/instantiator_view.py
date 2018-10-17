from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .form_types import instantiation_forms


class InstantiatorView(View):

    def get(self, request, slug):
        form = instantiation_forms[slug]()
        context = {
            'form': form
        }
        return render(request, 'form_instantiator.html', context)

    def post(self, request, slug):
        form = instantiation_forms[slug](request.POST)
        model_instance = form.save(commit=True)
        setattr(model_instance, 'meta_version', model_instance.current_version)
        #model_instance.notify_signers()
        model_instance.save()
        return HttpResponse("Form instantiated")
