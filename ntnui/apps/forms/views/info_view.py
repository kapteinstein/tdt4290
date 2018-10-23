from django.shortcuts import render
from django.views import View
from forms.models import FormTextModel, AbstractFormModel
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import Http404


class InfoView(View):
    def get(self, request, slug, id):
        try:
            form_instance = AbstractFormModel.objects.get(id=id)
            form_text = FormTextModel.objects.get(id=form_instance.meta_version)
            signatures = form_instance.form_signatures.all()
            signers = form_instance.form_signers.all()
            user = request.user
            print(signatures)
            print(signers)
            if user in signatures or user not in signers:
                raise PermissionDenied
            context = {
                'form_id': id,
                'form_text': form_text.form_text_content,
                'form_slug': slug
            }
            return render(request, 'form_info.html', context)
        except ObjectDoesNotExist:
            raise Http404("Could not find form record")

