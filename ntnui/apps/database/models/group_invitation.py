from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


def member_not_in_group(obj):
    if obj.member in obj.group:
        raise ValidationError("{} is already in {}".format(
            obj.member, obj.group))


def unique_invitation(obj):
    member = obj.member
    group = obj.group

    # If an invitation object with the same members exists, raise a validation error
    if GroupInvitationModel.objects.filter(group=group, member=member):
        raise ValidationError("This user is already invited")


class GroupInvitationModel(models.Model):
    invitation_id = models.AutoField(primary_key=True)

    ''' Invitation details '''
    member = models.ForeignKey('UserModel', on_delete=models.CASCADE)
    group = models.ForeignKey(
        'GroupModel', on_delete=models.CASCADE, related_name='invitation')
    time = models.DateTimeField(
        default=datetime.now, editable=False)

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Group Invitation Object"
        verbose_name_plural = "Group Invitation Objects"

    def __str__(self):
        return "Group Invitation from {} to {}".format(str(self.group), str(self.member))

    def clean(self):
        ''' Make sure this object does not yet exist '''
        member_not_in_group(self)
        unique_invitation(self)
