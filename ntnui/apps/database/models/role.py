from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from datetime import date
from .enums import ROLE_CHOICES
from ..models import UserModel


def validate_user(obj):
    # Retrieve the user instance from the model object
    user = obj.member
    # Retrieve the group insance from the model object
    group = obj.board.group

    if user not in group:
        raise ValidationError("{} is not a member of {}".format(user, group))


class RoleModel(models.Model):
    ''' Role information '''
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(
        max_length=40, choices=ROLE_CHOICES, default="-")
    date_joined = models.DateField(
        default=date.today, null=False, blank=False)

    ''' Role relationships '''
    board = models.ForeignKey(
        'BoardModel', on_delete=models.CASCADE, related_name="roles")
    member = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.role + " - " + str(self.member)

    def clean(self):
        ''' This method is "magically" called by django whenever a model instance is saved '''
        validate_user(self)
