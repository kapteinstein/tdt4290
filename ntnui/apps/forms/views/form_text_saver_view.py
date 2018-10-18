from django.shortcuts import render
from django.views import View
from forms.models import FormTextModel, FormTextSaverForm
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseForbidden

# TODO finish or delete
class FormTextSaverView(View):

    def get(self, request):
        form = FormTextSaverForm()
        context = {
            'form': form
        }
        return render(request, 'form_text_saver_view.html', context)

    def post(self, request):

        form = FormTextSaverForm(request.POST)
        model_instance = form.save(commit=True)
        model_instance.save()

        return HttpResponse("hei")

