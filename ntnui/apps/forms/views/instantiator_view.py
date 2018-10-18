from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from ..form_types import instantiation_forms
from forms.models import FormTextModel
from forms.actions import Actions

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
        actions = Actions(model_instance)
        actions.do()
        # get formtext with highest primary key
        form_text_id = FormTextModel.objects.filter(form_slug=slug).last().id
        setattr(model_instance, 'meta_version', form_text_id)
        #model_instance.notify_signers()
        model_instance.save()
        return HttpResponse("Form instantiated")
