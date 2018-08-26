from django.db import models
from .enums import LANGUAGE_CHOICES


class GroupMetaModel(models.Model):
    meta_id = models.AutoField(primary_key=True)

    # Contains the description of a group
    description = models.TextField(max_length=200)

    language = models.CharField(
        max_length=5, default="no", choices=LANGUAGE_CHOICES)

    ''' Meta group relationships '''
    group = models.OneToOneField('GroupModel', on_delete=models.CASCADE)

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Group Metadata"
        verbose_name_plural = "Group Metadata"

    def __str__(self):
        return "Meta object for {}".format(str(self.group))
