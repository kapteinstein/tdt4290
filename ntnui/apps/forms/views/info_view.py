from django.shortcuts import render, get_object_or_404
from django.views import View
from forms.models import FormTextModel, AbstractFormModel
from django.http import HttpResponseForbidden

class InfoView(View):
    def get(self, request, slug, id):
        form_instance = get_object_or_404(AbstractFormModel, pk=id)
        form_text = FormTextModel.objects.get(id=form_instance.meta_version)
        signatures = form_instance.form_signatures.all()
        signers = form_instance.form_signers.all()
        user = request.user
        print(signatures)
        print(signers)
        if user in signatures or user not in signers:
            return HttpResponseForbidden()
        context = {
            'form_id': id,
            'form_text': form_text.form_text_content,
            'form_slug': slug
        }
        return render(request, 'form_info.html', context)

