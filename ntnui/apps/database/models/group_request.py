from django.db import models
from datetime import datetime


def member_not_in_group(obj):
    if obj.member in obj.group:
        raise ValidationError("{} is already in {}".format(
            obj.member, obj.group))


def unique_request(obj):
    member = obj.member
    group = obj.group

    # If an invitation object with the same members exists, raise a validation error
    if GroupRequestModel.objects.filter(group=group, member=member):
        raise ValidationError(
            "{} has already requested to join {}".format(member, group))


class GroupRequestModel(models.Model):
    request_id = models.AutoField(primary_key=True)

    ''' Invitation details '''
    member = models.ForeignKey('UserModel', on_delete=models.CASCADE)
    group = models.ForeignKey(
        'GroupModel', on_delete=models.CASCADE, related_name='request')
    time = models.DateTimeField(
        default=datetime.now, editable=False)

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Group Request Object"
        verbose_name_plural = "Group Request Objects"

    def __str__(self):
        return "Group Request from {} to {}".format(str(self.member), str(self.group))

    def clean(self):
        ''' Make sure this object does not yet exist '''
        member_not_in_group(self)
        unique_request(self)
