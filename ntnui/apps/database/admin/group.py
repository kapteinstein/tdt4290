from django.contrib import admin
from ..models import GroupModel
from ..models import GroupMetaModel
from ..models import GroupMediaModel
from ..models import BoardModel
from ..models import RoleModel
from ..models import GroupRelationshipModel
from .admin import NtnuiAdmin
import nested_admin


class GroupMetaInline(nested_admin.NestedStackedInline):
    model = GroupMetaModel


class GroupMediaInline(nested_admin.NestedStackedInline):
    model = GroupMediaModel


class RoleInline(nested_admin.NestedStackedInline):
    model = RoleModel

    # Default to three roles, max 50
    extra = 3
    max_num = 50


class BoardInline(nested_admin.NestedStackedInline):
    model = BoardModel
    inlines = [RoleInline]


class GroupRelationshipInline(nested_admin.NestedStackedInline):
    model = GroupRelationshipModel

    # Reference to the related name in the GroupRelationshipModel
    fk_name = "parent_group"
    extra = 1
    max_num = 50


@admin.register(GroupModel)
class GroupAdmin(nested_admin.NestedModelAdmin):
    search_fields = ['name', 'founding_date']

    # Exclude the group media and meta as these are loaded inline
    exclude = ('group_media', 'group_meta',)
    inlines = [GroupRelationshipInline,
               GroupMetaInline, GroupMediaInline, BoardInline]
    list_display = ('name',)
