from django.shortcuts import render
from forms.models import AbstractForm, CashierModel, TrusteeModel
from forms.models import CashierForm, TrusteeForm
from django.http import HttpResponseRedirect
from django.urls import reverse

formsets = {
    'trustee': TrusteeForm(),
    'cashier': CashierForm(),
}

form_models = {
    'trustee': TrusteeModel,
    'cashier': CashierModel,
}


def form_create(request, form_slug):
    template_name = 'form_create.html'

    context = {
        'is_authorized': True,
        'form_name': form_models[form_slug].form_name,
        'formset': formsets[form_slug],
        'form_slug': form_slug,
    }

    return render(request, template_name, context)


def form_instantiate(request, form_slug):
    print(request.POST)
    # Extract all input without the csrf token
    fields = list(request.POST.items())[1:]
    # Instantiate the correct model
    form_model = form_models[form_slug]()
    # Set all fields according to input
    for field in fields:
        setattr(form_model, field[0], field[1])
    # Save the new instance in the database
    form_model.save()
    return HttpResponseRedirect(reverse('forms:create_form', args=(form_slug,)))
