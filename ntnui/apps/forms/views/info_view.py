from django.shortcuts import render
from django.views import View

from forms.models import FormTextModel, AbstractFormModel


class InfoView(View):
    def get(self, request,slug, id):
        # TODO use request slug instead of instance slug
        form_instance = AbstractFormModel.objects.get(id=id)
        current_version = form_instance.meta_version
        form_slug = form_instance.form_slug
        form_text = FormTextModel.objects.get(form_name=form_slug,form_text_version_number=current_version)
        context = {
            'form_id': id,
            'form_text': form_text.form_text_content,
            'form_slug': form_slug
        }
        return render(request, 'form_info.html', context)