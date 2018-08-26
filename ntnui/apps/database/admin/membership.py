from django.contrib import admin
from ..models import MembershipModel
from ..models import CommentModel
from .admin import NtnuiAdmin
from nested_admin import NestedStackedInline


class CommentInline(NestedStackedInline):
    model = CommentModel


@admin.register(MembershipModel)
class MembershipAdmin(NtnuiAdmin):
    search_fields = ['member', 'group', 'payment',
                     'group_expiry', 'sports_license_expiry', 'sports_license_no', 'date_joined']
    inlines = [CommentInline]
    exclude = ('comment', )

    # Use fields here to be able to control the order of the fields
    fields = ('member', 'group', 'date_joined', 'group_expiry',
              'sports_license_expiry', 'sports_license_no', )

    ''' Make the membership read-only '''

    def has_add_permission(self, request):
        # Nobody is allowed to add
        return False

    def has_delete_permission(self, request, obj=None):
        # Nobody is allowed to delete
        return False

    def save_model(self, request, obj, form, change):
        # Return nothing to make sure user can't update any data
        pass

    ''' List view details '''
    list_display = ("member", "group", "date_joined", "group_expiry")
