from django.contrib import admin

from ..models import UserModel


class UserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']

    def get_list_display(self, request):
        return ('id', 'first_name', 'last_name')


admin.site.register(UserModel, UserAdmin)
