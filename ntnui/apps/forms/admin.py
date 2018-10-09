from django.contrib import admin
from .models import AbstractFormModel
from .models import CoachFormModel

admin.site.register(AbstractFormModel)
admin.site.register(CoachFormModel)