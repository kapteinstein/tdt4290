from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
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


class CreateUserModelForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        exclude = ('password', 'last_login', 'is_active', 'is_superuser', 'is_admin',
                   'is_staff', 'groups', 'user_permissions')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(CreateUserModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ChangeUserModelForm(CreateUserModelForm):
    password = ReadOnlyPasswordHashField()
    password1 = forms.CharField(
        label='New Password', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(
        label='New Password confirmation', widget=forms.PasswordInput, required=False)

    class Meta:
        model = UserModel
        exclude = ('last_login', 'is_active', 'is_superuser', 'is_admin',
                   'is_staff', 'groups', 'user_permissions')

    def clean_password(self):
        return self.initial["password"]


@admin.register(UserModel)
class UserAdmin(BaseUserAdmin, NtnuiAdmin):
    form = ChangeUserModelForm
    add_form = CreateUserModelForm

    inlines = [MembershipInline]

    fieldsets = (
        (None, {'fields': ('email', 'password', 'password1', 'password2')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'date_of_birth',
                                      'gender', 'language', 'calling_code', 'phone_no')}),
        ('Membership Details', {'fields': (
            'customer_no', 'register_date', 'card_no', 'contract_no', 'contract_expiry_date')})
    )

    add_fieldsets = (
        (None, {'classes': ('wide'), 'fields': (
            'email', 'password1', 'password2')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'date_of_birth',
                                      'gender', 'language', 'calling_code', 'phone_no')}),
        ('Membership Details', {'fields': (
            'customer_no', 'register_date', 'card_no', 'contract_no', 'contract_expiry_date')})
    )

    filter_horizontal = ()

    ''' List view details '''
    list_display = ("ntnui_no", "first_name", "last_name",
                    "email", "register_date")
    search_fields = ['ntnui_no', 'first_name', 'last_name',
                     'email', 'phone_no', 'register_date', 'gender']
    ordering = ('email',)
