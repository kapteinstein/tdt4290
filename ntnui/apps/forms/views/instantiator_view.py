from django.shortcuts import render
from django.views import View

from forms.models import CoachInstantiationForm, CoachSigningForm, CoachFormModel, FormTextModel, AbstractFormModel
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied

# Add here when creating a new type of form
forms = {
    CoachFormModel.form_slug: CoachInstantiationForm,
}


class InstantiatorView(View):

    def get(self, request, slug):
        form = forms[slug]()
        context = {
            'form': form
        }
        return render(request, 'form_instantiator.html', context)

    def post(self, request, slug):
        form = forms[slug](request.POST)
        model_instance = form.save(commit=True)
        setattr(model_instance, 'meta_version', model_instance.current_version)
        #model_instance.notify_signers()
        model_instance.save()
        return HttpResponse("Form instantiated")
