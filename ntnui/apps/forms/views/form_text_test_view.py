from django.shortcuts import render
from django.views import View
from forms.models import FormTextModel

# TODO implement or delete
class FormTextTestView(View):
    def get(self, request):


        formText = FormTextModel.objects.get(id=1)
        formTextHTML = formText.form_text_content

        context = {
            'html_content': formTextHTML
        }

        return render(request, 'form_text_test_view.html', context)