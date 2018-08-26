from django.db import models
from ..models import GroupModel
from django.core.exceptions import ValidationError


def validate_sub_groups(obj):
    if obj.parent_group == obj.child_group:
        raise ValidationError("A group cannot be a sub-group of itself!")


class GroupRelationshipModel(models.Model):
    ''' Group relationship information '''

    parent_group = models.ForeignKey(GroupModel, related_name="parent_group")
    child_group = models.ForeignKey(GroupModel, related_name="child_group")

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Group Relation"
        verbose_name_plural = "Group Relations"

    def __str__(self):
        return "(Parent) {} -> (Child) {}".format(self.parent_group, self.child_group)

    def clean(self):
        ''' This method is "magically" called by django whenever a model instance is saved '''
        validate_sub_groups(self)
