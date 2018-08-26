from django.db import models
from os import path


def get_upload_location(type, instance, filename):
    ''' Get upload location (todo: find a way to serialize...)'''

    if not type:
        return None

    if not instance:
        return None

    if not filename:
        return None

    return path.join(type, instance.group.slug, filename)


def get_upload_cover(instance, filename):
    return get_upload_location("cover_photo", instance, filename)


def get_upload_logo(instance, filename):
    return get_upload_location("logo", instance, filename)


class GroupMediaModel(models.Model):
    media_id = models.AutoField(primary_key=True)

    cover_photo = models.ImageField(
        upload_to=get_upload_cover, default="cover_photo/ntnui.png")

    logo = models.ImageField(upload_to=get_upload_logo,
                             default="logo/ntnui.svg")

    ''' Media group relationships '''
    group = models.OneToOneField('GroupModel', on_delete=models.CASCADE)

    class Meta:
        ''' Configure the name displayed in the admin panel '''
        verbose_name = "Group Media"
        verbose_name_plural = "Group Media"

    def __str__(self):
        return "Media object for {}".format(str(self.group))
