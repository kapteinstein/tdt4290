from django.contrib import admin
from django.forms.models import BaseInlineFormSet, ModelForm
from ..models import GroupModel
from ..models import GroupMetaModel
from ..models import GroupMediaModel
from ..models import BoardModel
from ..models import RoleModel
from ..models import GroupRelationshipModel
from ..models import GroupInvitationModel
from .admin import NtnuiAdmin
import nested_admin


class RequiredInlineFormSet(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        form.empty_permitted = False
        return form


class ForceChangeForm(ModelForm):
    ''' Override the has_changed method in order to always save the default media '''

    def has_changed(self):
        return True


class GroupMetaInline(nested_admin.NestedStackedInline):
    model = GroupMetaModel
    formset = RequiredInlineFormSet


class GroupMediaInline(nested_admin.NestedStackedInline):
    model = GroupMediaModel
    form = ForceChangeForm

    fieldsets = (
        ('Logo', {'fields': ('logo', 'logo_tag',)}),
        ('Cover', {'fields': ('cover', 'cover_tag',)})
    )
    readonly_fields = ('logo_tag', 'cover_tag')


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
    fk_name = "child_group"
    extra = 1
    max_num = 50


class GroupInvitationsInline(nested_admin.NestedStackedInline):
    model = GroupInvitationModel


@admin.register(GroupModel)
class GroupAdmin(NtnuiAdmin):
    search_fields = ['name', 'founding_date']
    exclude = ('meta', 'media',)

    # Exclude the group media and meta as these are loaded inline
    inlines = [GroupRelationshipInline,
               GroupMetaInline, GroupMediaInline, BoardInline, GroupInvitationsInline]
    list_display = ('name',)
