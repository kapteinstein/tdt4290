from django.contrib import admin

from ..models import UserModel
from ..models import MembershipModel
from ..models import CommentModel
from nested_admin import NestedStackedInline
from .admin import NtnuiAdmin


class CommentInline(NestedStackedInline):
    model = CommentModel


class MembershipInline(NestedStackedInline):
    model = MembershipModel
    inlines = [CommentInline]

    # Default to one membership, max 50
    extra = 1
    max_num = 50

    # Use fields here to be able to control the order of the fields
    fields = ('member', 'group', 'date_joined', 'group_expiry',
              'sports_license_expiry', 'sports_license_no', )
    exclude = ('comment',)


@admin.register(UserModel)
class UserAdmin(NtnuiAdmin):
    search_fields = ['ntnui_no', 'first_name', 'last_name',
                     'email', 'phone_no', 'register_date', 'gender']

    inlines = [MembershipInline]
    exclude = ('last_login', 'is_active', 'is_superuser', 'is_admin',
               'is_staff', 'groups', 'user_permissions')

    ''' List view details '''
    list_display = ("ntnui_no", "first_name", "last_name",
                    "email", "register_date")
