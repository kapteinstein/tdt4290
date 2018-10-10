from django.contrib import admin
from .models import AbstractFormModel
from .models import CoachFormModel
from .models import FormTextModel

admin.site.register(AbstractFormModel)
admin.site.register(CoachFormModel)
admin.site.register(FormTextModel)