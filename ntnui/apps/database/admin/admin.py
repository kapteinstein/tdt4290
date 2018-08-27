from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib import admin
from django.http import HttpResponse
from nested_admin import NestedModelAdmin
import csv

SKIP_FIELDS = ['password', 'last_login',
               'is_superuser', 'is_admin', 'is_staff']


class NtnuiAdmin(NestedModelAdmin):
    ''' Actions '''
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        # Filter out any of the SKIP_FIELDS mentioned above
        fields = list(filter(lambda f: f not in SKIP_FIELDS, field_names))

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            meta)
        writer = csv.writer(response, delimiter=',', dialect='excel',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(fields)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field)
                                   for field in fields])

        return response

    export_as_csv.short_description = "Export Selected"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
