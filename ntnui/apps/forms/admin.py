from django.contrib import admin
from .models import AbstractFormModel, CoachFormModel, FormTextModel, TeamContractFormModel

admin.site.register(AbstractFormModel)
admin.site.register(CoachFormModel)
admin.site.register(FormTextModel)
admin.site.register(TeamContractFormModel)