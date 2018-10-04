from django.contrib import admin
from .models import AbstractFormModel
from .models import CoachModel

admin.site.register(AbstractFormModel)
admin.site.register(CoachModel)