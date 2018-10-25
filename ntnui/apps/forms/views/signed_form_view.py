from django.shortcuts import render, get_object_or_404
from django.views import View
from ..models import AbstractFormModel, FormTextModel
from ..utils import form_utils
from django.http import HttpResponseForbidden
from ..form_types import *


class SignedFormView(View):

    def get(self, request, slug, id):
            current_user = request.user
            record = get_object_or_404(AbstractFormModel, pk=id)
            if current_user not in record.form_signers.all():
                return HttpResponseForbidden()

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
      