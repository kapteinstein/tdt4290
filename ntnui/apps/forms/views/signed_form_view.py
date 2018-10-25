from django.shortcuts import render
from django.views import View
from ..models import AbstractFormModel, FormTextModel
from ..utils import form_utils
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import Http404
from ..form_types import *


class SignedFormView(View):

    def get(self, request, slug, id):
        try:
            current_user = request.user
            record = AbstractFormModel.objects.get(id=id)
            if current_user not in record.form_signers.all():
                raise PermissionDenied

            form_text = FormTextModel.objects.get(id=record.meta_version)
            form = signing_forms[slug](request.POST or None, instance=record)

            context = {
                'current_user': current_user,
                'record': record,
                'form': form,
                'form_text': form_text.form_text_content,
                'is_authorized': form_utils.is_authorized(current_user),
            }
            return render(request, 'form_signed_info.html', context)
        except ObjectDoesNotExist:
            raise Http404("Could not find form record")
